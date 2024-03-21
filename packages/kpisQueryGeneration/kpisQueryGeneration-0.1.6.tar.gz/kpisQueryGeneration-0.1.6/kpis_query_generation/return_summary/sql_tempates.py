kpi_fetch_template = """
    with return_associated_kpis as (
        select 1
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
            and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
        {% endif %}
    ),
    order_associated_kpis as (
            select 1
            {{computed_fields_ov | sqlsafe}}
        from product_analysis_mv
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
            and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
        {% endif %}
    ),
    post_returners as (select 1
               {% if computed_fields_pr %}
                      {{computed_fields_pr | sqlsafe}}
                    FROM product_analysis_mv
                    WHERE 1=1
                         {% if filters.start %}
                            AND ITEMS_RETURNED_AT >= {{filters.start}}
                        {% endif %}
                        {% if filters.stop %}
                            AND ITEMS_RETURNED_AT <= {{filters.stop}}
                        {% endif %}
                        {% if where_clause and where_clause.order %}
                            {{where_clause.order | sqlsafe}}
                        {% endif %}
                        {% if cohort_filter_query %}
                            and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                        {% endif %}
                {% endif %}),
    summary_aur_values as (
                select 1
                {% if computed_fields_aur %}
                       {{computed_fields_aur | sqlsafe}}
                    from (select distinct vendor_product_id, item_price
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
                    {% if not is_return_associated_cohort and  cohort_filter_query %}
                        and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                    {% endif %}
                    group by vendor_product_id, item_price) as sub
                {% endif %})
   select   1
            {{computed_fields_select | sqlsafe}}
            from return_associated_kpis rak,
            order_associated_kpis oak,
            post_returners pr,
            summary_aur_values
    """

raw_kpi_fetch_template = """
            WITH get_unique_customers AS (
                    SELECT 1
               {% if computed_fields_orv %}
                    {{computed_fields_orv | sqlsafe}}
                 from product_analysis_mv
                 where 1=1
                    {% if filters.start and filters.stop %}
                        and ((order_shipped_at >= {{filters.start}}
                        and order_shipped_at <= {{filters.stop}}) or
                        (items_returned_at >= {{filters.start}}
                        and items_returned_at <= {{filters.stop}}))
                    {% endif %}
                    {% if where_clause and where_clause.order %}
                            {{where_clause.order | sqlsafe}}
                    {% endif %}
                    {% if cohort_filter_query %}
                        and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                    {% endif %}
               {% endif %}

            ),
            get_returns_data AS (
                SELECT 1
                       {{computed_fields_rv | sqlsafe}}
                FROM product_analysis_mv
                where 1=1
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
                    and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                {% endif %}
            ),
                 get_revenue_data AS (
                     SELECT 1
                            {{computed_fields_ov | sqlsafe}}
                     FROM product_analysis_mv
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
                    {% if not is_return_associated_cohort and  cohort_filter_query %}
                        and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                    {% endif %}
                 ),
                post_returners as (select 1
                {% if computed_fields_pr %}
                    {{computed_fields_pr | sqlsafe}}
                    FROM product_analysis_mv
                    WHERE 1=1
                         {% if filters.start %}
                            AND ITEMS_RETURNED_AT >= {{filters.start}}
                        {% endif %}
                        {% if filters.stop %}
                            AND ITEMS_RETURNED_AT <= {{filters.stop}}
                        {% endif %}
                        {% if where_clause and where_clause.order %}
                            {{where_clause.order | sqlsafe}}
                        {% endif %}
                        {% if cohort_filter_query %}
                            and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                        {% endif %}
                {% endif %}),
                summary_aur_values as (
                        select 1
                        {% if computed_fields_aur %}
                               {{computed_fields_aur | sqlsafe}}
                            from (select distinct vendor_product_id, item_price
                                from product_analysis_mv
                                where 1=1
                            {% if filters.start and filters.stop %}
                                and ((order_shipped_at >= {{filters.start}}
                                and order_shipped_at <= {{filters.stop}}) or
                                (items_returned_at >= {{filters.start}}
                                and items_returned_at <= {{filters.stop}}))
                            {% endif %}
                            {% if where_clause and where_clause.non_return%}
                                {{where_clause.non_return | sqlsafe}}
                            {% endif %}
                            {% if not is_return_associated_cohort and  cohort_filter_query %}
                                and coalesce({{cohort_name | sqlsafe}}, 'None') in ( {{cohort_filter_query | sqlsafe}} )
                            {% endif %}
                            group by vendor_product_id, item_price) as sub
                        {% endif %})

            SELECT 1
                   {{computed_fields_select | sqlsafe}}
            FROM get_revenue_data,
                 get_returns_data,
                 get_unique_customers,
                 post_returners,
                 summary_aur_values
    """
