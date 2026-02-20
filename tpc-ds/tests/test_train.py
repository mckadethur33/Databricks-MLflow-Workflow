from src.train import train_model

def test_train_model_runs(spark):
    df = spark.createDataFrame(
        [(10.0, 5.0, 20.0, 10.0, 30)],
        "total_store_sales double, total_web_sales double, avg_store_basket double, avg_web_basket double, days_since_last_purchase int"
    )

    model, run_id = train_model(df)
    assert model is not None
    assert isinstance(run_id, str)
