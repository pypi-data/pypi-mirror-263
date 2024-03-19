use polars_core::prelude::*;

use crate::prelude::*;

mod cache_states;
#[cfg(feature = "cse")]
mod cse;
mod delay_rechunk;
mod drop_nulls;

mod collect_members;
mod count_star;
#[cfg(feature = "cse")]
mod cse_expr;
mod fast_projection;
#[cfg(any(
    feature = "ipc",
    feature = "parquet",
    feature = "csv",
    feature = "cse",
    feature = "json"
))]
pub(crate) mod file_caching;
mod flatten_union;
#[cfg(feature = "fused")]
mod fused;
mod predicate_pushdown;
mod projection_pushdown;
mod simplify_expr;
mod simplify_functions;
mod slice_pushdown_expr;
mod slice_pushdown_lp;
mod stack_opt;
mod type_coercion;

use delay_rechunk::DelayRechunk;
use drop_nulls::ReplaceDropNulls;
use fast_projection::FastProjectionAndCollapse;
use polars_io::predicates::PhysicalIoExpr;
pub use predicate_pushdown::PredicatePushDown;
pub use projection_pushdown::ProjectionPushDown;
pub use simplify_expr::{SimplifyBooleanRule, SimplifyExprRule};
use slice_pushdown_lp::SlicePushDown;
pub use stack_opt::{OptimizationRule, StackOptimizer};
pub use type_coercion::TypeCoercionRule;

use self::flatten_union::FlattenUnionRule;
pub use crate::frame::{AllowedOptimizations, OptState};
use crate::logical_plan::optimizer::count_star::CountStar;
#[cfg(feature = "cse")]
use crate::logical_plan::optimizer::cse_expr::CommonSubExprOptimizer;
use crate::logical_plan::optimizer::predicate_pushdown::HiveEval;
#[cfg(feature = "cse")]
use crate::logical_plan::visitor::*;
use crate::prelude::optimizer::collect_members::MemberCollector;

pub trait Optimize {
    fn optimize(&self, logical_plan: LogicalPlan) -> PolarsResult<LogicalPlan>;
}

// arbitrary constant to reduce reallocation.
const HASHMAP_SIZE: usize = 16;

pub(crate) fn init_hashmap<K, V>(max_len: Option<usize>) -> PlHashMap<K, V> {
    PlHashMap::with_capacity(std::cmp::min(max_len.unwrap_or(HASHMAP_SIZE), HASHMAP_SIZE))
}

pub fn optimize(
    logical_plan: LogicalPlan,
    opt_state: OptState,
    lp_arena: &mut Arena<ALogicalPlan>,
    expr_arena: &mut Arena<AExpr>,
    scratch: &mut Vec<Node>,
    hive_partition_eval: HiveEval<'_>,
) -> PolarsResult<Node> {
    // get toggle values
    let predicate_pushdown = opt_state.predicate_pushdown;
    let projection_pushdown = opt_state.projection_pushdown;
    let type_coercion = opt_state.type_coercion;
    let simplify_expr = opt_state.simplify_expr;
    let slice_pushdown = opt_state.slice_pushdown;
    let streaming = opt_state.streaming;
    let fast_projection = opt_state.fast_projection;
    // Don't run optimizations that don't make sense on a single node.
    // This keeps eager execution more snappy.
    let eager = opt_state.eager;
    #[cfg(feature = "cse")]
    let comm_subplan_elim = opt_state.comm_subplan_elim && !eager;

    #[cfg(feature = "cse")]
    let comm_subexpr_elim = opt_state.comm_subexpr_elim;
    #[cfg(not(feature = "cse"))]
    let comm_subexpr_elim = false;

    #[allow(unused_variables)]
    let agg_scan_projection = opt_state.file_caching && !streaming && !eager;

    // gradually fill the rules passed to the optimizer
    let opt = StackOptimizer {};
    let mut rules: Vec<Box<dyn OptimizationRule>> = Vec::with_capacity(8);

    // during debug we check if the optimizations have not modified the final schema
    #[cfg(debug_assertions)]
    let prev_schema = logical_plan.schema()?.into_owned();

    let mut lp_top = to_alp(logical_plan, expr_arena, lp_arena)?;

    // Collect members for optimizations that need it.
    let mut members = MemberCollector::new();
    if !eager && (comm_subexpr_elim || projection_pushdown) {
        members.collect(lp_top, lp_arena)
    }

    #[cfg(feature = "cse")]
    let cse_plan_changed = if comm_subplan_elim {
        let (lp, changed) = cse::elim_cmn_subplans(lp_top, lp_arena, expr_arena);
        lp_top = lp;
        members.has_cache |= changed;
        changed
    } else {
        false
    };
    #[cfg(not(feature = "cse"))]
    let cse_plan_changed = false;

    // we do simplification
    if simplify_expr {
        rules.push(Box::new(SimplifyExprRule {}));
        #[cfg(feature = "fused")]
        rules.push(Box::new(fused::FusedArithmetic {}));
    }

    // should be run before predicate pushdown
    if projection_pushdown {
        let mut projection_pushdown_opt = ProjectionPushDown::new();
        let alp = lp_arena.take(lp_top);
        let alp = projection_pushdown_opt.optimize(alp, lp_arena, expr_arena)?;
        lp_arena.replace(lp_top, alp);

        if members.has_joins_or_unions && members.has_cache {
            cache_states::set_cache_states(lp_top, lp_arena, expr_arena, scratch, cse_plan_changed);
        }

        if projection_pushdown_opt.is_count_star {
            let mut count_star_opt = CountStar::new();
            count_star_opt.optimize_plan(lp_arena, expr_arena, lp_top);
        }
    }

    if predicate_pushdown {
        let predicate_pushdown_opt = PredicatePushDown::new(hive_partition_eval);
        let alp = lp_arena.take(lp_top);
        let alp = predicate_pushdown_opt.optimize(alp, lp_arena, expr_arena)?;
        lp_arena.replace(lp_top, alp);
    }

    // make sure its before slice pushdown.
    if fast_projection {
        rules.push(Box::new(FastProjectionAndCollapse::new(eager)));
    }

    if !eager {
        rules.push(Box::new(DelayRechunk::new()));
    }

    if slice_pushdown {
        let slice_pushdown_opt = SlicePushDown::new(streaming);
        let alp = lp_arena.take(lp_top);
        let alp = slice_pushdown_opt.optimize(alp, lp_arena, expr_arena)?;

        lp_arena.replace(lp_top, alp);

        // expressions use the stack optimizer
        rules.push(Box::new(slice_pushdown_opt));
    }
    if type_coercion {
        rules.push(Box::new(TypeCoercionRule {}))
    }
    // this optimization removes branches, so we must do it when type coercion
    // is completed
    if simplify_expr {
        rules.push(Box::new(SimplifyBooleanRule {}));
    }

    // make sure that we do that once slice pushdown
    // and predicate pushdown are done. At that moment
    // the file fingerprints are finished.
    #[cfg(any(feature = "cse", feature = "parquet", feature = "ipc", feature = "csv"))]
    if agg_scan_projection || cse_plan_changed {
        // we do this so that expressions are simplified created by the pushdown optimizations
        // we must clean up the predicates, because the agg_scan_projection
        // uses them in the hashtable to determine duplicates.
        let simplify_bools = &mut [Box::new(SimplifyBooleanRule {}) as Box<dyn OptimizationRule>];
        lp_top = opt.optimize_loop(simplify_bools, expr_arena, lp_arena, lp_top)?;

        // scan the LP to aggregate all the column used in scans
        // these columns will be added to the state of the AggScanProjection rule
        let mut file_predicate_to_columns_and_count = PlHashMap::with_capacity(32);
        find_column_union_and_fingerprints(
            lp_top,
            &mut file_predicate_to_columns_and_count,
            lp_arena,
            expr_arena,
        );

        let mut file_cacher = FileCacher::new(file_predicate_to_columns_and_count);
        file_cacher.assign_unions(lp_top, lp_arena, expr_arena, scratch);

        #[cfg(feature = "cse")]
        if cse_plan_changed {
            // this must run after cse
            cse::decrement_file_counters_by_cache_hits(lp_top, lp_arena, expr_arena, 0, scratch);
        }
    }

    rules.push(Box::new(ReplaceDropNulls {}));
    if !eager {
        rules.push(Box::new(FlattenUnionRule {}));
    }

    lp_top = opt.optimize_loop(&mut rules, expr_arena, lp_arena, lp_top)?;

    // This one should run (nearly) last as this modifies the projections
    #[cfg(feature = "cse")]
    if comm_subexpr_elim && !members.has_ext_context {
        let mut optimizer = CommonSubExprOptimizer::new(expr_arena);
        lp_top = ALogicalPlanNode::with_context(lp_top, lp_arena, |alp_node| {
            alp_node.rewrite(&mut optimizer)
        })?
        .node()
    }

    // during debug we check if the optimizations have not modified the final schema
    #[cfg(debug_assertions)]
    {
        // only check by names because we may supercast types.
        assert_eq!(
            prev_schema.iter_names().collect::<Vec<_>>(),
            lp_arena
                .get(lp_top)
                .schema(lp_arena)
                .iter_names()
                .collect::<Vec<_>>()
        );
    };

    Ok(lp_top)
}
