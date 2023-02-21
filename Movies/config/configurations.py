"""
Created on Monday feb 13 2023
@author: kumar.dahal
This class is created to get the values from yaml file and  return the entity of each type
"""
from Movies.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, \
    ModelTrainingConfig, ModelEvaluationConfig,ModelPushConfig,TrainigPipelineConfig

from Movies.constants import *
from Movies.utils import read_yaml_file
from Movies.logger import logging
class Configurations:
    """
    Location of config.yaml , time stamp to keep the record that
    when the file was read and also the function to read_yaml is initialized.
    """
    def __init__(self,config_file_path:str = CONFIG_FILE_DIR,current_time_stamp:str = get_current_time_stamp()) -> None:
        #initialize the read_yaml function to read yaml file
        self.config_info = read_yaml_file(filepath = config_file_path)

        self.training_pepeline_config = self.get_training_pepeline_config()
        
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        this functioins will return the folder structure of url of data downlaod dir,train adnd test dir which is our pipeline artifact.
        """
        try:
            
            data_ingestion_config = self.config_info[DATA_INGESTION_CONFIG_KEY]
            url_data = data_ingestion_config[DATA_INGESTION_DOWNLOAD_URL_KEY]
            data_artifact = self.training_pepeline_config.artifact_file_dir
            data_ingestion_artifact_dir = os.path.join(data_artifact,DATA_INGESTION_ARTIFACT_DIR,self.time_stamp)

            raw_data_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[RAW_DATA_DIR_KEY])

            tgz_downloaad_dir = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[TGZ_DOWNLOAD_DIR_KEY])

                       
    
            train_data = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[INGESTED_DIR_KEY],data_ingestion_config[INGESTED_TRAIN_DIR_KEY])
            test_data = os.path.join(data_ingestion_artifact_dir,data_ingestion_config[INGESTED_DIR_KEY],data_ingestion_config[INGESTED_TEST_DIR_KEY])


            data_ingestion_config = DataIngestionConfig(
                dataset_download_url = url_data,
                tgz_download_dir= tgz_downloaad_dir,
                raw_data_dir = raw_data_dir,
                ingested_train_dir =train_data,
                ingested_test_dir = test_data
                )
            logging.info(f"Data ingestion config:{data_ingestion_config}")    
            return data_ingestion_config

            
        except Exception as e:
            return e    

    def get_data_validation_config(self) -> DataValidationConfig:
        try:

            data_artifact = self.training_pepeline_config.artifact_file_dir  #top level artifact folder {Movies}

            data_validation_config = self.config_info[DATA_VALIDATION_CONFIG_KEY]
            
            data_schema_dir = os.path.join(
                data_artifact,
                data_validation_config[SCHEMA_FILE_DIR_KEY],
                self.time_stamp)
            schema_file_path = os.path.join(data_schema_dir,data_validation_config[SCHEMA_FILE_NAME_KEY]) 
            #in this path we are going to store the validation output  
            data_report_file = os.path.join(data_schema_dir,data_validation_config[REPORT_FILE_NAME]) 
            data_report_page = os.path.join(data_schema_dir,data_validation_config[REPORT_PAGE_FILE]) 
            
            data_validation_config = DataValidationConfig(scehma_file_path=schema_file_path,
                                                          data_report_file_name=data_report_file,
                                                          report_page_name=data_report_page)
            
            return data_validation_config
            
        except  Exception as e:
            return e
    def get_data_transformation_config(self)->DataTransformationConfig:
        try:
            data_artifact = self.training_pepeline_config.artifact_file_dir
            data_transformation_config = self.config_info[DATA_TRANSFORMATION_CONFIG_KEY]
            transformed_dir = os.path.join(data_artifact,data_transformation_config[TRANSFORMED_DIR_KEY],self.time_stamp)

            transformed_train_dir = os.path.join(transformed_dir,data_transformation_config[TRANSFORMED_TRAIN_DIR_KEY])

            transformed_test_dir = os.path.join(transformed_dir,data_transformation_config[TRANSFORMED_TEST_DIR_KEY])
            
            preprocessed_dir = os.path.join(data_artifact,data_transformation_config[PREPROCESSED_DIR_KEY],self.time_stamp)
            preprocessed_file = os.path.join(preprocessed_dir,data_transformation_config[PREPROCESSED_OBJECT_FILE_NAME_KEY])

            data_transformation_config = DataTransformationConfig(
                tranfored_train_dir=transformed_train_dir,
                transormed_test_dir=transformed_test_dir,
                preprocessed_file_path=preprocessed_file
                )
            return data_transformation_config  

        except Exception as e:
            return e  

    def get_model_training_config(self) -> ModelTrainingConfig:
        try:
            data_artifact = self.training_pepeline_config.artifact_file_dir
            data_training_model = self.config_info[MODEL_TRAINING_CONFIG_KEY]

            train_dir = os.path.join(
                data_artifact,
                data_training_model[TRAINED_MODEL_DIR_KEY],
                self.time_stamp
                )
            trained_model_file = os.path.join(
                train_dir,
                data_training_model[MODEL_FILE_NAME_KEY]
                )
            base_accuracy = data_training_model[MODEL_BASE_ACCURACY_KEY]    
               
            data_training_model = ModelTrainingConfig(
                trained_model_filepath=trained_model_file,
                base_accuracy_model=base_accuracy
                )
            return data_training_model    
            
        except Exception as e:
            return e


    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        try:
            data_artifact = self.training_pepeline_config.artifact_file_dir
            model_evaluation_config = self.config_info[MODEL_EVALUATION_CONFIG_KEY]
            model_path = os.path.join(data_artifact,model_evaluation_config[MODEL_FILE_DIR_KEY])
            model_name = os.path.join(model_path,model_evaluation_config[MODEL_NAME_KEY])
            
            model_evaluation_config = ModelEvaluationConfig(model_evaluation_filepath=model_name,time_stamp=self.time_stamp)

            return model_evaluation_config

        except Exception as e:
            return e    
    def get_model_pusher_config(self) -> ModelPushConfig:
        data_artifact = self.training_pepeline_config.artifact_file_dir
        model_pusher_config = self.config_info[MODEL_PUSHER_CONFIG_KEY]
        model_export_dir = os.path.join(data_artifact,model_pusher_config[MDOEL_EXPORT_DIR_KEY])
        model_pusher_config = ModelPushConfig(export_dir_path=model_export_dir)
        return model_pusher_config  

    def get_training_pepeline_config(self) ->TrainigPipelineConfig:
        """in this function we pass the inputs to Entity
        """
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]

            #artifact directory = /home/$USER/Documents/Movies/Movies/artifact'
            artifact_dir = os.path.join(CURRENT_WORKING_DIR,
                                        training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                        )
            training_pipeline_config = TrainigPipelineConfig(artifact_file_dir=artifact_dir)                            
            logging.info(f"training pipeline configuration done {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            return e


