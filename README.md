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

## ⚙️ Setup Instructions

### 1️⃣ Create Conda Environment

```bash 
cd "C:\Users\KIIT\Desktop\Data - Science\Electricity-Bill-Predictor"

# Create and activate environment
conda create -n elec_bill python=3.11 -y
conda activate elec_bill

```

### 2️⃣ Install Dependencies

```bash 
pip install -r requirements.txt

```

(or manually)

```bash 
pip install pandas numpy scikit-learn xgboost joblib pyyaml python-box notebook

```

### 3️⃣ Run Individual Pipelines

```bash 
# Data ingestion
python -m src.components.data_ingestion

# Data transformation
python -m src.components.data_transformation

# Full orchestrator
python main.py

```

### 4️⃣ Run Jupyter Notebook 

``` bash 
pip install notebook
python -m notebook

```

## 📊 Dataset

**Source**: Electricity consumption dataset (CSV/ZIP)

**Columns**:

    - Numerical: Fan, Refrigerator, AirConditioner, Television, Monitor, MotorPump, Month, MonthlyHours, TariffRate

    - Categorical: City, Company

    - Target: ElectricityBill

## 🏗 Pipeline Flow

**1. Data Ingestion** → downloads & stores dataset into artifacts/data_ingestion

**2. Data Validation** → checks schema, validates columns, writes status in artifacts/data_validation/status.txt

**3. Data Transformation** → applies preprocessing (scaling & encoding), saves preprocessor object (preprocessor.joblib)

**4. Model Training** → trains ML models, stores trained model in artifacts/model_trainer/model.joblib

**5. Prediction Pipeline** → loads saved model & predicts electricity bill

## 📈 Model Evaluation Metrics

1. The pipeline evaluates models using:

2. Mean Absolute Error (MAE)

3. Mean Squared Error (MSE)

4. Root Mean Squared Error (RMSE)

5. Mean Absolute Percentage Error (MAPE)

6. R² Score

## 🚀 Quick Start Examples

**🔹 Train the Model**

```bash 
from joblib import load
from src.ElectricityBill.components.c_04_model_trainer import ModelTrainer
from src.ElectricityBill.config.configuration import ConfigurationManager

# Load configuration
config = ConfigurationManager().get_model_trainer_config()

# Initialize trainer
trainer = ModelTrainer(config)

# Train and save model
metrics = trainer.train()
print("Training Metrics:", metrics)

```

**🔹 Make Predictions**

``` bash 
import pandas as pd
import joblib

# Load preprocessor and model
preprocessor = joblib.load("artifacts/data_transformation/preprocessor.joblib")
model = joblib.load("artifacts/model_trainer/model.joblib")

# Sample input data
sample = pd.DataFrame([{
    "Fan": 5,
    "Refrigerator": 2,
    "AirConditioner": 1,
    "Television": 2,
    "Monitor": 1,
    "MotorPump": 0,
    "Month": 8,
    "City": "Mumbai",
    "Company": "Tata Power Company Ltd.",
    "MonthlyHours": 350,
    "TariffRate": 8.5
}])

# Transform input
X_sample = preprocessor.transform(sample)

# Predict bill
prediction = model.predict(X_sample)
print("Predicted Electricity Bill:", prediction[0])

```
## 🚀 Future Improvements

1. **Implement CI/CD Pipelines**
   - Automate build, testing, and deployment workflows using **GitHub Actions**.

2. **Containerization & Deployment**
   - Deploy the application using **FastAPI/Flask** with **Docker** for scalable and portable deployments.

3. **Experiment Tracking & Model Versioning**
   - Integrate **MLflow** or **DVC (Data Version Control)** for experiment tracking, model versioning, and reproducible machine learning workflows.

4. **Advanced MLOps Automation**
   - Extend the project into a fully automated **MLOps pipeline** by integrating **IoT-enabled OCR-Driven Energy Invoice Automation**, including automated data ingestion, OCR processing, model retraining, deployment, and monitoring.

   > **Related Repository:**  
   > **IoT & OCR-Driven Energy Invoice Automation**  
   > GitHub: <https://github.com/pranjalsinha1965/webhook-implementation>
