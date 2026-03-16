# Rakuten Product Classification - MLOps Project

## Project Overview

This project builds an end-to-end machine learning pipeline to classify Rakuten e-commerce products.

The model predicts product categories based on:

- product title (item_name)
- product description (item_caption)
- product images

The focus of the project is not only the model, but the full MLOps pipeline architecture.

## Dataset

Rakuten Institute of Technology e-commerce product classification dataset.

The dataset contains:
- product titles
- product descriptions
- product images
- product category labels

## Project Structure

rakuten-product-classification-mlops
│
├── data/
│   ├── raw/            # original dataset
│   └── processed/      # cleaned / transformed data
│
├── notebooks/          # exploration and experiments
│
├── src/
│   ├── data/           # data loading
│   ├── features/       # feature engineering
│   ├── models/         # training and prediction
│   ├── api/            # inference API
│   └── utils/          # helper functions
│
├── tests/              # unit tests
├── outputs/            # predictions / artifacts
│
├── requirements.txt
├── README.md
├── .gitignore
└── main.py

## Setup

Create virtual environment

python3 -m venv .venv
source .venv/bin/activate

Install dependencies

pip install -r requirements.txt

## First Goal

Build a simple baseline model using text features (TF-IDF + Logistic Regression) before integrating images and deploying the inference API.

## Technologies

Python  
scikit-learn  
FastAPI  
Docker (later)  
MLflow (later)  
DVC (later)  
Airflow (later)

