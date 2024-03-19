use super::*;

// Information concerning individual sides of a join.
#[derive(PartialEq, Eq)]
struct LeftRight<T>(T, T);

fn should_block_join_specific(
    ae: &AExpr,
    how: &JoinType,
    on_names: &PlHashSet<Arc<str>>,
    expr_arena: &Arena<AExpr>,
    schema_left: &Schema,
    schema_right: &Schema,
) -> LeftRight<bool> {
    use AExpr::*;
    match ae {
        // joins can produce null values
        Function {
            function:
                FunctionExpr::Boolean(BooleanFunction::IsNotNull)
                | FunctionExpr::Boolean(BooleanFunction::IsNull)
                | FunctionExpr::FillNull { .. },
            ..
        } => join_produces_null(how),
        #[cfg(feature = "is_in")]
        Function {
            function: FunctionExpr::Boolean(BooleanFunction::IsIn),
            ..
        } => join_produces_null(how),
        // joins can produce duplicates
        #[cfg(feature = "is_unique")]
        Function {
            function:
                FunctionExpr::Boolean(BooleanFunction::IsUnique)
                | FunctionExpr::Boolean(BooleanFunction::IsDuplicated),
            ..
        } => LeftRight(true, true),
        #[cfg(feature = "is_first_distinct")]
        Function {
            function: FunctionExpr::Boolean(BooleanFunction::IsFirstDistinct),
            ..
        } => LeftRight(true, true),
        // any operation that checks for equality or ordering can be wrong because
        // the join can produce null values
        // TODO! check if we can be less conservative here
        BinaryExpr { op, left, right } => match op {
            Operator::NotEq => LeftRight(false, false),
            Operator::Eq => {
                let LeftRight(bleft, bright) = join_produces_null(how);

                let l_name = aexpr_output_name(*left, expr_arena).unwrap();
                let r_name = aexpr_output_name(*right, expr_arena).unwrap();

                let is_in_on = on_names.contains(&l_name) || on_names.contains(&r_name);

                let block_left =
                    is_in_on && (schema_left.contains(&l_name) || schema_left.contains(&r_name));
                let block_right =
                    is_in_on && (schema_right.contains(&l_name) || schema_right.contains(&r_name));
                LeftRight(block_left | bleft, block_right | bright)
            },
            _ => join_produces_null(how),
        },
        _ => LeftRight(false, false),
    }
}

fn join_produces_null(how: &JoinType) -> LeftRight<bool> {
    #[cfg(feature = "asof_join")]
    {
        match how {
            JoinType::Left => LeftRight(false, true),
            JoinType::Outer { .. } | JoinType::Cross | JoinType::AsOf(_) => LeftRight(true, true),
            _ => LeftRight(false, false),
        }
    }
    #[cfg(not(feature = "asof_join"))]
    {
        match how {
            JoinType::Left => LeftRight(false, true),
            JoinType::Outer { .. } | JoinType::Cross => LeftRight(true, true),
            _ => LeftRight(false, false),
        }
    }
}

fn all_pred_cols_in_left_on(
    predicate: Node,
    expr_arena: &mut Arena<AExpr>,
    left_on: &[Node],
) -> bool {
    let left_on_col_exprs: Vec<Expr> = left_on
        .iter()
        .map(|&node| node_to_expr(node, expr_arena))
        .collect();
    let mut col_exprs_in_predicate = aexpr_to_column_nodes_iter(predicate, expr_arena)
        .map(|node| node_to_expr(node, expr_arena));

    col_exprs_in_predicate.all(|expr| left_on_col_exprs.contains(&expr))
}

#[allow(clippy::too_many_arguments)]
pub(super) fn process_join(
    opt: &PredicatePushDown,
    lp_arena: &mut Arena<ALogicalPlan>,
    expr_arena: &mut Arena<AExpr>,
    input_left: Node,
    input_right: Node,
    left_on: Vec<Node>,
    right_on: Vec<Node>,
    schema: SchemaRef,
    options: Arc<JoinOptions>,
    acc_predicates: PlHashMap<Arc<str>, Node>,
) -> PolarsResult<ALogicalPlan> {
    use ALogicalPlan::*;
    let schema_left = lp_arena.get(input_left).schema(lp_arena);
    let schema_right = lp_arena.get(input_right).schema(lp_arena);

    let on_names = left_on
        .iter()
        .flat_map(|n| aexpr_to_leaf_names_iter(*n, expr_arena))
        .chain(
            right_on
                .iter()
                .flat_map(|n| aexpr_to_leaf_names_iter(*n, expr_arena)),
        )
        .collect::<PlHashSet<_>>();

    let mut pushdown_left = init_hashmap(Some(acc_predicates.len()));
    let mut pushdown_right = init_hashmap(Some(acc_predicates.len()));
    let mut local_predicates = Vec::with_capacity(acc_predicates.len());

    for (_, predicate) in acc_predicates {
        // check if predicate can pass the joins node
        let block_pushdown_left = has_aexpr(predicate, expr_arena, |ae| {
            should_block_join_specific(
                ae,
                &options.args.how,
                &on_names,
                expr_arena,
                &schema_left,
                &schema_right,
            )
            .0
        });
        let block_pushdown_right = has_aexpr(predicate, expr_arena, |ae| {
            should_block_join_specific(
                ae,
                &options.args.how,
                &on_names,
                expr_arena,
                &schema_left,
                &schema_right,
            )
            .1
        });

        // these indicate to which tables we are going to push down the predicate
        let mut filter_left = false;
        let mut filter_right = false;

        debug_assert_aexpr_allows_predicate_pushdown(predicate, expr_arena);

        if !block_pushdown_left && check_input_node(predicate, &schema_left, expr_arena) {
            insert_and_combine_predicate(&mut pushdown_left, predicate, expr_arena);
            filter_left = true;
            // If we push down to the left and all predicate columns are also
            // join columns, we also push down right for inner, left or semi join
            if all_pred_cols_in_left_on(predicate, expr_arena, &left_on) {
                filter_right = match &options.args.how {
                    // TODO! if join_on right has a different name
                    // we can set this to `true` IFF we rename the predicate
                    JoinType::Inner | JoinType::Left => {
                        check_input_node(predicate, &schema_right, expr_arena)
                    },
                    #[cfg(feature = "semi_anti_join")]
                    JoinType::Semi => check_input_node(predicate, &schema_right, expr_arena),
                    _ => false,
                }
            }
        // this is `else if` because if the predicate is in the left hand side
        // the right hand side should be renamed with the suffix.
        // in that case we should not push down as the user wants to filter on `x`
        // not on `x_rhs`.
        } else if !block_pushdown_right && check_input_node(predicate, &schema_right, expr_arena) {
            filter_right = true
        }
        if filter_right {
            insert_and_combine_predicate(&mut pushdown_right, predicate, expr_arena);
        }

        match (filter_left, filter_right, &options.args.how) {
            // if not pushed down on one of the tables we have to do it locally.
            (false, false, _) |
            // if left join and predicate only available in right table,
            // 'we should not filter right, because that would lead to
            // invalid results.
            // see: #2057
            (false, true, JoinType::Left)
            => {
                local_predicates.push(predicate);
                continue;
            },
            // business as usual
            _ => {}
        }
    }

    opt.pushdown_and_assign(input_left, pushdown_left, lp_arena, expr_arena)?;
    opt.pushdown_and_assign(input_right, pushdown_right, lp_arena, expr_arena)?;

    let lp = Join {
        input_left,
        input_right,
        left_on,
        right_on,
        schema,
        options,
    };
    Ok(opt.optional_apply_predicate(lp, local_predicates, lp_arena, expr_arena))
}
