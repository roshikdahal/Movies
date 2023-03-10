"""
@author: kumar dahal
created date:14 feb 2023
this class is created to make pipeline of each entity  and steps are performed one after another 
by identifying the changes made, ,if changes are there then only that entity will run otherwise control will move to next entity.
"""
from Movies.config.configurations import Configurations
from Movies.entity.artifact_entity import DataIngestionArtifact,DataValidationArtifact
from Movies.component.data_ingestion import DataIngestion
from Movies.component.data_validation import DataValidation

class Pipelining:
    def __init__(self,config: Configurations= Configurations()) -> None:
        try:
            #store the config informations
            self.config = config
        except Exception as e:
            return e

    def start_data_ingestion(self)->DataIngestionArtifact:
        """
        this function will call DataIngestion which run url downloading and like steps
        return :DataIngestionArtifact 
        """
        try:
            #create the object of DataIngestion from components and "dataingestionconfig" is the parameter that our "DataIngestion" needs
            data_ingestion = DataIngestion(dataingestionconfig=self.config.get_data_ingestion_config())
            #perform download of data,extract and train test split
            return data_ingestion.initialize_data_ingestion()
        except Exception as e:
            return e   

    def start_data_validation(self,data_ingestion_artifact:DataIngestionArtifact) ->DataValidationArtifact:
        try:

            data_validation = DataValidation(data_validation_config=self.config.get_data_validation_config(),
                                             data_ingestion_artifact=data_ingestion_artifact
                                             )
            return data_validation.initiate_data_validation()
            

        except Exception as e:
            return e    

    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            return e   
    
    def start_model_training(slef):
        try:
            pass
        except Exception as e:
            return e   

    def start_model_evaluation(self):
        pass

    def start_model_push(self):
        pass



    def run_pipelining(self):
        try:
            #run data ingestion artifact
            data_ingestion_artifact =self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
        except Exception as e:
            return e             
