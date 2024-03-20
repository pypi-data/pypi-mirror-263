import copy

_computed_fields = [
    # return associated
    {'name': 'revenue_sold_', 'expression': ',COALESCE(Sum(revenue_sold), 0)'},
    {'name': 'revenue_sold_orv',
        'expression': ',COALESCE(Sum(revenue_sold), 0)'},
    {'name': 'return_revenue',
        'expression': ',COALESCE(Sum(revenue_lost), 0)'},
    {'name': 'return_revenue_',
        'expression': ',COALESCE(Sum(revenue_lost_zeroed_out), 0)'},
    {'name': 'profit_loss', 'expression': ',COALESCE(Sum(profit_lost), 0)'},
    {'name': 'distinct_order_count',
        'expression': ',COALESCE(Count(distinct order_id), 0)'},
    {'name': 'bracketing_order_count',
        'expression': 'COUNT(DISTINCT (CASE WHEN bracketing = \'Bracketed\' THEN order_id END))'},
    {'name': 'exchange_order_count',
        'expression': ',sum(case when exchange_type is not null then 1 else 0 end)'},
    {'name': 'items_returned',
        'expression': ",COALESCE(Sum(items_returned), 0)"},
    {'name': 'return_cost', 'expression': ',COALESCE(Sum(cost), 0)'},
    {
        'name': 'unsellable_items_returned',
        'expression': ''',COALESCE(SUM(CASE WHEN LOWER(disposition) IN (SELECT LOWER(setting_value) FROM models.settings WHERE setting_name = 'disposition_code') THEN items_returned ELSE NULL END), 0)'''
    },
    {
        'name': 'unique_items_returned',
        'expression': ',count( DISTINCT CASE WHEN items_returned > 0  THEN vendor_product_id END)'
    },
    # order associated
    {'name': 'sum_ship_time_delta',
        'expression': ',COALESCE(Sum(ship_time_delta), 0)'},
    {'name': 'sum_item_price', 'expression': ',COALESCE(Sum(item_price), 0)'},
    {'name': 'order_count', 'expression': ',COALESCE(count(*), 0)'},
    {
        'name': 'repeat_customers',
        'expression': ',Count(distinct case when IS_SUBSEQUENT_ORDER = 1 then customer_account_number else NULL end)'
    },
    {'name': 'total_purchased_customers_',
        'expression': ',Count(DISTINCT customer_account_number)'},
    {'name': 'total_baseline_revenue_lost',
        'expression': ',COALESCE(Sum(baseline_revenue_lost), 0)'},
    {'name': 'items_sold', 'expression': ",COALESCE(Sum(items_sold), 0)"},
    {'name': 'avg_style_repurchase_time',
     'expression': ",avg(case when IFNULL(style_repurchase_time_delta, 0) > 0 then style_repurchase_time_delta::double precision end)"
     },
    {'name': 'avg_time_to_repurchase',
     'expression': ",avg(case when IFNULL(customer_repurchase_time_delta, 0) > 0 then customer_repurchase_time_delta::double precision end)"
     },
    # both
    {'name': 'total_unique_customers',
        'expression': ',Count(DISTINCT customer_account_number)'},
    # returning customer count
    {
        'name': 'return_customer_count',
        'expression': ''',COUNT(DISTINCT CASE WHEN COALESCE(items_returned, 0) > 0 then customer_account_number end)''',
    },
    {
        'name': 'total_returning_customers',
        'expression': ',COALESCE(return_customer_count, 0)',
        'depends_on': ['return_customer_count']
    },
    # post return repurchase
    {
        'name': 'is_returner',
        'expression': ''',COUNT(DISTINCT CASE
                              WHEN IS_SUBSEQUENT_ORDER_AFTER_RETURN_EXISTS = 1
                                  THEN CUSTOMER_ACCOUNT_NUMBER END)'''
    },
    # calculate total customer for post return repurchase rate.
    # !NOTE: cannot use total_purchased_customers_ since
    # 1) it is associated with order_associated_values which creates order_associated CTE
    # 2) the description is selected if order_associated CTE is generated
    # 3) but order_associated CTE does not join with post_return CTE
    {'name': 'pr_customer_sum',
        'expression': ',Count(DISTINCT customer_account_number)'},
    {
        'name': 'pr_repurchase_rate',
        'expression': ',CASE WHEN pr_customer_sum !=0 THEN is_returner / pr_customer_sum * 100 ELSE 0 END',
        'depends_on': ['is_returner', 'pr_customer_sum']
    },

    # usually on final select statement
    {'name': 'total_items_sold', 'expression': ',coalesce(items_sold, 0)', 'depends_on': [
        'items_sold']},
    {'name': 'average_order_value', 'expression': ',coalesce(avg_order_value, 0)', 'depends_on': [
        'avg_order_value']},

    {'name': 'total_return_cost',
        'expression': ',coalesce(return_cost, 0)', 'depends_on': ['return_cost']},
    {'name': 'total_revenue_sold', 'expression': ',coalesce(revenue_sold_, 0)', 'depends_on': [
        'revenue_sold_']},
    {'name': 'total_return_revenue',
        'expression': ',coalesce(return_revenue, 0)', 'depends_on': ['return_revenue']},
    {'name': 'total_profit_loss',
        'expression': ',coalesce(profit_loss, 0)', 'depends_on': ['profit_loss']},
    {'name': 'post_return_repurchase_rate', 'expression': ',coalesce(pr_repurchase_rate,0)',
     'depends_on': ['pr_repurchase_rate']},
    {'name': 'total_items_returned',
        'expression': ',coalesce(items_returned, 0)', 'depends_on': ['items_returned']},
    {'name': 'total_unique_items_returned', 'expression': ',coalesce(unique_items_returned, 0)',
     'depends_on': ['unique_items_returned']},
    {'name': 'overall_revenue_sold',
        'expression': ',sum(revenue_sold_) over()', 'depends_on': ['revenue_sold_']},
    {'name': 'overall_return_revenue',
        'expression': ',sum(return_revenue) over()', 'depends_on': ['return_revenue']},
    {
        'name': 'items_returned_vs_items_sold',
        'expression': '''
            ,CASE
                   WHEN total_items_sold = 0 AND total_items_returned != 0 then 100
                   WHEN total_items_sold = 0 THEN 0
                   ELSE 100 * (total_items_returned::DOUBLE PRECISION / total_items_sold)
            END
            ''',
        'depends_on': ['total_items_sold', 'total_items_returned']
    },
    {
        'name': 'return_revenue_vs_revenue_sold',
        'expression': '''
            ,CASE
                   WHEN total_revenue_sold = 0 AND total_return_revenue != 0 then 100
                   WHEN total_revenue_sold = 0 THEN 0
                   ELSE 100 * (total_return_revenue::DOUBLE PRECISION / total_revenue_sold)
            END
            ''',
        'depends_on': ['total_revenue_sold', 'total_return_revenue']
    },
    {
        'name': 'overall_avg_return_revenue_vs_revenue_sold',
        'expression': '''
            ,CASE
                   WHEN overall_revenue_sold = 0 AND overall_return_revenue != 0 then 100
                   WHEN overall_revenue_sold = 0 THEN 0
                   ELSE 100 * (overall_return_revenue::DOUBLE PRECISION / overall_revenue_sold)
            END
            ''',
        'depends_on': ['overall_revenue_sold', 'overall_return_revenue']
    },
    {
        'name': 'repeat_customers_count',
        'expression': ',COALESCE(repeat_customers, 0)',
        'depends_on': ['repeat_customers']
    },
    {
        'name': 'unique_customers',
        'expression': ',COALESCE(total_unique_customers, 0)',
        'depends_on': ['total_unique_customers']
    },
    {
        'name': 'total_purchased_customers',
        'expression': ',COALESCE(total_purchased_customers_, 0)',
        'depends_on': ['total_purchased_customers_']
    },
    {
        'name': 'total_unsellable_items_returned',
        'expression': ',COALESCE(unsellable_items_returned, 0)',
        'depends_on': ['unsellable_items_returned']
    },
    {
        'name': 'unsellable_percent',
        'expression': ',CASE WHEN total_items_returned = 0 THEN 0 ELSE 100 * total_unsellable_items_returned/total_items_returned::double precision END',
        'depends_on': ['total_unsellable_items_returned', 'total_items_returned']
    },
    {
        'name': 'rank',
        'expression': '',
        'depends_on': ['total_items_returned', 'total_items_sold', 'total_revenue_sold', 'total_return_revenue',
                       'items_returned_vs_items_sold', 'return_revenue_vs_revenue_sold', 'total_profit_loss'],
    },
    {
        'name': 'best_performer',
        'expression': '',
        'depends_on': ['total_items_returned', 'total_items_sold', 'total_revenue_sold', 'total_return_revenue',
                       'items_returned_vs_items_sold', 'return_revenue_vs_revenue_sold', 'total_profit_loss'],
    },
    {
        'name': 'r_rate',
        'expression': ''',COUNT(DISTINCT CASE
                                        WHEN IS_SUBSEQUENT_ORDER = 1
                                            THEN CUSTOMER_ACCOUNT_NUMBER
                        END)                                AS is_repurchase,
                        is_repurchase / COUNT(DISTINCT customer_account_number) * 100'''

    },
    {
        'name': 'repurchase_rate',
        'expression': ',COALESCE(r_rate, 0)',
        'depends_on': ['r_rate']

    },
    {
        'name': 'avg_order_value',
        'expression': ''',CASE
                            WHEN distinct_order_count != 0 THEN
                                coalesce(Sum(revenue_sold), 0) / distinct_order_count
                            ELSE 0 END''',
        'depends_on': ['distinct_order_count']

    },
    {
        'name': 't_customers',
        'expression': ''',COUNT(DISTINCT customer_account_number)'''
    },
    {
        'name': 'total_customers',
        'expression': ',COALESCE(t_customers, 0)',
        'depends_on': ['t_customers']
    },
    {
        'name': 'total_revenue_sold_orv',
        'expression': ',COALESCE(revenue_sold_orv, 0)',
        'depends_on': ['revenue_sold_orv']
    },
    {
        'name': 'total_distinct_order_count',
        'expression': ',COALESCE(distinct_order_count, 0)',
        'depends_on': ['distinct_order_count']
    },
    {
        'name': 'average_unit_selling_price',
        'expression': ', COALESCE(average_item_price, 0)',
        'depends_on': ['average_item_price']
    },
    {
        'name': 'average_item_price',
        'expression': ', avg(item_price)'
    },
    {
        'name': 't_item_price',
        'expression': ''', SUM(item_price)'''
    },
    {
        'name': 't_item_count',
        'expression': ''', COUNT(item_price)'''
    },
    {
        'name': 'total_item_price',
        'expression': ''', COALESCE(t_item_price, 0)''',
        'depends_on': ['t_item_price']
    },
    {
        'name': 'total_item_count',
        'expression': ''', COALESCE(t_item_count, 0)''',
        'depends_on': ['t_item_count']
    },
    {
        'name': 'style_repurchase_time',
        'expression': ''', avg_style_repurchase_time''',
        'depends_on': ['avg_style_repurchase_time']
    },
    {'name': 'time_to_repurchase', 'expression': ',avg_time_to_repurchase',
        'depends_on': ['avg_time_to_repurchase']},
    {
        'name': 'style_repurchase_rate',
        'expression': ''', CASE WHEN total_purchased_customers_ !=0 THEN is_style_repurchase / total_purchased_customers_ * 100 ELSE 0 END''',
        'depends_on': ['total_purchased_customers_', 'is_style_repurchase']
    },
    {
        'name': 'is_style_repurchase',
        'expression': ',COUNT(DISTINCT CASE WHEN has_subsequent_style_order = 1 THEN CUSTOMER_ACCOUNT_NUMBER END)'
    },
    {
        'name': 'recoverable_revenue',
        'expression': ''', CASE WHEN return_revenue_ - total_baseline_revenue_lost < 0 THEN 0 ELSE
        return_revenue_ - total_baseline_revenue_lost END''',
        'depends_on': ['return_revenue_', 'total_baseline_revenue_lost']
    },
    {
        'name': 'avg_rating',
        'expression': ''', avg(case when star_rating = 'None' then null else star_rating::float end)''',
    },
    {
        'name': 'star_rating',
        'expression': ', COALESCE(avg_rating, 0)',
        'depends_on': ['avg_rating']
    },
    {
        'name': 'net_revenue',
        'expression': ''', total_revenue_sold - total_return_revenue''',
        'depends_on': ['total_revenue_sold', 'total_return_revenue']
    },
    {'name': 'exchanged_revenue_', 'expression': ',COALESCE(Sum(exchanged_revenue), 0)'},
    {'name': 'total_exchanged_revenue', 'expression': ',COALESCE(exchanged_revenue_, 0)',
     'depends_on': ['exchanged_revenue_']},
    {
        'name': 'net_lost_revenue',
        'expression': ''', total_return_revenue - total_exchanged_revenue''',
        'depends_on': ['total_return_revenue', 'total_exchanged_revenue']
    },
    # Mayzon specific KPI
    {
        'name': 'dmg_percentage',
        'expression': ''', CASE WHEN sum(revenue_sold) = 0 and sum(damaged_revenue) <> 0 THEN 100
                    WHEN  sum(damaged_revenue) = 0 THEN 0
                    ELSE sum(damaged_revenue)/sum(revenue_sold) * 100 END''',
    },
    {
        'name': 'damaged_percentage',
        'expression': ', COALESCE(dmg_percentage, 0)',
        'depends_on': ['dmg_percentage']
    },


]


def get_computed_fields():
    return copy.deepcopy(_computed_fields)
