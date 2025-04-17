# BY GOD'S GRACE Reusing the evalution configuration object to GRACIOUSLY buildup the evaluation Component

import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from GTLJC_cnnClassifier.entity.config_entity import EvaluationConfig
from GTLJC_cnnClassifier.utils.commons import save_json
from GTLJC_cnnClassifier import GTLJC_logger

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    def _valid_generator(self):

        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.30
        )

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation = "bilinear"
        )

        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )

        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs

        )


    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
        # ALL THANKS AND GLORY TO THE AND my ONLY GOD AND LORD JESUS CHRIST ALONE
    

    def evaluation(self):
        self.model = self.load_model(self.config.path_of_model)
        self._valid_generator()
        self.score = self.model.evaluate(self.valid_generator)
        self.save_score()

    def save_score(self):
        scores = {"loss":self.score[0], "accuracy":self.score[1]}
        save_json(path=Path("scores.json"), data = scores)
        # ALL THANKS AND GLORY TO THE AND my ONLY GOD AND LORD JESUS CHRIST ALONE

    
    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        import dagshub
        dagshub.init(repo_owner='unworthyslaveTOCHRIST', repo_name='end-to-end-mlops-dvc-mlflow', mlflow=True)

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics(
                { "loss": self.score[0], "accuracy": self.score[1] }
            )

            # Graciously checking if Model registry does not work with file store
            #if tracking_url_type_store != "file":


                # Graciously registering the model
                # There are other ways to use the model registry, which depends on the use case,
                # please Graciously refer to the doc for more information:
                # https://mlflow.org/docs/latest/model-registry.html#api-workflow

            mlflow.keras.log_model(self.model, artifact_path="artifacts/training/model.h5", registered_model_name="VGG16Model")
            GTLJC_logger.info(f"Graciously logged model to mlflow")
        
    
