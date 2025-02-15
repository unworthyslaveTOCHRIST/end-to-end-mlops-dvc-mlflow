# BY GOD'S GRACE ALONE

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir: Path  #An entity for data ingestion Graciously declaring class variables without using the self. prefix, 


    # BY GOD'S GRACE ALONE, the Graced entity section for the base model

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    updated_base_model_path: Path
    params_image_size: list
    params_learning_rate: float
    params_include_top: bool
    params_weights : str
    params_classes: int #An entity for Graciously preparing the base model Graciously declaring class variables without using the self. prefix, 