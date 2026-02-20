import mlflow
import mlflow.pyfunc
from pyspark.sql import DataFrame

def load_production_model(model_name: str):
    return mlflow.pyfunc.load_model(f"models:/{model_name}/Production")

def score(model, df: DataFrame):
    pandas_df = df.toPandas()
    preds = model.predict(pandas_df)
    pandas_df["prediction"] = preds
    return pandas_df
