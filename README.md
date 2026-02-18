# Databricks-MLflow-Workflow
Databricks MLflow Workflow
A collection of end‑to‑end machine learning workflows built on Databricks, showcasing modern data engineering, feature engineering, model training, experiment tracking, and orchestration using Delta Lake, MLflow, and Databricks Workflows.

This repository serves as a portfolio of production‑minded ML projects designed to demonstrate:

Scalable data pipelines using Databricks & PySpark

Medallion architecture (Bronze → Silver → Gold)

MLflow experiment tracking & model registry

Reproducible ML workflows

Deployment‑ready batch and streaming pipelines

📁 Repository Structure
Code
Databricks-MLflow-Workflow/
│
├── projects/
│   ├── tpc-ds-order-value-prediction/
│   └── (future projects)
│
├── notebooks/
│   └── (shared utilities or global notebooks)
│
├── workflows/
│   └── (Databricks workflow JSON exports)
│
└── README.md
Each project lives in its own folder under /projects, allowing this repo to grow into a full ML portfolio.

🚀 Current Projects
1. TPCH Order Value Prediction
Goal: Build an end‑to‑end ML pipeline that predicts the next order value for a customer using the TPCH sample dataset.

This project demonstrates:

Delta Lake medallion architecture

Feature engineering on relational data

MLflow experiment tracking

Model registry integration

Batch scoring pipeline

👉 Project folder:  
/projects/tpch-order-value-prediction/

🧭 Roadmap
This repository will expand over time with additional Databricks‑native ML projects, such as:

Retail demand forecasting (Bakehouse dataset)

Real‑time anomaly detection with Structured Streaming

Feature Store–powered ML pipelines

Model serving and monitoring workflows

🛠️ Technologies Used
Databricks (SQL, PySpark, Workflows, Unity Catalog)

Delta Lake

MLflow (tracking, registry, model management)

Python

PySpark ML / sklearn / XGBoost

Databricks AutoML (optional)