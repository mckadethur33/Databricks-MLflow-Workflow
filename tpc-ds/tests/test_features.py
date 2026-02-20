from src.features import build_customer_features

def test_feature_columns_exist(spark):
    # Minimal mock data
    store_sales = spark.createDataFrame([], "ss_customer_sk int, ss_net_paid double, ss_sold_date_sk int")
    web_sales = spark.createDataFrame([], "ws_bill_customer_sk int, ws_net_paid double, ws_sold_date_sk int")
    customer = spark.createDataFrame([], "c_customer_sk int")
    date_dim = spark.createDataFrame([], "d_date_sk int, d_date date")

    df = build_customer_features(store_sales, web_sales, customer, date_dim)

    expected_cols = [
        "total_store_sales",
        "total_web_sales",
        "avg_store_basket",
        "avg_web_basket",
        "days_since_last_purchase"
    ]

    for col in expected_cols:
        assert col in df.columns
