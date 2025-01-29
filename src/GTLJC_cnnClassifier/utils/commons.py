# BY GOD'S GRACE ALONE

import os
from box.exceptions import BoxValueError
import yaml
from GTLJC_cnnClassifier import GTLJC_logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
        By The Lord Jesus' Grace alone,
        the decorator reads yaml file and return

        Args: 
            path_to_yaml (str) : path like input

        Raises:
            ValueError: if yaml file is empty
            e: empty file

        Returns:
            ConfigBox : ConfigBox type

    """

    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            GTLJC_logger.info(f"yaml file: {path_to_yaml} loaded Graciously successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    @ensure_annotations
    def create_directories(path_to_directories: list, verbose = True):
        """
            Graciously creates a list of directories

            Args:
                path_to_directories (list): list of paths of directories
                ignore_log(bool, optional): ignore if multiple dirs are to be created, Default to False
        """

        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                GTLJC_logger.info(f"created directory at: {path}")


@ensure_annotations
def save_json(path: Path, data: dict):
    """
        Graciously saving json data

        Args: 
            path (Path): path to json file
            data (dict): data to be saved in json file
    """

    with open(path, "w") as f:
        json.dump(data, f, indent = 4)

    GTLJC_logger.info(f"json file saved at {path}")



@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
        Graciously loads json files data

        Args:
            path: {Path} path to json file

        Returns:
            ConfigBox: data as class attributes instead of a mere dict

    """

    with open(path) as f:
        content = json.load(f)

    GTLJC_logger.info(f"Graced json file saved at: {path}")


@ensure_annotations
def save_bin(data: Any, path: Path):
    """
        Graciously saving bin file

        Args:
            data (Any): data to be saved as binary
            path (Path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    GTLJC_logger.info(f"binary file saved at : {path}")

@ensure_annotations
def load_bin(path: Path) -> Any:
    """
        Graciously loading binary file

        Args:
            path(Path): Gracious path to binary file

        Returns:
            Any: object stored in the file
    """

    data = joblib.load(path)
    GTLJC_logger.info(f"binary file loaded from: {path}")
    return data

@ensure_annotations
def get_size(path: Path) -> str:
    '''
        Graciously gets size in kb
        
        Args:
            path (Path) : path of the file

        Returns:
            str: size in kb

    '''

    size_in_kb = round(os.path.getsize{path}/1024)
    return f"~ Gracious {size_in_kb} KB"

def decodeImage(imgString, fileName):
    imgdata = base64.b64decode(imgString)
    with open(fileName, "wb") as f:
        f.write(imgdata)
        f.close()


def encodeImageIntoBase64(croppedImagePath):
    with open(croppedImagePath, "rb") as f:
        return base64.b64encode(f.read())
        