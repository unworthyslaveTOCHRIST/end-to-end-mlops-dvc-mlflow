# BY GOD'S GRACE ALONE
from GTLJC_cnnClassifier import GTLJC_logger
import gdown
import os
import zipfile
from GTLJC_cnnClassifier.utils.commons import get_size
from GTLJC_cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self)-> str:
        """
            Graciously fetching data from url
        """

        try:
            dataset_url = self.config.source_URL
            zip_download_dir = self.config.local_data_file
            os.makedirs("artifacts/data_ingestion", exist_ok=True)
            GTLJC_logger.info(f"Graciously downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix = f"https://drive.google.com/uc?/export-download&id={file_id}"
            gdown.download(prefix,zip_download_dir)

            GTLJC_logger.info(f"Graciously downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise 
    

    def extract_zip_file(self):
        """
            BY GOD'S GRACE ALONE
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok = True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)
    


