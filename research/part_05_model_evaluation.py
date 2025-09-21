from pathlib import Path 
from dataclasses import dataclass

@dataclass()
class ModelEvaluationConfig:
   root_dir: Path 
   test_data_path: Path 
   test_target_variable: Path 
   model_path: Path 
   all_params: dict
   metric_file_name: Path 
   target_column: str 

from src.ElectricityBill.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.ElectricityBill.utils.commons import read_yaml, create_directories, save_json

class ConfigurationManager: 
   def __init__(
           self, 

        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


  