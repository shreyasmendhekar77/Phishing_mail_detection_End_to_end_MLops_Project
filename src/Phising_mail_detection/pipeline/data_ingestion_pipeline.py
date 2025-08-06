
from Phising_mail_detection.entity.config_entity import ConfigurationManager
from Phising_mail_detection.components.data_ingestion import DataIngestion
from Phising_mail_detection import logger

STAGE_NAME='DATA INGESTION'

class Data_ingestion_pipeline():
    def __init__(self):
        pass

    def main(self):
        config= ConfigurationManager()
        config_path_data= config.get_data_ingestion_config()
        data_ingestion_main=DataIngestion(config=config_path_data)
        data_ingestion_main.download_file()
        data_ingestion_main.extract_zip_file()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = Data_ingestion_pipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
