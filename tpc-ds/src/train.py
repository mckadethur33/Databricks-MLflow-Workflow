import mlflow
import mlflow.spark
from pyspark.sql import DataFrame
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import RandomForestRegressor
from pyspark.ml.evaluation import RegressionEvaluator

def train_model(df: DataFrame, label_col: str = "total_store_sales"):
    mlflow.set_experiment("/Shared/tpcds_ml_project")

    feature_cols = [
        "total_store_sales",
        "total_web_sales",
        "avg_store_basket",
        "avg_web_basket",
        "days_since_last_purchase"
    ]

    assembler = VectorAssembler(
        inputCols=feature_cols,
        outputCol="features"
    )

    data = assembler.transform(df).select("features", label_col)

    train, test = data.randomSplit([0.8, 0.2], seed=42)

    with mlflow.start_run():
        model = RandomForestRegressor(
            featuresCol="features",
            labelCol=label_col,
            numTrees=100,
            maxDepth=10
        )

        fitted = model.fit(train)
        preds = fitted.transform(test)

        evaluator = RegressionEvaluator(
            labelCol=label_col,
            predictionCol="prediction",
            metricName="rmse"
        )

        rmse = evaluator.evaluate(preds)
        mlflow.log_metric("rmse", rmse)

        mlflow.spark.log_model(fitted, "model")

        run_id = mlflow.active_run().info.run_id
        return fitted, run_id
