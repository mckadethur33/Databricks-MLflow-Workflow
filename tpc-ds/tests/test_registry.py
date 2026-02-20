from src.registry import (
    get_latest_run_id,
    register_model_version
)

def test_get_latest_run_id(spark):
    # This test checks that the function returns a string
    # (We assume at least one run exists in the experiment)
    experiment_path = "/Shared/tpcds_ml_experiment"
    run_id = get_latest_run_id(experiment_path)
    assert isinstance(run_id, str)

def test_register_model_version(spark):
    # This test ensures the function returns an integer version
    # (We assume a valid run exists)
    experiment_path = "/Shared/tpcds_ml_experiment"
    run_id = get_latest_run_id(experiment_path)
    model_uri = f"runs:/{run_id}/model"

    version = register_model_version(
        model_uri=model_uri,
        model_name="tpcds_customer_spend_model"
    )

    assert isinstance(version, int)
    assert version > 0