# ALL THANKS AND GLORY TO THE AND my ONLY GOD AND LORD JESUS CHRIST ALONE

import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO, format = '[%(asctime)s]: %(message)s:')

GTLJC_project_name = "GTLJC_cnnClassifier"

GTLJC_list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{GTLJC_project_name}/__init__.py",
    f"src/{GTLJC_project_name}/components/__init__.py",
    f"src/{GTLJC_project_name}/utils/__init__.py",
    f"src/{GTLJC_project_name}/config/__init__.py",
    f"src/{GTLJC_project_name}/config/configuration/__init__.py",
    f"src/{GTLJC_project_name}/pipeline/__init__.py",
    f"src/{GTLJC_project_name}/entity/__init__.py",
    f"src/{GTLJC_project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"

]

for GTLJC_filepath in GTLJC_list_of_files:
    GTLJC_filepath = Path(GTLJC_filepath)
    GTLJC_filedir, GTLJC_filename = os.path.split(GTLJC_filepath)

    if GTLJC_filedir != "":
        os.makedirs(GTLJC_filedir, exist_ok=True)
        logging.info(f"Graciously creating directory: {GTLJC_filedir} for the file: {GTLJC_filename}")

    if (not os.path.exists(GTLJC_filepath)) or (os.path.getsize(GTLJC_filepath) == 0):
        with open(GTLJC_filepath, "w")  as f:
            pass
            logging.info(f"Graciously creating empty file: {GTLJC_filepath}")

    else:
        logging.info(f"{GTLJC_filename} already exists")