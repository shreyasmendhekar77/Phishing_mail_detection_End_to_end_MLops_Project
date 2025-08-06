from Phising_mail_detection.utils.common import create_directories,read_yaml
from Phising_mail_detection.constants import *
from Phising_mail_detection.config.configuration import DataIngestionConfig, Data_preprocessing_config,ModelTrainingConfig


# this configuration manager will have the constructor such that - 
# it will get the config file path, params and schema file paths for 

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


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    
    def get_data_preprocessing_config(self) -> Data_preprocessing_config:
        config = self.config.data_preprocessing
        # schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = Data_preprocessing_config(
            root_dir=config.root_dir,
            unzip_data_dir = config.unzip_data_dir,
            vector_embed_model= config.vector_embed_model,
            cleaned_data = config.cleaned_data,
            vectorized_data = config.vectorized_data
            
        )

        return data_validation_config

    def get_model_training_config(self) -> ModelTrainingConfig:
        config = self.config.Model_training
        # params=self.params.model_params
        # schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        Model_train_config = ModelTrainingConfig(
            root_dir = config.root_dir,
            training_data_path= config.training_data_path,
            trained_model_dir= config.trained_model_dir,
            # model_name = params.model_name,
            # model_params = params.model_params
        )

        return Model_train_config
