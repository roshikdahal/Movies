"""
Created on Monday feb 13 2023
@author: kumar.dahal
"""
import os
from datetime import date, datetime

CURRENT_WORKING_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"
SCHEMA_FILE_NAME = "schema_validation.yaml"
CONFIG_FILE_DIR = os.path.join(CURRENT_WORKING_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

SCHEMA_FILE_DIR = os.path.join(CURRENT_WORKING_DIR,CONFIG_DIR,SCHEMA_FILE_NAME)
#schema constant
COLUMNS = 'columns'

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


#trainiig_pepline_config constants defining
TRAINING_PIPELINE_CONFIG_KEY =  "trainig_pipline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"

#data ingestion  constants defining ,DATA_INGESTION_ARTIFACT_DIR for folder creation 
DATA_INGESTION_CONFIG_KEY =  "data_ingestion_config"
DATA_INGESTION_ARTIFACT_DIR = "data_ingestion"
DATA_INGESTION_DOWNLOAD_URL_KEY = "dataset_download_url"
RAW_DATA_DIR_KEY = "raw_data_dir"
TGZ_DOWNLOAD_DIR_KEY = "tgz_download_dir"
INGESTED_DIR_KEY = "ingested_dir"
INGESTED_TRAIN_DIR_KEY = "ingested_train_dir"
INGESTED_TEST_DIR_KEY = "ingested_test_dir"

#data validation config constant defining
DATA_VALIDATION_CONFIG_KEY = "data_validation_config"
SCHEMA_FILE_DIR_KEY = "schema_file_dir"
SCHEMA_FILE_NAME_KEY = "schema_file_name"
REPORT_FILE_NAME = "data_report_file_name"
REPORT_PAGE_FILE = 'report_page_name'
DATA_VALIDATION_ARTIFACT_DIR_NAME = 'data_validation'  #after running data validation pipeline ,generate artifact so to store that artifact we create this folder


#data transformation config constant defining
DATA_TRANSFORMATION_CONFIG_KEY = "data_transformation_config"
TRANSFORMED_DIR_KEY = "transformed_dir"
TRANSFORMED_TRAIN_DIR_KEY = "transformed_train_dir"
TRANSFORMED_TEST_DIR_KEY = "transformed_test_dir"
PREPROCESSED_DIR_KEY = "preprocessed_dir"
PREPROCESSED_OBJECT_FILE_NAME_KEY ="preprocessed_object_file_name"

#model training config conctant defining
MODEL_TRAINING_CONFIG_KEY = "model_training_config"
TRAINED_MODEL_DIR_KEY = "trained_model_dir"
MODEL_FILE_NAME_KEY = "model_file_name"
MODEL_BASE_ACCURACY_KEY = "base_accuracy"

#model evaluation config constant
MODEL_EVALUATION_CONFIG_KEY = "model_evaluation_config"
MODEL_FILE_DIR_KEY = "model_file_dir"
MODEL_NAME_KEY = "model_name"

#model pusher config constant
MODEL_PUSHER_CONFIG_KEY = "model_pusher_config"
MDOEL_EXPORT_DIR_KEY = "model_export_dir"