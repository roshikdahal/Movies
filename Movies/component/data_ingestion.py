"""
Created on Monday feb 13 2023
@author: kumar.dahal
This class is created to  read the folder structure of our files from  DataIngestionConfig 
 and  create necessary folder require for DataIngestion
"""

from Movies.entity import DataIngestionConfig
from Movies.entity import DataIngestionArtifact
from Movies.logger import logging
import os
import time
from six.moves import urllib
import tarfile
import pandas as pd
import numpy as np


class DataIngestion:
    
    def __init__(self,dataingestionconfig:DataIngestionConfig):
        try:
            logging.info("Data ingestion started")
            self.data_ingestion_config = dataingestionconfig
        except Exception as e:
            return e

    def download_Movies_data(self,) -> str:
        """
        this function get the url create the folder and store the downloaded data 
        in the folder which will be our zip folder.
        """
        try:
            data_url  =self.data_ingestion_config.dataset_download_url
            tgz_download_dir = self.data_ingestion_config.tgz_download_dir
            os.makedirs(tgz_download_dir,exist_ok=True)

            #create the folder name based on url base name
            movie_file = os.path.basename(tgz_download_dir)
            #now append the movie filename in download_dir
            total_file_path = os.path.join(tgz_download_dir,movie_file)
            logging.info("Downloading file")
            start_time=time.time()
            urllib.request.urlretrieve(data_url, total_file_path)
            stop_time = time.time()
            logging.info("Time taken {} to downlad file:{}".format(stop_time-start_time,total_file_path))
            return total_file_path

        except Exception as e:
            return e

    #since we have downloaded data and store it in total_file_path which is of extension tgz we need to unzip it and store in raw data
    def extract_zip_file(self,total_file_path:str):
        try:
            raw_folder = self.data_ingestion_config.raw_data_dir
            #create the folder is exists is True also
            os.makedirs(raw_folder,exist_ok=True)   
            logging.info("Extracting tgz file:{}".format(total_file_path)) 
            with tarfile.open(total_file_path) as movies_file_object:
                movies_file_object.extractall(path=raw_folder)
            logging.info("Extracting tgz file:{} completed".format(raw_folder))     
        except Exception as e:
            return e


    def train_test_split(self) -> DataIngestionArtifact:
        """
        spliting data into train test and appending it on data ingestion artifact_entity
        """
        try:
            raw_data = self.data_ingestion_config.raw_data_dir
            #pick the first folder and get the data from first file 
            main_folder= os.listdir(raw_data)[0]
            #now merge folder to get propoer file path
            movies_file_path = os.path.join(raw_data,main_folder)
            logging.info("Reading the movies csv file [{movies_file_path}]")
            #read the csv file
            movies_df =  pd.read_csv(movies_file_path)
            #remaining to perform data split using stratified sampling
        except Exception as e:
            return e        

    def initialize_data_ingestion(self,) -> DataIngestionArtifact:
        try:
            tgz_file = self.download_Movies_data()
            self.extract_zip_file(total_file_path = tgz_file)
            return self.train_test_split
        except Exception as e:
            return e 

