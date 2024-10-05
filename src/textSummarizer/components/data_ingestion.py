import urllib.request as request
import zipfile
from textSummarizer.logging import logger
from textSummarizer.utils.common import get_size
from textSummarizer.entity import Dataingestionconfig
from pathlib import Path
import os 


class Dataingestion:
    def __init__(self,config:Dataingestionconfig) :
        self.config= config
    

    def dwonload_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers =request.urlretrieve(
                url= self.config.source_URL,
                filename=self.config.local_data_file


            )
            logger.info(f"{filename} Download with following info \n {headers}")
        else:
            logger.info(f"file is already exist at at:{get_size(Path(self.config.local_data_file))}")
     


    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)