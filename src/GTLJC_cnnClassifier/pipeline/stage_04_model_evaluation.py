# ALL THANKS AND GLORY TO THE AND my ONLY GOD AND LORD JESUS CHRIST ALONE

from GTLJC_cnnClassifier.config.configuration import ConfigurationManager
from GTLJC_cnnClassifier.components.model_evaluation_mlflow import Evaluation
from GTLJC_cnnClassifier import GTLJC_logger

STAGE_NAME = "Evaluation Stage"

class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()
        # evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        GTLJC_logger.info(f"*************************************")
        GTLJC_logger.info(f">>>>>>>>>>>>>>>> {STAGE_NAME} started <<<<<<<<<<<<<<<<<<<")
        obj = EvaluationPipeline()
        obj.main()
        GTLJC_logger.info(f">>>>>>>>> stage {STAGE_NAME} completed  <<<<<<<<<<<<\n\nx===============x")

    except Exception as e:
        GTLJC_logger.exception(e)
        raise e