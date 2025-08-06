from Phising_mail_detection import logger 
from Phising_mail_detection.entity.config_entity import ConfigurationManager
from Phising_mail_detection.components.model_training import Model_training_function

Stagename="Model Training..."

class model_training_pipeline():
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_training_config()
        model= Model_training_function(config=model_training_config)
        model.model_training()


if __name__=="__main__":
    try:
        logger.info("<<<<<< Started the {Stagename} Started >>>>>>>>>")
        train_model_obj=model_training_pipeline()
        train_model_obj.main()
        logger.info("<<<<<< Completed with {Stagename}")

    except Exception as e:
        logger.info(e)
        raise e

    


