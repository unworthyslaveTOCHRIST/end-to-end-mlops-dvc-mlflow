# Gracious End-to-End Chest cancer classification using mlflow dvc


## Workflow

1. Update config.yaml
2.  Update secrets.yaml [optional]
3.  Update params.yaml
4.  Update the entity
5.  Update the configuration manager in the src config
6.  Update the components
7.  Update the pipeline
8.  Update the main.py
9.  Update the dvc.yaml

# BY GOD'S GRACE ALONE, Gracious information from DVC
import dagshub
dagshub.init(repo_owner='unworthyslaveTOCHRIST', repo_name='end-to-end-mlops-dvc-mlflow', mlflow=True)

import mlflow
with mlflow.start_run():
  mlflow.log_param('parameter name', 'value')
  mlflow.log_metric('metric name', 1)