from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.logging import logger

class Data_transformationTrainingPipeline:
    def __init__(self):
        pass


    def main(self):
      config=ConfigurationManager()
      data_config=config.get_data_transformation_config()
      datatransformation=DataTransformation(config=data_config)
      datatransformation.convert()
