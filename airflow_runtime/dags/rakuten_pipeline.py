from datetime import datetime

from airflow import DAG
from airflow.operators.bash import BashOperator

PROJECT_DIR = "/opt/airflow"

with DAG(
    dag_id="rakuten_mlops_pipeline",
    description="Rakuten MLOps pipeline with MLflow experiment comparison and promotion.",
    start_date=datetime(2025, 1, 1),
    schedule_interval=None,
    catchup=False,
    tags=["rakuten", "mlops", "mlflow", "monitoring", "promotion"],
) as dag:

    run_baseline = BashOperator(
        task_id="run_baseline_text_model",
        bash_command="cd /opt/airflow && \
        RAKUTEN_RUN_NAME=baseline_text_only \
        RAKUTEN_MAX_ROWS=150 \
        RAKUTEN_MAX_FEATURES=200 \
        RAKUTEN_ALPHA=0.01 \
        RAKUTEN_USE_IMAGE_FEATURES=false \
        python3 src/models/train.py",
    )

    run_image_text = BashOperator(
        task_id="run_image_text_model",
        bash_command="cd /opt/airflow && \
        RAKUTEN_RUN_NAME=image_text_baseline \
        RAKUTEN_MAX_ROWS=500 \
        RAKUTEN_MAX_FEATURES=1000 \
        RAKUTEN_ALPHA=0.001 \
        RAKUTEN_USE_IMAGE_FEATURES=true \
        python3 src/models/train.py",
    )

    run_candidate = BashOperator(
        task_id="run_production_candidate",
        bash_command="cd /opt/airflow && \
        RAKUTEN_RUN_NAME=production_candidate \
        RAKUTEN_MAX_ROWS=1000 \
        RAKUTEN_MAX_FEATURES=5000 \
        RAKUTEN_ALPHA=0.0001 \
        RAKUTEN_USE_IMAGE_FEATURES=true \
        python3 src/models/train.py",
    )

    compare_and_promote = BashOperator(
        task_id="compare_and_promote_model",
        bash_command="cd /opt/airflow && RAKUTEN_PROMOTE_ONLY=true python3 src/models/train.py",
    )

    generate_drift_report = BashOperator(
        task_id="generate_drift_report",
        bash_command=f"cd {PROJECT_DIR} && python3 src/monitoring/drift_report.py",
    )

    [run_baseline, run_image_text, run_candidate] >> compare_and_promote >> generate_drift_report