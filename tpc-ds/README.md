TPC‑DS ML Pipeline on Databricks
End‑to‑End Machine Learning Project with PySpark, MLflow, and Databricks Workflows
This project demonstrates a complete machine learning workflow on Databricks, using the TPC‑DS SF1000 dataset as the foundation for large‑scale feature engineering and model development. It highlights modern ML engineering practices including:

Distributed data processing with PySpark

Feature engineering on Delta Lake

Experiment tracking with MLflow

Model lifecycle management with the Databricks Model Registry

Orchestration using Databricks Workflows

Optional: Databricks Feature Store + Model Serving

This repository is designed as a portfolio‑ready example of how to build production‑grade ML pipelines on Databricks.

📁 Project Structure
Code
project/
│
├── notebooks/
│   ├── 01_ingest_data.py
│   ├── 02_feature_engineering.py
│   ├── 03_train_model.py
│   ├── 04_register_and_deploy.py
│
├── src/
│   ├── __init__.py
│   ├── features.py
│   ├── utils.py
|
├── tests/
|   ├── __init__.py
|   ├── test_utils.py
│
├── conf/
│   ├── config.yaml
│
├── requirements.txt
└── README.md
📦 Dataset: TPC‑DS SF1000
The TPC‑DS dataset is a well‑known industry benchmark for decision support systems. Databricks provides a pre‑generated scale factor 1000 dataset (tpcds_sf1000) containing billions of rows across dozens of tables.

This project uses a subset of tables relevant to customer purchasing behavior, such as:

store_sales

customer

item

date_dim

These tables are ideal for demonstrating large‑scale feature engineering with Spark.

🎯 Project Goal
Predict customer spending behavior using historical store sales and customer attributes.

Example target variable:

Total spend per customer over a defined time window
or

Probability a customer exceeds a spend threshold

This is flexible — the goal is to demonstrate the ML engineering workflow, not optimize a specific benchmark.

🧱 Architecture Overview
Code
                ┌──────────────────────────┐
                │   TPC‑DS SF1000 Dataset   │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Ingest & Bronze Tables  │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │  Feature Engineering      │
                │  (PySpark → Delta Lake)   │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │     Model Training        │
                │   (MLflow Experiments)    │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │   Model Registry (Prod)   │
                └─────────────┬────────────┘
                              │
                              ▼
                ┌──────────────────────────┐
                │ Batch Scoring / Serving   │
                └──────────────────────────┘
🧪 1. Data Ingestion
Notebook: 01_ingest_data.py

Reads TPC‑DS tables from Databricks datasets

Writes them as Delta tables in the workspace

Ensures schema consistency and partitioning

Example:

python
df = spark.read.table("tpcds_sf1000_delta.store_sales")
df.write.format("delta").mode("overwrite").saveAsTable("ml_tpcds.store_sales_bronze")
🔧 2. Feature Engineering (PySpark)
Notebook: 02_feature_engineering.py

Key transformations include:

Joining customer, item, and sales tables

Aggregating spend metrics

Creating temporal features (day of week, seasonality)

Handling missing values

Writing feature tables to Delta

Example:

python
features = (
    sales.join(customers, "customer_id")
         .groupBy("customer_id")
         .agg(
             sum("sales_price").alias("total_spend"),
             count("*").alias("num_transactions"),
             avg("quantity").alias("avg_quantity")
         )
)
features.write.format("delta").mode("overwrite").saveAsTable("ml_tpcds.features")
🤖 3. Model Training with MLflow
Notebook: 03_train_model.py

This notebook demonstrates:

Converting Spark features to Pandas or using Spark MLlib

Logging parameters, metrics, and artifacts

Tracking multiple experiments

Example:

python
with mlflow.start_run():
    model = RandomForestRegressor(n_estimators=200)
    model.fit(X_train, y_train)

    mlflow.log_param("n_estimators", 200)
    mlflow.log_metric("rmse", rmse)
    mlflow.sklearn.log_model(model, "model")
📚 4. Model Registry Integration
Notebook: 04_register_and_deploy.py

Registers the best model in the MLflow Model Registry

Transitions it to Staging or Production

Optionally enables Databricks Model Serving

Example:

python
registered = mlflow.register_model(
    model_uri=f"runs:/{run_id}/model",
    name="tpcds_customer_spend_model"
)
⚙️ 5. Workflow Orchestration
A Databricks Workflow (Job) orchestrates the pipeline:

Ingest Data

Feature Engineering

Train Model

Register Model

Batch Scoring (optional)

This demonstrates production‑grade automation.

🚀 Optional Enhancements
Feature Store
Register features for reuse across models.

Model Serving
Deploy the model as a REST endpoint.

Unity Catalog Integration
Store models, tables, and features with governance.

📊 Results & Artifacts
The project produces:

MLflow experiment runs

Registered models with versioning

Delta feature tables

Workflow DAG screenshots

Model performance metrics

These artifacts are ideal for showcasing ML engineering skills.

📝 How to Run
Clone this repo into Databricks Repos

Attach a cluster with:

Runtime: DBR 13+ ML recommended

Autoscaling enabled

Run notebooks in order:

01_ingest_data.py

02_feature_engineering.py

03_train_model.py

04_register_and_deploy.py

(Optional) Create a Databricks Workflow to automate the pipeline

📌 Summary
This project demonstrates a full ML lifecycle on Databricks using a large‑scale dataset (TPC‑DS SF1000). It highlights:

Distributed feature engineering

MLflow experiment tracking

Model registry best practices

Workflow orchestration

Production‑ready ML engineering patterns

It is designed to serve as a strong portfolio piece for transitioning into Machine Learning roles.