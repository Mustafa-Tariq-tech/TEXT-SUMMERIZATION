from textSummarizer.entity import Datavalidationconfig
import os 







class Datavalidation:
    def __init__(self,config:Datavalidationconfig) :
        self.config= config
    
    def validation_all_files_exist(self)->bool:
        try:
            validation_status= None
            all_files=os.listdir(os.path.join("artifacts","data_ingestion","samsum_dataset"))
            for file in all_files:
                if file not in self.config.required_file:
                    validation_status=False
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation  Status: {validation_status} ")
                else:

                    
                    validation_status=True
                    with open(self.config.STATUS_FILE,'w') as f:
                        f.write(f"Validation  Status: {validation_status} ")
        except Exception as e:
            raise e