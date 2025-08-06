from Phising_mail_detection.entity.config_entity import ConfigurationManager
from Phising_mail_detection.components.data_preprocessing import Data_preprocessing_Validation
from Phising_mail_detection import logger

STAGE_NAME="DATA PREPROCESSING AND CLEANING"

class Data_preprocessing_pipeline():
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        config_path_data= config.get_data_preprocessing_config()
        Data_preprocessing_main=Data_preprocessing_Validation(config=config_path_data)
        Data_preprocessing_main.clean_and_Vector_embed()



if __name__== '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} Started <<<<<<\n\nx==========x")        
        obj=Data_preprocessing_pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")        
        
    
    except Exception as e:
        raise e