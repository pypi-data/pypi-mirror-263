import copy
import logging

return_rate_type_mapping = {
    "raw_return": "raw_return",
    "crud_return": "crud_return"
}


def build_join_clause(tables_to_use: list, return_type: str, mapper: dict, is_heatmap=False,
                      is_cohort_trend=False, expanded_cohorts_config=None,
                      is_primary_cohort_return_associated=False) -> str:
    logging.info('extra cohorts for join clause: %s', expanded_cohorts_config)
    tables_to_use = list(dict.fromkeys(tables_to_use))  # remove duplicate ctes
    if 'order_associated_values' in tables_to_use:
        # moving order_associated_values to last index of list
        # when we generate the join clause all the other ctes are joined
        # to the first ctes in the list. But when the first cte in list is
        # order_associated_values and the primary cohort is return_associated cohort
        # there won't be any joining key of order_associated_values and hences results in
        # cross join to all the other ctes. The issue will be seen when there are more than
        # 2 ctes.
        tables_to_use.remove('order_associated_values')
        tables_to_use.append('order_associated_values')

    clause = f"{tables_to_use[0]} as {mapper[tables_to_use[0]]}"
    if len(tables_to_use) == 1:
        return clause
    join_list = [clause]
    join_type = "join" if return_type == "crud_return" else "full join"
    for i in range(1, len(tables_to_use)):

        if is_heatmap:
            join_list.append(
                f"{join_type} {tables_to_use[i]} as {mapper[tables_to_use[i]]} on {mapper[tables_to_use[0]]}.cohort_x_={mapper[tables_to_use[i]]}.cohort_x_ and {mapper[tables_to_use[0]]}.cohort_y_={mapper[tables_to_use[i]]}.cohort_y_")

        elif is_cohort_trend:
            order_table_name = 'trend_ov'
            join_param = get_join_clause(tables_to_use, mapper, join_type, i, order_table_name, is_primary_cohort_return_associated=is_primary_cohort_return_associated)
            join_list.append(join_param + f" and {mapper[tables_to_use[0]]}.date_={mapper[tables_to_use[i]]}.date_")
        else:

            # if the primary cohort is return associated and tables to use is order_associated_values,
            # we should not include it in join clause. The reason being, return associated cohorts are not included
            # while calculating order associated values in query level.
            order_table_name = 'ov'
            join_param = get_join_clause(tables_to_use, mapper, join_type, i, order_table_name, is_primary_cohort_return_associated=is_primary_cohort_return_associated)

            if expanded_cohorts_config and len(expanded_cohorts_config) > 0:
                for cohort_config in expanded_cohorts_config:
                    if not (cohort_config['is_return_associated'] and (mapper[tables_to_use[0]] == order_table_name or
                                                                       mapper[tables_to_use[i]] == order_table_name)):
                        join_param = join_param + f" and {mapper[tables_to_use[0]]}.cohort_name_{cohort_config['name']}={mapper[tables_to_use[i]]}.cohort_name_{cohort_config['name']}"

            join_list.append(join_param)

    return " ".join(join_list)


def get_join_clause(tables_to_use, mapper, join_type, index, order_table_name, is_primary_cohort_return_associated: bool = False):
    if (is_primary_cohort_return_associated and (mapper[tables_to_use[0]] == order_table_name or
                                                 mapper[tables_to_use[index]] == order_table_name)):
        join_param = f'{join_type} {tables_to_use[index]} as {mapper[tables_to_use[index]]} on 1=1'
    else:
        join_param = f'{join_type} {tables_to_use[index]} as {mapper[tables_to_use[index]]} on {mapper[tables_to_use[0]]}.cohort_name_={mapper[tables_to_use[index]]}.cohort_name_'

    return join_param


def generate_quality_operation(ctes_to_use: list, join_keys: list, equality_op: str = "=") -> list:
    result = []
    for join_key in join_keys:
        clause_output = []
        for cte in ctes_to_use:
            clause_output.append(f"{cte['alias']}.{join_key}")
        if clause_output:
            result.append(f" {equality_op} ".join(clause_output))
    return result


def concat_list_with_prefix(cohorts: list, join_op: str = ",", prefix: str = "", postfix: str = "") -> str:
    clause = f" {join_op} ".join(cohorts)
    return f"{prefix} {clause}{postfix}"


# mapping of kpi and the associated CTE
# based on it we can determine which of the CTEs are requried for the incoming request
tables_to_use_mappings = {
    'total_items_returned': ['return_associated_values'],
    'total_items_sold': ['order_associated_values'],
    'total_revenue_sold': ['order_associated_values'],
    'total_return_revenue': ['return_associated_values'],
    'total_return_cost': ['return_associated_values'],
    'total_profit_loss': ['return_associated_values'],
    'total_unsellable_items_returned': ['return_associated_values'],
    'rank': ['return_associated_values', 'order_associated_values'],
    'best_performer': ['return_associated_values', 'order_associated_values'],
    'items_returned_vs_items_sold': ['return_associated_values', 'order_associated_values'],
    'return_revenue_vs_revenue_sold': ['return_associated_values', 'order_associated_values'],
    'total_unique_items_returned': ['return_associated_values'],
    'average_order_value': ['order_associated_values', 'return_associated_values'],
    'total_customers': ['return_associated_values'],
    'post_return_repurchase_rate': ['only_returns_associated_values'],
    'repurchase_rate': ['order_associated_values'],
    'unsellable_percent': ['return_associated_values'],
    'distinct_order_count': ['order_associated_values'],
    'revenue_sold_orv': ['return_associated_values'],
    'average_unit_selling_price': ['aur_values'],
    'style_repurchase_time': ['order_associated_values'],
    'time_to_repurchase': ['order_associated_values'],
    'style_repurchase_rate': ['order_associated_values'],
    'recoverable_revenue': ['order_associated_values'],
    'total_returning_customers': ['return_associated_values'],
    'star_rating': ['order_associated_values'],
    'damaged_percentage': ['return_associated_values'],
    'total_distinct_order_count': ['order_associated_values'],
    'net_revenue': ['order_associated_values', 'return_associated_values'],
    'net_lost_revenue': ['return_associated_values'],
}

raw_returns_tables_to_use_mappings = {
    'average_order_value': ['order_or_return_associated_values'],
    'distinct_order_count': ['order_or_return_associated_values'],
    'total_customers': ['order_or_return_associated_values'],
    'total_distinct_order_count': ['order_or_return_associated_values'],
}

# NOTE!: Needs better logic
cohort_trend_table_mappings = {
    'total_items_returned': ['main_return_associated_values'],
    'total_items_sold': ['main_order_associated_values'],
    'total_revenue_lost': ['main_order_associated_values'],
    'total_revenue_sold': ['main_order_associated_values'],
    'total_return_revenue': ['main_return_associated_values'],
    'total_return_cost': ['main_return_associated_values'],
    'total_profit_loss': ['main_return_associated_values'],
    'total_unsellable_items_returned': ['main_return_associated_values'],
    'rank': ['main_return_associated_values', 'main_order_associated_values'],
    'best_performer': ['main_return_associated_values', 'main_order_associated_values'],
    'items_returned_vs_items_sold': ['main_return_associated_values', 'main_order_associated_values'],
    'return_revenue_vs_revenue_sold': ['main_return_associated_values', 'main_order_associated_values'],
    'total_unique_items_returned': ['main_return_associated_values'],
    'average_order_value': ['main_order_associated_values'],
    'total_customers': ['main_return_associated_values'],
    'post_return_repurchase_rate': ['main_only_returns_associated_values'],
    'repurchase_rate': ['main_order_associated_values'],
    'unsellable_percent': ['main_return_associated_values'],
    'distinct_order_count': ['main_order_associated_values'],
    'revenue_sold_orv': ['main_return_associated_values'],
    'average_unit_selling_price': ['trend_aur_values'],
    'style_repurchase_time': ['main_order_associated_values'],
    'style_repurchase_rate': ['main_order_associated_values'],
    'time_to_repurchase': ['main_order_associated_values'],
    'recoverable_revenue': ['main_order_associated_values'],
    'total_returning_customers': ['main_return_associated_values'],
    'star_rating': ['main_order_associated_values'],
    'damaged_percentage': ['main_return_associated_values'],
    'total_distinct_order_count': ['main_order_associated_values'],
    'net_revenue': ['main_order_associated_values', 'main_return_associated_values'],
    'net_lost_revenue': ['main_return_associated_values'],
}

cohort_trend_raw_table_mappings = {
    'average_order_value': ['main_order_or_return_associated_values'],
    'total_customers': ['main_order_or_return_associated_values'],
    'distinct_order_count': ['main_order_or_return_associated_values'],
    'total_distinct_order_count': ['main_order_or_return_associated_values'],
    'total_returning_customers': ['main_return_associated_values'],
    'post_return_repurchase_rate': ['main_return_associated_values'],
}


def get_cohort_trend_table_mapping(return_rate_type=None):
    table_to_use = copy.deepcopy(cohort_trend_table_mappings)
    if return_rate_type == "raw_return":
        table_to_use.update(cohort_trend_raw_table_mappings)
    return table_to_use


def get_tables_to_use_mappings(return_rate_type=None):
    table_to_use = copy.deepcopy(tables_to_use_mappings)
    if return_rate_type == "raw_return":
        table_to_use.update(raw_returns_tables_to_use_mappings)
    return table_to_use


# mapping of CTEs and the fields associated under the corresponding CTE
# all the fields should be listed in computed_fields as well
field_type_mapper = {
    "return_associated_fields": ['items_returned', 'profit_loss', 'unsellable_items_returned', 'repeat_customers',
                                 'return_revenue', 'return_cost', 't_customers',
                                 'total_unique_customers', 'overall_return_revenue', 'unique_items_returned',
                                 'revenue_sold_orv', 'return_customer_count', 'dmg_percentage', 'exchanged_revenue_'],
    "order_associated_fields": ['items_sold', 'revenue_sold_', 'r_rate', 'avg_time_to_repurchase',
                                'avg_style_repurchase_time', 'repurchasing_customers', 'repurchase_time_sum',
                                'total_purchased_customers_', 'is_style_repurchase', 'overall_revenue_sold',
                                'baseline_revenue_lost', 'total_baseline_revenue_lost', 'return_revenue_', 'avg_rating',
                                'distinct_order_count', 'avg_order_value'],
    "aur_fields": ['t_item_count', 't_item_price', 'average_item_price'],
    "pr_fields": ['is_returner', 'pr_repurchase_rate', 'pr_customer_sum'],
    "select_fields": ['total_items_sold', 'total_return_cost',
                      'total_revenue_sold',
                      'total_return_revenue',
                      'total_profit_loss',
                      'post_return_repurchase_rate',
                      'total_items_returned',
                      'items_returned_vs_items_sold',
                      'return_revenue_vs_revenue_sold',
                      'repeat_customers_count',
                      'unique_customers',
                      'total_purchased_customers',
                      'total_unsellable_items_returned',
                      'unsellable_percent',
                      'total_revenue_sold_orv',
                      'rank',
                      'best_performer',
                      'repurchase_rate',
                      'average_order_value',
                      'total_customers',
                      'total_unique_items_returned',
                      'total_revenue_sold_orv',
                      'total_distinct_order_count',
                      'average_unit_selling_price',
                      'total_item_price',
                      'total_item_count',
                      'style_repurchase_time',
                      'time_to_repurchase',
                      'total_repurchase_time_delta',
                      'total_repurchasing_customers',
                      'style_repurchase_rate',
                      'overall_avg_return_revenue_vs_revenue_sold',
                      'recoverable_revenue',
                      'style_repurchase_rate',
                      'total_returning_customers',
                      'star_rating',
                      'damaged_percentage',
                      'net_revenue',
                      'total_exchanged_revenue',
                      'net_lost_revenue'
                      ]
}

raw_field_type_mapper = {
    "order_or_return_associated_fields": ['t_customers', 'avg_order_value', 'revenue_sold_orv', 'distinct_order_count',
                                          'total_unique_customers', 'avg_order_value'],
    "return_associated_fields": ['items_returned', 'profit_loss', 'unsellable_items_returned', 'repeat_customers',
                                 'return_revenue', 'return_cost', 'overall_return_revenue', 'unique_items_returned',
                                 'return_customer_count', 'dmg_percentage', 'exchanged_revenue_'],
    "order_associated_fields": ['items_sold', 'revenue_sold_', 'r_rate', 'avg_time_to_repurchase',
                                'avg_style_repurchase_time', 'repurchasing_customers', 'repurchase_time_sum',
                                'total_purchased_customers_', 'is_style_repurchase', 'overall_revenue_sold',
                                'baseline_revenue_lost', 'total_baseline_revenue_lost', 'return_revenue_', 'avg_rating']
}


def get_field_type_mapper(return_type="None"):
    filter_type = copy.deepcopy(field_type_mapper)
    if return_type == return_rate_type_mapping["raw_return"]:
        filter_type.update(raw_field_type_mapper)

    return filter_type


subquery_alias_mapping = {
    'return_associated_values': 'rv',
    'order_associated_values': 'ov',
    'aur_values': 'av',
    'only_returns_associated_values': 'pr',
    'order_or_return_associated_values': 'orv',
    'main_return_associated_values': 'trend_rv',
    'main_order_associated_values': 'trend_ov',
    'trend_aur_values': 'trend_av',
    'main_only_returns_associated_values': 'trend_pr',
    'main_order_or_return_associated_values': 'trend_orv',
}


def generate_template(return_rate_type, crud_return_template, raw_return_template):
    if return_rate_type == return_rate_type_mapping["crud_return"]:
        return crud_return_template

    return raw_return_template
