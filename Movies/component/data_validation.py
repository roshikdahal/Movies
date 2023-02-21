"""
Created on Monday feb 19 2023
@author: kumar.dahal
This class is created to validate the data.
"""
from Movies.config.configurations import DataValidationConfig
from Movies.entity.artifact_entity import DataIngestionArtifact
from Movies.logger import logging

import os
class DataValidation:
    """
    parameters:
    data_validation_config of data type DataValidationconfig,
    data_ingestion_artifact (which is our output)
    """
    def __init__(self,data_validation_config:DataValidationConfig,
            data_ingestion_artifact:DataIngestionArtifact):
        try:
            self.data_validation_config = data_validation_config
            self.data_ingestion_artifact = data_ingestion_artifact
        except Exception as e:
            return e

    def is_train_test_file_exists(self):
          """
          this function ensure the presence of train and test data then only we perform 
           initiate_data_validation 
           first we decleare our file present to False since 
           it is boolean we can return the file to true if file exist
          """

          try:
            is_train_file_exist = False  
            is_test_file_exist = False
            #our output data_ingestion_artifact has the data so
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path
            
            #os.path.exists return boolean value of path exists or not
            is_train_file_exist = os.path.exists(train_file_path) 
            is_test_file_exist = os.path.exists(test_file_path)
            
            # and operator to make it sure only returns True is both are true otherwise False
            is_exists =  is_train_file_exist and is_test_file_exist
            #writing logger  
            logging.info("Train and test file {}".format(is_exists))
            return is_exists

          except Exception as e:
            return e   



    def initiate_data_validation(self):
        """
        In this functioin  schema validation is done.

        """  
        try:
            is_exists = self.is_train_test_file_exists()
            if not is_exists:
                #our output data_ingestion_artifact has the data so
                train_file_path = self.data_ingestion_artifact.train_file_path
                test_file_path = self.data_ingestion_artifact.test_file_path
                messages = f"Training_file {train_file_path} or Testing file :{test_file_path} is not present "
            logging.info(messages)
        except Exception as e:
            return e      