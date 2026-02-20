import mlflow
from pyspark.sql import DataFrame
from pyspark.sql import functions as F

def add_ingest_timestamp(df: DataFrame) -> DataFrame:
    return df.withColumn("ingest_timestamp", F.current_timestamp())

def log_params(params: dict):
    for k, v in params.items():
        mlflow.log_param(k, v)

def log_metrics(metrics: dict):
    for k, v in metrics.items():
        mlflow.log_metric(k, v)
