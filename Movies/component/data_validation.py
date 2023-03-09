"""
Created on Monday feb 19 2023
@author: kumar.dahal
This class is created to validate the data.
"""
from Movies.config.configurations import DataValidationConfig
from Movies.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from Movies.logger import logging

import pandas as pd

from evidently.model_profile import Profile
from evidently.model_profile.sections import DataDriftProfileSection
from evidently.dashboard import Dashboard
from evidently.dashboard.tabs import DataDriftTab  #for data dashboard
from Movies.utils.read_yaml import read_yaml_file
from Movies.constants import *
import json
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
            self.schema_config = read_yaml_file(filepath=SCHEMA_FILE_DIR)
        except Exception as e:
            return e

    def is_train_test_file_exists(self)-> bool:
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

            if not is_exists:
                #our output data_ingestion_artifact has the data so
                train_file_path = self.data_ingestion_artifact.train_file_path
                test_file_path = self.data_ingestion_artifact.test_file_path
                messages = f"Training_file {train_file_path} or Testing file :{test_file_path} is not present "
                raise Exception(messages)
        
            
            return is_exists

          except Exception as e:
            return e   
          
    def get_train_test_df(self):
        """
        this function is return to obtain the train and test dataset for checking the data drift 
        """
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            return e
        
    def validate_schema_columns_dataset(self)-> bool:
        '''
        this method will fetch the necessary requirement from #schema_validation.yaml 
        to check the file contained is satisfied.
        '''    

        try:
            # is_validated = False
            # columns = self.schema_config[COLUMNS]
            # columns_numbers = self.schema_config['NumberofColumns']
            # target_column = self.schema_config['target_column']
            # domain_range = self.schema_config['domain_value']
            # train_df,test_df = self.get_train_test_df()
            # df = train_df
            # for keys,values in target_column.items():
            #     if df.shape[1]==columns_numbers :
            #         pass
            #     else:
            #         logging.info(f, "Invalid Column Length for the file %s" % train_df)
            # logging.info('column length is validated')
               
                
                
                                   
            # """perform validation here"""
            # return is_validated
            pass
        except Exception as e:
            return e
        
    def get_save_data_drift_report(self):
        """
        create the profile object for data drift from Evidently
        It ask for profile section which check data drift which need profile of our data
        since it is comparision of 2 dataset train and test so we need  dataset 
        """
        try:
            profile = Profile(sections=[DataDriftProfileSection()])

            train_df,test_df = self.get_train_test_df()
            profile.calculate(train_df,test_df)  #calculate method accept train and test df to generate data drift report
            #now data drift is available in the form of string  format by profile.json() and using json.loads to convert
            report= json.loads(profile.json())

            with open(self.data_validation_config.data_report_file_name,'w') as report_file_name:
                json.dump(report,report_file_name,indent=6) #indent=6 is for formatting

            return report    
       
        except Exception as e:
            return e

    def save_data_drift_report_page(self):
        try:
            """DatadriftTab is required in list format to get the data dashborad"""
            dashboard =  Dashboard(tabs=[DataDriftTab()])
            train_df,test_df = self.get_train_test_df()
            dashboard.calculate(train_df,test_df)

            report_page_file_name = self.data_validation_config.data_report_file_name
            report_page_dir = os.path.dirname(report_page_file_name)
            #make directory if not exist
            os.makedirs(report_page_dir,exist_ok=True)
            #save in the location
            dashboard.save(report_page_file_name)
           
        except Exception as e:
            return e 

    def is_data_drift_found(self)-> bool:
        try:
            report = self.get_save_data_drift_report()
            self.save_data_drift_report_page()
            
            return True
        except Exception as e:
            return e    

    def initiate_data_validation(self)->DataValidationArtifact:
        """
        In this functioin  schema validation is done.

        """  
        try:
            self.is_train_test_file_exists()
            self.validate_schema_columns_dataset()
            self.is_data_drift_found()
            
            data_validation_artifact = DataValidationArtifact(
                schema_file_path=self.data_validation_config.scehma_file_path,
                report_file_path=self.data_validation_config.data_report_file_name,
                report_page_file_path=self.data_validation_config.report_page_name,
                is_validated=True,
                message="Data Validation performed successully."
            )
            logging.info(f"Data validation artifact: {data_validation_artifact}")
            return data_validation_artifact
            
        except Exception as e:
            return e

    def __del__(self):
        logging.info(f"ata Valdaition log completed. \n\n")
              