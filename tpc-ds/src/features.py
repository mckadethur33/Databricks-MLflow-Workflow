from pyspark.sql import DataFrame
from pyspark.sql import functions as F
from pyspark.sql.window import Window

def build_customer_features(store_sales: DataFrame,
                            web_sales: DataFrame,
                            customer: DataFrame,
                            date_dim: DataFrame) -> DataFrame:
    # Aggregate store sales
    store_agg = (
        store_sales.groupBy("ss_customer_sk")
        .agg(
            F.sum("ss_net_paid").alias("total_store_sales"),
            F.avg("ss_net_paid").alias("avg_store_basket"),
            F.max("ss_sold_date_sk").alias("last_store_purchase_date_sk")
        )
    )

    # Aggregate web sales
    web_agg = (
        web_sales.groupBy("ws_bill_customer_sk")
        .agg(
            F.sum("ws_net_paid").alias("total_web_sales"),
            F.avg("ws_net_paid").alias("avg_web_basket"),
            F.max("ws_sold_date_sk").alias("last_web_purchase_date_sk")
        )
    )

    # Join store + web + customer
    df = (
        customer
        .join(store_agg, customer.c_customer_sk == store_agg.ss_customer_sk, "left")
        .join(web_agg, customer.c_customer_sk == web_agg.ws_bill_customer_sk, "left")
    )

    # Convert date_sk to actual date
    df = (
        df
        .join(date_dim.select("d_date_sk", "d_date"), 
              df.last_store_purchase_date_sk == date_dim.d_date_sk, "left")
        .withColumnRenamed("d_date", "last_store_purchase_date")
        .drop("d_date_sk")
    )

    df = (
        df
        .join(date_dim.select("d_date_sk", "d_date"), 
              df.last_web_purchase_date_sk == date_dim.d_date_sk, "left")
        .withColumnRenamed("d_date", "last_web_purchase_date")
        .drop("d_date_sk")
    )

    # Recency feature
    df = df.withColumn(
        "days_since_last_purchase",
        F.datediff(F.current_date(), 
                   F.greatest("last_store_purchase_date", "last_web_purchase_date"))
    )

    return df
