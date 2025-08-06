from Phising_mail_detection import logger
import numpy as np
from Phising_mail_detection.utils.common import load_model,save_model
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix,classification_report
from lightgbm import LGBMClassifier
from Phising_mail_detection.config.configuration import ModelTrainingConfig


class Model_training_function:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config
    
    def convert_string_to_array(self,vector_string):
        
      """Convert string representation of vector to numpy array"""
      try:
        # Remove brackets and split by whitespace
            vector_string = vector_string.strip('[]')
        # Convert to numpy array
            return np.fromstring(vector_string, sep=' ')
      except Exception as e:
            return e
      

    def data_preparation(self):
        logger.info("Loading training data")
        training_data = pd.read_csv(self.config.training_data_path)
        training_data['Email_vector'] = training_data['Email_vector'].apply(self.convert_string_to_array)
        logger.info("Splitting data into features and target")
        X = training_data['Email_vector']
        y = training_data['Email Type'].values
        logger.info("Splitting data into train and test sets")
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        X_train = np.vstack(X_train)
        X_test= np.vstack(X_test)
        print(X_train.shape)
        return X_train, X_test, y_train, y_test
        
        
    def model_training(self):
        logger.info("Training the model")
        
        X_train, X_test, y_train, y_test = self.data_preparation()
                # model = LGBMClassifier()
        # model = LGBMClassifier(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
        logger.info("Model training started")
        model=RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)
        logger.info("Model evaluation on training data")
        y_train_pred = model.predict(X_train)
        train_accuracy = accuracy_score(y_train, y_train_pred)
        train_classification_rep = classification_report(y_train, y_train_pred)
        print(f"Training Accuracy: {train_accuracy}")
        print("Training Classification Report:")
        print(train_classification_rep)
        logger.info("Evaluating the model")
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        classification_rep = classification_report(y_test, y_pred)
        print(f"Accuracy: {accuracy}")
        print("Classification Report:")
        print(classification_rep)
        print("Confusion Matrix:")
        print(confusion_matrix(y_test, y_pred))
        logger.info("Saving the trained model")
        save_model(model, self.config.trained_model_dir)
        logger.info(f"Model saved to the file location {self.config.trained_model_dir}  ")
