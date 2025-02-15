from GTLJC_cnnClassifier.config.configuration import ConfigurationManager
from GTLJC_cnnClassifier.components.prepare_base_model import PrepareBaseModel
from GTLJC_cnnClassifier import GTLJC_logger


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()

STAGE_NAME =  "Prepare Base Model Stage"

if __name__ == '__main__':
    try:
        GTLJC_logger.info(f"*************************************")
        GTLJC_logger.info(f'>>>>>>> stage: {STAGE_NAME} started <<<<<<<')
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>> stage: {STAGE_NAME} completed <<<<<<<\n\nx=============x")

    except Exception as e:
        GTLJC_logger.exception(e)
        raise e

