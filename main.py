# BY GOD'S GRACE ALONE
from GTLJC_cnnClassifier import GTLJC_logger
from GTLJC_cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from GTLJC_cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from GTLJC_cnnClassifier.pipeline.stage_03_model_trainer import ModelTrainingPipeline
from GTLJC_cnnClassifier.pipeline.stage_04_model_evaluation import EvaluationPipeline

STAGE_NAME = "Date Ingestion Stage"

try:
        GTLJC_logger.info(f'>>>>>>> stage: {STAGE_NAME} started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>> stage: {STAGE_NAME} completed <<<<<<<\n\nx=============x")

except Exception as e:
    GTLJC_logger.exception(e)
    raise e

STAGE_NAME = "Prepare Base Model Stage"
try:
        GTLJC_logger.info(f"*************************************")
        GTLJC_logger.info(f'>>>>>>> stage: {STAGE_NAME} started <<<<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>> stage: {STAGE_NAME} completed <<<<<<<\n\nx=============x")

except Exception as e:
        GTLJC_logger.exception(e)
        raise e


STAGE_NAME = "Model Training Stage"
try:
        GTLJC_logger.info(f"*******************************")
        GTLJC_logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\nx====================x")

except Exception as e:
        GTLJC_logger.exception(e)
        raise e


STAGE_NAME = "Model Evaluation Stage"
try:
        GTLJC_logger.info(f"*************************************")
        GTLJC_logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<<<<\n\nx===============x")

except Exception as e:
        GTLJC_logger.exception(e)
        raise e