from typing import List, Dict

from jinjasql import JinjaSql

jSql = JinjaSql()


def build_query_snippet(fields: List[str], computed_fields_config: List[Dict]) -> str:
    """
        Returns kpi expressions from the provided config and computed_fields
        fields: list of kpi/fields of which sql snippet is to be generated
        computed_fields_config: config containing name and corresponding expression of kpi/field
    """
    if not fields:
        return ''
    matched_computed_fields = filter(lambda x: x.get('name') in fields, computed_fields_config)
    template = '''
        {% for kpi in kpis %}
            {% if kpi.expression %}
                {{ kpi.expression | sqlsafe }} as {{ kpi.name | sqlsafe }}
            {% endif %}
        {% endfor %}
    '''
    data = {
        'kpis': matched_computed_fields
    }
    query, _ = jSql.prepare_query(template, data)
    return query


def get_dependent_computed_fields(fields: List[str], computed_fields: List[Dict]) -> List[str]:
    if not fields:
        return []

    return get_dependent_fields_by_name(fields[0], computed_fields) + \
        get_dependent_computed_fields(fields[1:], computed_fields)


def get_dependent_fields_by_name(name: str, computed_fields: List[Dict]) -> List[str]:
    computed_fields_by_name = [
        *filter(lambda x: x.get('name') == name, computed_fields)]

    if not computed_fields_by_name:
        return []

    if len(computed_fields_by_name) > 1:
        raise BaseException(f'multiple computed fields found for the field `{name}`')

    field = computed_fields_by_name[0]
    if 'depends_on' in field:
        return list(set([name] + field.get('depends_on') + get_dependent_computed_fields(field.get('depends_on'),
                                                                                         computed_fields)))

    return [name]


def get_computed_fields_query(computed_fields: List, kpis_to_calculate: List[str], cte_to_field_mapper: Dict,
                              ctes: List[str]) -> Dict:
    required_fields = list(
        set(get_dependent_computed_fields(kpis_to_calculate, computed_fields)))

    result = {}
    for cte in ctes:
        fields = filter_kpi_fields(
            required_fields, cte_to_field_mapper.get(cte, []))
        result[cte] = build_query_snippet(fields, computed_fields)

    return result


def filter_kpi_fields(required_fields: List[str], cte_fields: List[str]) -> List[str]:
    return list(filter(lambda x: x in cte_fields, required_fields))

# if the primary cohort is return associated,
# we should not include it in select clause of order associated values.


def get_select_cohort_query(table_mapper, tables_to_use, order_table_name, is_primary_cohort_return_associated=False):
    cohorts = [
        f"{table_mapper[table]}.cohort_name_" for table in tables_to_use if not (
            is_primary_cohort_return_associated and table_mapper[table] == order_table_name
        )]
    cohort_adj = ",".join(cohorts)
    select_cohort_query = f"COALESCE({cohort_adj}, 'None') as cohort_name"
    return select_cohort_query


def get_select_cohortname(tables_to_use, table_mapper, is_heatmap=False, is_cohort_trend=False,
                          no_default_coalesce: bool = False, select_column_key: str = None,
                          expanded_cohorts_config=None,
                          is_primary_cohort_return_associated=False):
    if is_heatmap:
        cohorts_y = [
            f"{table_mapper[table]}.cohort_y_" for table in tables_to_use]
        cohort_adj_y = ",".join(cohorts_y)

        cohorts_x = [
            f"{table_mapper[table]}.cohort_x_" for table in tables_to_use]
        cohort_adj_x = ",".join(cohorts_x)

        return f"COALESCE({cohort_adj_x}, 'None') as cohort_x, COALESCE({cohort_adj_y}, 'None') as cohort_y"

    # !NOTE: Needs better logic
    if is_cohort_trend:
        order_table_name = 'trend_ov'
        select_cohort_query = get_select_cohort_query(table_mapper, tables_to_use, order_table_name, is_primary_cohort_return_associated=is_primary_cohort_return_associated)

        date = [f"{table_mapper[table]}.date_" for table in tables_to_use]
        date_adj = ",".join(date)
        if len(date) == 1:
            return f"{date_adj} as date, {select_cohort_query}"

        return f"COALESCE({date_adj}) as date, {select_cohort_query}"

    if no_default_coalesce:
        cohorts = [
            f"{table_mapper[table]}.{select_column_key}" for table in tables_to_use]
        cohort_adj = ",".join(cohorts)
        return f"coalesce({cohort_adj}) as {select_column_key}"

    order_table_name = 'ov'
    select_cohort_query = get_select_cohort_query(table_mapper, tables_to_use, order_table_name, is_primary_cohort_return_associated=is_primary_cohort_return_associated)

    if expanded_cohorts_config and len(expanded_cohorts_config) > 0:
        for cohort_config in expanded_cohorts_config:
            cohorts = [
                f"{table_mapper[table]}.cohort_name_{cohort_config['name']}"
                for table in tables_to_use if not (
                    cohort_config['is_return_associated'] and table_mapper[table] == order_table_name)]
            cohort_adj = ",".join(cohorts)
            select_cohort_query = select_cohort_query + f",COALESCE({cohort_adj}, 'None') as cohort_name_{cohort_config['name']}"
    return select_cohort_query
