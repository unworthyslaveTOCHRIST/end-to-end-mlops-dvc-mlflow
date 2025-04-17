# BY GOD'S GRACE ALONE

from GTLJC_cnnClassifier.config.configuration import ConfigurationManager
from GTLJC_cnnClassifier.components.model_trainer import Training
from GTLJC_cnnClassifier import GTLJC_logger


STAGE_NAME = "Training Stage"


class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()


if __name__ == "__main__":
    try:
        GTLJC_logger.info(f"*******************************")
        GTLJC_logger.info(f">>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<")
        obj = ModelTrainingPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<<<<<\n\nx====================x")

    except Exception as e:
        GTLJC_logger.exception(e)
        raise e