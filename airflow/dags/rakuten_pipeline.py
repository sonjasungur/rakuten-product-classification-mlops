from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_DIR = "/opt/airflow"

with DAG(
    dag_id="rakuten_mlops_pipeline",
    description="Rakuten MLOps demo pipeline: train model and generate drift report.",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rakuten", "mlops", "mlflow", "monitoring"],
) as dag:

    train_model = BashOperator(
        task_id="train_model_with_mlflow",
        bash_command=f"cd {PROJECT_DIR} && python3 src/models/train.py",
    )

    generate_drift_report = BashOperator(
        task_id="generate_drift_report",
        bash_command=f"cd {PROJECT_DIR} && python3 src/monitoring/drift_report.py",
    )

    train_model >> generate_drift_report
