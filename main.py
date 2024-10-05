from textSummarizer.logging import logger

from textSummarizer.pipeline.stage_01_data_ingestion import Data_ingestionTrainingPipeline

from textSummarizer.pipeline.stage_02_data_validation import Data_validationTrainingPipeline
from textSummarizer.pipeline.stage_03_data_transformation import Data_transformationTrainingPipeline

STAGE_NAME="Data Ingestion stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<<")
    obj=Data_ingestionTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME}  completed  <<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data validation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<<")
    obj=Data_validationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME}  completed  <<<<<")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Transformation stage"
try:
    logger.info(f">>>> stage {STAGE_NAME} Started <<<<<")
    obj=Data_transformationTrainingPipeline()
    obj.main()
    logger.info(f">>>> stage {STAGE_NAME}  completed  <<<<<")

except Exception as e:
    logger.exception(e)
    raise e








