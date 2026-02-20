from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def build_customer_features(store_sales: DataFrame, customer: DataFrame, date_dim: DataFrame) -> DataFrame:
    # Store sales aggregation
    store_agg = (
        store_sales.groupBy("ss_customer_sk")
        .agg(
            F.count("*").alias("num_transactions"),
            F.sum("ss_quantity").alias("total_quantity"),
            F.sum("ss_sales_price").alias("total_spend"),
            F.avg("ss_sales_price").alias("avg_sales_price"),
            F.avg("ss_ext_discount_amt").alias("avg_discount"),
            F.countDistinct("i_category").alias("num_categories_bought"),
            F.max("d_date").alias("last_purchase_date")
        )
    )

    # Join store + customer
    df = (
        customer
        .join(store_agg, customer.c_customer_sk == store_agg.ss_customer_sk, "left")
    )

    # Feature: days since last purchase
    df = df.withColumn(
        "days_since_last_purchase",
        F.datediff(F.current_date(), F.col("last_purchase_date"))
    )

    return df