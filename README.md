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

## 📂 Project Structure

``` bash 
Electricity-Bill-Predictor/
│
├── src/
│   ├── ElectricityBill/
│   │   ├── components/        # Core pipeline components
│   │   ├── config/            # Configuration & schema
│   │   ├── pipelines/         # Pipeline scripts (ingestion, validation, etc.)
│   │   ├── utils/             # Utility functions (yaml, directories, size)
│   │   ├── exception.py       # Custom exception handler
│   │   ├── logger.py          # Centralized logger
│   │
│   └── artifacts/             # Generated artifacts (data, models, preprocessor, logs)
│
├── research/                  # Experimentation scripts
│   ├── part_01_data_ingestion.py
│   ├── part_02_data_validation.py
│   ├── part_03_data_transformation.py
│   ├── part_04_model_trainer.py
│
├── config/
│   ├── config.yaml            # Pipeline configs
│   ├── params.yaml            # Model hyperparameters
│   ├── schema.yaml            # Data schema
│
├── main.py                    # Orchestrator
├── requirements.txt           # Dependencies
└── README.md                  # Project documentation

```