import os
from datetime import date, datetime

CURRENT_WORKING_DIR = os.getcwd()
CONFIG_DIR = "config"
CONFIG_FILE_NAME = "config.yaml"

CONFIG_FILE_DIR = os.path.join(CURRENT_WORKING_DIR,CONFIG_DIR,CONFIG_FILE_NAME)

def get_current_time_stamp():
    return f"{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}"


#trainiig_pepline_config constants defining
TRAINING_PIPELINE_CONFIG_KEY =  "trainig_pipline_config"
TRAINING_PIPELINE_NAME_KEY = "pipeline_name"
TRAINING_PIPELINE_ARTIFACT_DIR_KEY = "artifact_dir"

