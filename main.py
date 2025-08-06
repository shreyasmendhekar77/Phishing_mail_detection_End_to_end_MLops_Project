#  Training pipeline with all the components
from Phising_mail_detection.pipeline.data_ingestion_pipeline import Data_ingestion_pipeline
from Phising_mail_detection.pipeline.data_preprocessing_pipeline import Data_preprocessing_pipeline
from Phising_mail_detection.pipeline.model_training_pipeline import model_training_pipeline

class model_retrain_pipeline():
    def __init__(self):
        pass


    def complete_pipeline(self):
        
        try:
            Ingestion=Data_ingestion_pipeline()
            Ingestion.main()
        except Exception as e:
            raise e


        try:
            Preporcessing=Data_preprocessing_pipeline()
            Preporcessing.main()
        except Exception as e:
            raise e


        try:
            Training=model_training_pipeline()
            Training.main()
        except Exception as e:
            raise e


if __name__=='__main__':
    try:
        retrain_pipeline=model_retrain_pipeline()
        retrain_pipeline.complete_pipeline()
    except Exception as e:
        raise e