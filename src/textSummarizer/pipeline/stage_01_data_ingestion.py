from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_ingestion import Dataingestion
from textSummarizer.logging import logger


class Data_ingestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        dataingestion_config=config.get_data_ingestion_config()
        dataingestion=Dataingestion(config=dataingestion_config)
        dataingestion.dwonload_file()
        dataingestion.extract_file()