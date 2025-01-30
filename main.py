# BY GOD'S GRACE ALONE
from GTLJC_cnnClassifier import GTLJC_logger
from GTLJC_cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Date Ingestion Stage"

try:
        GTLJC_logger.info(f'>>>>>>> stage: {STAGE_NAME} started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>> stage: {STAGE_NAME} completed <<<<<<<\n\nx=============x")

except Exception as e:
    GTLJC_logger.exception(e)
    raise e