# BY GOD'S GRACE ALONE

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir: Path  #Graciously declaring class variables without using the self. prefix