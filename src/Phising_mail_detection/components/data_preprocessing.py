from Phising_mail_detection import logger
import re
import os
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from Phising_mail_detection.utils.common import load_model,save_model
import pandas as pd
from gensim.models import Word2Vec
from pathlib import Path
from Phising_mail_detection.entity.config_entity import Data_preprocessing_config
ps=PorterStemmer()

class Data_preprocessing_Validation:
    def __init__(self, config: Data_preprocessing_config):
        self.config = config
    

    def clean(self,data):
        data = re.sub(r'[^a-zA-Z\s]', '', data)
        data = data.lower()
        stop_words = set(stopwords.words('english'))
        words = data.split()
        words = [word for word in words if word not in stop_words]
        words = [ps.stem(word) for word in words]
        return words  # returns a list of tokens
    
    # Function to get average vector for an email
    def get_email_vector(self,tokens, model):
        vectors = [model.wv[word] for word in tokens if word in model.wv]
        if vectors:
            return np.mean(vectors, axis=0)
        else:
            return np.zeros(model.vector_size)

    def clean_and_Vector_embed(self):
        data=pd.read_csv(self.config.unzip_data_dir)
        data['Email Text'].fillna('',inplace=True)
        # print(data.isna().sum())
        # print("First row",data['Email Text'][0])
        # sample=data['Email Text'][0]
        # out=self.clean(sample)
        # Apply the clean function on the email text feature 
        # if os.path.exists(self.config.cleaned_data):
        #     logger.info(f"Cleaned data already exists at {self.config.cleaned_data}")
        #     data = pd.read_csv(self.config.cleaned_data)
        # else:
        #     logger.info("Cleaned data file not exists")
        data['Email Type'].replace({'Safe Email':0,'Phishing Email':1},inplace=True)
        data['tokens'] = data['Email Text'].apply(self.clean)
        # data.to_csv(self.config.cleaned_data, index=False)
        print(data['tokens'].iloc[0])  # Show the first cleaned email text
        # apply the word2vec for embedding purpose
        # check the word_to_vec model exists other wise train the word2vec model and use it
       

        if os.path.exists(self.config.vector_embed_model):
            logger.info(f"Vector embedding model exists at {self.config.vector_embed_model}")
            model=load_model(Path(self.config.vector_embed_model))

        else:
            logger.info("Model not exists - training the word2vec model on the email dataset")
            w2v_model = Word2Vec(sentences=data['tokens'], vector_size=100, window=5, min_count=1, workers=4)
            save_model(w2v_model,self.config.vector_embed_model)
            model=load_model(Path(self.config.vector_embed_model))
        
        print(data['tokens'][0])
        example=data['tokens'][0]
        vec=self.get_email_vector(example,model)
        print("Vector is ",vec)

        # Apply the vectorization to each email
        data['Email_vector'] = data['tokens'].apply(lambda x: self.get_email_vector(x, model))
        data.to_csv(self.config.vectorized_data)
        # Show the first email's vector
        print(data['Email_vector'].iloc[0])
        


    
