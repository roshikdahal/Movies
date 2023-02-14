"""
Created on Monday feb 13 2023
@author: kumar.dahal
This class is created to get the values from yaml file and  return the entity of each type
"""
from Movies.entity.config_entity import DataIngestionConfig,DataValidationConfig,DataTransformationConfig, \
    ModelTrainingConfig, ModelEvaluationConfig,ModelPushConfig,TrainigPipelineConfig

from Movies.constants import *
from Movies.utils import read_yaml_file

class Configurations:
    """
    Location of config.yaml , time stamp to keep the record that
    when the file was read and also the function to read_yaml is initialized.
    """
    def __init__(self,config_file_path:str = CONFIG_FILE_DIR,current_time_stamp:str = get_current_time_stamp()) -> None:
        #initialize the read_yaml function to read yaml file
        self.yaml_reader = read_yaml_file(self.config_file_path)

        self.training_pepeline_config = self.get_training_pepeline_config()
        
        self.time_stamp = current_time_stamp

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        pass

    def get_data_validation_config(self) -> DataValidationConfig:
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass  

    def get_model_training_config(self) -> ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self) -> ModelEvaluationConfig:
        pass 

    def get_model_pusher_config(self) -> ModelPushConfig:
        pass 

    def get_training_pepeline_config(self) ->TrainigPipelineConfig:
        """in this function we get the dict of training_pipeline_config from config.yaml
        by pass to the constants
        """
        try:
            training_pipeline_config = self.yaml_reader[TRAINING_PIPELINE_CONFIG_KEY]
            #artifact directory
            artifact_dir = os.path.join(CURRENT_WORKING_DIR,
                                        training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                        training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
                                        )

        except Exception as e:
            return e


