from collections import namedtuple
"""
this information are provided with yaml file.
in yaml we provide all the information and read  yaml file 
and create object for it
"""

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url",
                                                        "tgz_download_dir",
                                                        "raw_data_dir",
                                                        "ingested_train_dir",
                                                        "ingested_test_dir"])


DataValidationConfig = namedtuple("DataValidationConfig",["scehma_file_path"])


#preprocessed_file_path contains file path of DataValidationConfig pickel file
DataTransformationConfig = namedtuple("DataTransformationConfig",["tranfored_train_dir",
                                                                  "transormed_test_dir",
                                                                  "preprocessed_file_path"])

#trained_model_filepath = location of pickel file path
ModelTrainingConfig = namedtuple("ModelTrainingConfig",["trained_model_filepath","base_accuracy_model"])


ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",["model_evaluation_filepath","time_stamp"])


ModelPushConfig = namedtuple("ModelPushConfig",["export_dir_path"])

TrainigPipelineConfig = namedtuple("TrainigPipelineConfig",["artifact_file_dir"])
