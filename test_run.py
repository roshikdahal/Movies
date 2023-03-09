from Movies.pipeline.pipelining import Pipelining
from Movies.logger import logging
from Movies.config.configurations import Configurations
from Movies.component.data_ingestion import DataIngestion

def main():
    try:
        data_ingestion = DataIngestion().initialize_data_ingestion()
        print(data_ingestion)
    except Exception as e:
        logging.error(f"{e}")
        print(e)  

if __name__=="__main__":
    main()          