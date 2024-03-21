kpi_fetch = """
    with placeHolder as (
        SELECT NULL
    )
{% if computed_fields_rv %}
    ,main_return_associated_values as (
        select {{date_query_order_shipped_at | sqlsafe}} AS date_rv
            {{computed_fields_rv | sqlsafe}}
        from product_analysis_mv
        where 1=1
        {% if filters.start %}
            and order_shipped_at >= {{filters.start}}
        {% endif %}
        {% if filters.stop %}
            and order_shipped_at <= {{filters.stop}}
        {% endif %}

        {% if where_clause and where_clause.order %}
            {{where_clause.order | sqlsafe}}
        {% endif %}
         {% if cohort_filter_query %}
            and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
        {% endif %}
        group by date_rv
    )
{% endif %}
{% if computed_fields_pr %}
    ,main_only_returns_associated_values AS (
        select {{date_query_items_returned_at | sqlsafe}} as date_prv
            {{computed_fields_pr | sqlsafe}}
        from product_analysis_mv
    where 1=1
    AND items_returned_at is not NULL
    {% if filters.start %}
        and items_returned_at >= {{filters.start}}
    {% endif %}
    {% if filters.stop %}
        and items_returned_at <= {{filters.stop}}
    {% endif %}

    {% if where_clause and where_clause.order %}
        {{where_clause.order | sqlsafe}}
    {% endif %}
    {% if cohort_filter_query %}
        and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
    {% endif %}
    group by date_prv )
{% endif %}
{% if computed_fields_ov %}
    ,main_order_associated_values as (
            select {{date_query_order_shipped_at | sqlsafe}} AS date_ov
                    {{computed_fields_ov | sqlsafe}}
        from product_analysis_mv cmv
        where 1=1
        {% if filters.start %}
            and order_shipped_at >= {{filters.start}}
        {% endif %}
        {% if filters.stop %}
            and order_shipped_at <= {{filters.stop}}
        {% endif %}

        {% if where_clause and where_clause.non_return %}
            {{where_clause.non_return | sqlsafe}}
        {% endif %}
        {% if not is_return_associated_cohort and cohort_filter_query %}
            and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
        {% endif %}
        group by date_ov
    )
{% endif %}
{% if computed_fields_aur %}
,trend_aur_values as (
        select order_shipped_date AS date_
                {{computed_fields_aur | sqlsafe}}
                from (select distinct vendor_product_id, item_price,
                            {{date_query_order_shipped_at | sqlsafe}} as order_shipped_date
                    from product_analysis_mv
                    where 1=1
                {% if filters.start %}
                    and order_shipped_at >= {{filters.start}}
                {% endif %}
                {% if filters.stop %}
                    and order_shipped_at <= {{filters.stop}}
                {% endif %}
                {% if where_clause and where_clause.non_return%}
                    {{where_clause.non_return | sqlsafe}}
                {% endif %}
                {% if not is_return_associated_cohort and cohort_filter_query %}
                    and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                {% endif %}
                group by order_shipped_date, vendor_product_id, item_price
                ) as sub
            group by date_
        )
  {% endif %}
   select
        {% if computed_fields_pr %}
            COALESCE(date_ov, date_rv, date_prv) as date
        {% else %}
            COALESCE(date_ov, date_rv) as date
        {% endif %}
            {{computed_fields_select | sqlsafe}}
            from main_return_associated_values
            join main_order_associated_values on date_rv = date_ov
            {% if computed_fields_aur %}
                join trend_aur_values on trend_aur_values.date_ = coalesce(date_ov, date_rv)
            {% endif %}
            {% if computed_fields_pr %}
                full join main_only_returns_associated_values on main_only_returns_associated_values.date_prv = coalesce(date_ov, date_rv)
            {% endif %}
            order by date;
    """

net_kpi_fetch = """
    with placeHolder AS (
        SELECT NULL
    )
{% if computed_fields_rv or computed_fields_pr %}
    ,main_return_associated_values AS (
        select {{date_query_items_returned_at | sqlsafe}} as date_rv
            {{computed_fields_rv | sqlsafe}}
            {{computed_fields_pr | sqlsafe}}
        from product_analysis_mv
    where 1=1
    AND items_returned_at is not NULL
    {% if filters.start %}
        and items_returned_at >= {{filters.start}}
    {% endif %}
    {% if filters.stop %}
        and items_returned_at <= {{filters.stop}}
    {% endif %}

    {% if where_clause and where_clause.order %}
        {{where_clause.order | sqlsafe}}
    {% endif %}
    {% if cohort_filter_query %}
        and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
    {% endif %}
    group by date_rv )
{% endif %}
{% if computed_fields_ov %}
    ,main_order_associated_values AS (
    select {{date_query_order_shipped_at | sqlsafe}} as date_ov
            {{computed_fields_ov | sqlsafe}}
    from product_analysis_mv cmv
    where 1=1
    and order_shipped_at is not null
    {% if filters.start %}
        and order_shipped_at >= {{filters.start}}
    {% endif %}
    {% if filters.stop %}
        and order_shipped_at <= {{filters.stop}}
    {% endif %}

    {% if where_clause and where_clause.non_return %}
        {{where_clause.non_return | sqlsafe}}
    {% endif %}
    {% if not is_return_associated_cohort and cohort_filter_query %}
        and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
    {% endif %}
    group by date_ov
)
{% endif %}
{% if computed_fields_orv %}
,main_order_or_return_associated_values AS (
    SELECT  {% if filters.start and filters.stop %}
                CASE WHEN order_shipped_at BETWEEN {{filters.start}} AND {{filters.stop}} THEN {{date_query_order_shipped_at | sqlsafe}}
                 ELSE {{date_query_items_returned_at | sqlsafe}}  END AS date_orv
            {% else %}
                {{date_query_order_shipped_at | sqlsafe}} as date_orv
            {% endif %}
            {{computed_fields_orv | sqlsafe}}
    from product_analysis_mv
    where 1=1
    and date_orv is not null
    {% if filters.start and filters.stop %}
        and ((order_shipped_at >= {{filters.start}}
        and order_shipped_at <= {{filters.stop}})
        or  (items_returned_at >= {{filters.start}}
        and items_returned_at <= {{filters.stop}}))
    {% endif %}
    {% if where_clause and where_clause.order %}
        {{where_clause.order | sqlsafe}}
    {% endif %}
    {% if cohort_filter_query %}
        and {{cohort_name | sqlsafe}} in ( {{cohort_filter_query | sqlsafe}} )
    {% endif %}
    group by date_orv
     )
{% endif %}
{% if computed_fields_aur %}
,trend_aur_values as (
                select date_
                       {{computed_fields_aur | sqlsafe}}
                    from (select distinct vendor_product_id, item_price,
                            {% if filters.start and filters.stop %}
                               CASE WHEN order_shipped_at BETWEEN {{filters.start}} AND {{filters.stop}} THEN {{date_query_order_shipped_at | sqlsafe}}
                                ELSE {{date_query_items_returned_at | sqlsafe}} END AS date_
                            {% else %}
                               {{date_query_order_shipped_at | sqlsafe}} as date_
                            {% endif %}
                        from product_analysis_mv
                        where 1=1
                        and date_ is not null
                    {% if filters.start and filters.stop %}
                        and ((order_shipped_at between {{filters.start}} and {{filters.stop}}) or
                        (items_returned_at between {{filters.start}} and {{filters.stop}}))
                    {% endif %}
                    {% if where_clause and where_clause.non_return%}
                        {{where_clause.non_return | sqlsafe}}
                    {% endif %}
                    {% if not is_return_associated_cohort and cohort_filter_query %}
                        and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                    {% endif %}
                    group by date_, vendor_product_id, item_price
                    ) as sub
                group by date_
            )
{% endif %}
select {% if computed_fields_aur and computed_fields_orv %}
        COALESCE(date_rv, date_ov, date_orv, date_) AS date
       {% elif computed_fields_orv %}
        COALESCE(date_rv, date_ov, date_orv) AS date
       {% elif computed_fields_aur %}
        COALESCE(date_rv, date_ov, date_) AS date
       {% else %}
        COALESCE(date_rv, date_ov) AS date
       {% endif %}
       {{computed_fields_select | sqlsafe}}
from main_order_associated_values
        full outer join
    main_return_associated_values
    on date_rv = date_ov
    {% if computed_fields_orv %}
     full join main_order_or_return_associated_values
     on main_order_or_return_associated_values.date_orv = coalesce(date_ov, date_rv)
    {% endif %}
    {% if computed_fields_aur %}
     full join trend_aur_values
     on trend_aur_values.date_ = coalesce(date_ov, date_rv)
    {% endif %}
ORDER BY date;
    """
