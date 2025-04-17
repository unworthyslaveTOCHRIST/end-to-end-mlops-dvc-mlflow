# BY GOD'S GRACE ALONE\
# import sys
# print("System path", sys.path)

import sys
sys.path.append("c:\\users\\for_christ_my_love\\desktop\\end-to-end-mlops-dvc-mlflow\\src")

from GTLJC_cnnClassifier.config.configuration import ConfigurationManager
from GTLJC_cnnClassifier.components.data_ingestion import DataIngestion
from GTLJC_cnnClassifier import GTLJC_logger


STAGE_NAME = "Data Ingestion Stage"

class DataIngestionTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == '__main__':
    try:
        GTLJC_logger.info(f'>>>>>>> stage: {STAGE_NAME} started <<<<<<<')
        obj = DataIngestionTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>> stage: {STAGE_NAME} completed <<<<<<<\n\nx=============x")

    except Exception as e:
        GTLJC_logger.exception(e)
        raise e