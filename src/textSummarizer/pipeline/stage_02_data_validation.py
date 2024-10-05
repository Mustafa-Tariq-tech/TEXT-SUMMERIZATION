
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_validation import Datavalidation
from textSummarizer.logging import logger

class Data_validationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
      config=ConfigurationManager()
      datavalidation_config=config.get_validation_config()
      datavalidation=Datavalidation(config=datavalidation_config)
      datavalidation.validation_all_files_exist()

