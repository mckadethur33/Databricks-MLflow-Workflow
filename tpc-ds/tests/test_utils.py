from src.utils import add_ingest_timestamp

def test_add_ingest_timestamp(spark):
    df = spark.createDataFrame([(1,)], ["id"])
    result = add_ingest_timestamp(df)
    assert "ingest_timestamp" in result.columns
