from src.ElectricityBill.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH, SCHEMA_FILE_PATH
from src.ElectricityBill.utils.commons import read_yaml, create_directories, get_size 
from src.ElectricityBill.entity.configuration_entity import DataIngestionConfig

# create a configurations manager class to manage the configurations 
class ConfigurationManager: 
    def __init__(
            self, 
            config_filepath = CONFIG_FILE_PATH,  
            params_filepath = PARAMS_FILE_PATH, 
            schema_filepath = SCHEMA_FILE_PATH
    ): 
        
        # Initialize the onfguration manager 
        # Read YAML configurations files to  intialize configuration parameters 
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(SCHEMA_FILE_PATH)

        # create necessary directories specified in the configuration 
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        # Get the data ingestion configuration 
        config = self.config.data_ingestion 
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir = config.root_dir, 
            source_URL = config.source_URL, 
            local_data_file = config.local_data_file, 
            unzip_dir = config.unzip_dir
        )

        return data_ingestion_config 
    