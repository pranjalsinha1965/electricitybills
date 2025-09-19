from dataclasses import dataclass 
from pathlib import Path 

# Entity
@dataclass 
class ModelTrainerConfig: 
    root_dir: Path
    train_data_path: Path 
    test_data_path: Path 
    model_name: str 
    # DecisiontreeRegressor Parameter 
    