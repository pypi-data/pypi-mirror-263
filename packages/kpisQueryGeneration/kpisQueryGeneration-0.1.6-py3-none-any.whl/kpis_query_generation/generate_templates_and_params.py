from kpis_query_generation.return_summary.sql_tempates import kpi_fetch_template, raw_kpi_fetch_template
from kpis_query_generation.utils.query_templating.query_utils import generate_template, get_field_type_mapper
from kpis_query_generation.utils.query_templating.computed_fileds_config import get_computed_fields
from kpis_query_generation.utils.query_templating.computed_field_util import get_computed_fields_query
from kpis_query_generation.return_trend import sql_template as trend_template


def generate_kpi_summary_template(return_rate_type):
    return generate_template(return_rate_type, kpi_fetch_template, raw_kpi_fetch_template)

def generate_kpi_summary_params(filters, where_clause, cohort, is_return_associated_cohort, cohort_filter_query, kpis_to_calculate, return_rate_type):
    # build computed fields query snippets
    computed_fields = get_computed_fields()
    field_type_mapper = get_field_type_mapper(return_rate_type)
    computed_fields_queries = get_computed_fields_query(computed_fields, kpis_to_calculate, field_type_mapper,
                                                        ['return_associated_fields', 'order_associated_fields',
                                                         'order_or_return_associated_fields', 'pr_fields', 'aur_fields',
                                                         'select_fields'])
    data = {
        "filters": filters,
        "where_clause": where_clause,
        "cohort_name": cohort,
        "is_return_associated_cohort": is_return_associated_cohort,
        "cohort_filter_query": cohort_filter_query,
        "computed_fields_rv": computed_fields_queries['return_associated_fields'],
        "computed_fields_ov": computed_fields_queries['order_associated_fields'],
        "computed_fields_orv": computed_fields_queries['order_or_return_associated_fields'],
        "computed_fields_pr": computed_fields_queries['pr_fields'],
        "computed_fields_aur": computed_fields_queries['aur_fields'],
        "computed_fields_select": computed_fields_queries['select_fields'],
    }

    return data

def generate_kpi_trend_query_template(return_rate_type):
    return generate_template(return_rate_type, trend_template.kpi_fetch, trend_template.net_kpi_fetch)

def generate_kpi_trend_query_params(filters, where_clause, cohort, is_return_associated_cohort, cohort_filter_query, kpis_to_calculate, return_rate_type, date_query_order_shipped_at, date_query_items_returned_at):
    computed_fields = get_computed_fields()
    field_type_mapper = get_field_type_mapper(return_rate_type)

    computed_fields_queries = get_computed_fields_query(computed_fields, kpis_to_calculate, field_type_mapper,
                                                        ['return_associated_fields', 'order_associated_fields',
                                                         'pr_fields', 'order_or_return_associated_fields', 'aur_fields',
                                                         'select_fields'])

    data = {
        "filters": filters,
        "cohort_name": cohort,
        "is_return_associated_cohort": is_return_associated_cohort,
        "where_clause": where_clause,
        "cohort_filter_query": cohort_filter_query,
        'computed_fields_rv': computed_fields_queries['return_associated_fields'],
        'computed_fields_ov': computed_fields_queries['order_associated_fields'],
        'computed_fields_orv': computed_fields_queries['order_or_return_associated_fields'],
        'computed_fields_pr': computed_fields_queries['pr_fields'],
        'computed_fields_aur': computed_fields_queries['aur_fields'],
        'computed_fields_select': computed_fields_queries['select_fields'],
        'date_query_order_shipped_at': date_query_order_shipped_at,
        'date_query_items_returned_at': date_query_items_returned_at,
    }

    return data