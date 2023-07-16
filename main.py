from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionPipeline
from src.textSummarizer.logging import logger
from src.textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from src.textSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline




STAGE_NAME="Data Ingestion Stage"

try:

    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_ingestion=DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} ended <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e 



STAGE_NAME="Data Validatipn Stage"

try:

    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_validation=DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} ended <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e 




STAGE_NAME="Data Transformation Stage"

try:

    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<")
    data_transformation=DataTransformationTrainingPipeline()
    data_transformation.main()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} ended <<<<<<<<<")

except Exception as e:
    logger.exception(e)
    raise e 