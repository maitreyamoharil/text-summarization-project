# utils folder contains frequently used functions and acts like a module for us for easy programming
import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations # It is used for return type checking
from box import ConfigBox # Used for easy access of key values from a dictionary
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Read a yaml file and return

    Args:
        path_to_yaml (str): path like input

    Raises:
        Valueerror: if yaml file is empty
        e: empty yaml file

    Returns:
        ConfigBox: ConfigBox type 
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully") 
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e 
    

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """
    Create list of directories

    Args:
        path_to_directories (list): list of path_to_directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created, Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")


@ensure_annotations
def get_size(path: Path) -> str:
    """
    get size in KB

    Args:
        path (Path): path of the file
        
    Returns:
        str: size in KB
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
