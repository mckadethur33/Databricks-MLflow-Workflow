import mlflow

from mlflow.tracking import MlflowClient

 

client = MlflowClient()

 

def get_latest_run_id(experiment_path: str) -> str:

    experiment = mlflow.get_experiment_by_name(experiment_path)

    if experiment is None:

        raise ValueError(f"Experiment not found: {experiment_path}")

 

    runs = mlflow.search_runs(

        experiment_ids=[experiment.experiment_id],

        order_by=["start_time DESC"],

        max_results=1

    )

 

    if runs.empty:

        raise ValueError("No MLflow runs found in experiment.")

 

    return runs.iloc[0].run_id

 

 

def register_model_version(model_uri: str, model_name: str) -> int:

    registered = mlflow.register_model(

        model_uri=model_uri,

        name=model_name

    )

    return int(registered.version)

 

 

def assign_model_alias(model_name: str, version: int, alias: str):

    client.set_registered_model_alias(

        name=model_name,

        alias=alias,

        version=version

    )