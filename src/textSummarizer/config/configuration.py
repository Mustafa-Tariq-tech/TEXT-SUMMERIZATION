from textSummarizer.constants import *
from textSummarizer.utils.common import create_directories,read_yaml
from textSummarizer.entity import Dataingestionconfig,Datavalidationconfig,DataTransformationConfig


class ConfigurationManager:
    def __init__(self,config_file_path=CONFIG_FILE_PATH,params_file_path=PARAMS_FILE_PATH):
        self.config=read_yaml(config_file_path)
        self.params=read_yaml(params_file_path)
        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)->Dataingestionconfig:
        config=self.config.data_ingestion 
        create_directories([config.root_dir])  

        data_ingestion_config =Dataingestionconfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir

        )
        return data_ingestion_config
    
    def get_validation_config(self) ->Datavalidationconfig:
        config=self.config.data_validation

        create_directories([config.root_dir])

        data_validation_config=Datavalidationconfig(
          root_dir= config.root_dir,
          STATUS_FILE=config.STATUS_FILE,
          required_file= config.required_file

            
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation

        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            tokenizer_name = config.tokenizer_name
        )

        return data_transformation_config