# ⚡ Electricity Bill Predictor – MLOps Pipeline

## 📌 Overview

This project implements an end-to-end MLOps pipeline for predicting monthly electricity bills. The pipeline is modular, config-driven, and built to simulate production-ready workflows.

## The project covers:

**1 .Data Ingestion** – Download/unzip raw datasets, save artifacts

**2. Data Validation** – Schema checks, column validation, logging

**3. Data Transformation** – Preprocessing with pipelines (scaling, encoding)

**4. Model Training** – ML models (Decision Tree, XGBoost) with evaluation

**5. Prediction Pipeline** – Load trained model & make predictions

**6. Logging & Exception Handling** – Centralized error handling with FileOperatorError

## 🛠 Tech Stack

**Language**: Python 3.11 (Conda environment)

**Libraries**: pandas, numpy, scikit-learn, xgboost, joblib, PyYAML, python-box

**MLOps Practices**: modular pipeline, config-driven YAMLs, artifacts tracking, logging

**Environment Management**: Miniconda