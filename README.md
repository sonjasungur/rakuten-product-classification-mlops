# Rakuten Product Classification — MLOps Pipeline

Production-oriented MLOps pipeline for e-commerce product classification using machine learning, experiment tracking, orchestration and deployment workflows.

🌐 Website: https://mscisystems.com

---

# Project Overview

This project demonstrates an end-to-end MLOps workflow for classifying Rakuten e-commerce products using:

* product title (`item_name`)
* product description (`item_caption`)
* product images

The project focuses not only on model development, but on building a scalable machine learning system including:

* experiment tracking
* orchestration
* model registry workflows
* API deployment
* monitoring
* reproducible pipelines

---

# MLOps Stack

* MLflow (Experiment Tracking & Model Registry)
* Airflow (Pipeline Orchestration)
* FastAPI (Inference API)
* Docker (Containerization)
* Grafana (Monitoring)
* Evidently (Data Drift Monitoring)
* AWS / S3-based workflows

---

# Dataset

Rakuten Institute of Technology e-commerce product classification dataset.

The dataset contains:

* product titles
* product descriptions
* product images
* category labels

---

# Project Structure

```text
rakuten-product-classification-mlops/

├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│
├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── api/
│   ├── monitoring/
│   └── utils/
│
├── tests/
├── outputs/
├── docker/
├── airflow/
├── mlruns/
│
├── requirements.txt
├── docker-compose.yml
├── README.md
└── main.py
```

---

# Key Features

* End-to-end MLOps workflow
* Experiment tracking with MLflow
* Model Registry workflows
* Airflow orchestration
* API deployment
* Monitoring & observability
* Drift detection workflows
* Reproducible ML pipelines

---

# Technologies

Python • MLflow • Airflow • FastAPI • Docker • Grafana • Evidently • scikit-learn • AWS • Machine Learning • MLOps

# Author

Sonja Sungur
AI Systems Engineering • MLOps • Operational AI

🌐 https://mscisystems.com

