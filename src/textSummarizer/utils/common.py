import os 
from src.textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import yaml
from box.exceptions import BoxValueError

@ensure_annotations
def read_yaml(path_to_yaml:yaml)->ConfigBox:


    """ Read yaml file

    Args: 
        path_to_yaml (str): path to yaml file

    Raises:
        ValueError : if yaml file is empty
        e: empty file

    Return:
        ConfigBox: ConfigBox type    
    """

    try:

        with open(path_to_yaml) as yaml_file:
            content=yaml.safe_load(yaml_file)

            logger.info(f"yaml file {path_to_yaml} load successfully")

            return ConfigBox(content)
    except BoxValueError:

        raise ValueError("yaml file is empty")
    
    except Exception as e:
        raise e
    


@ensure_annotations
def create_directories(path_to_directories:list, verbose=True):


        """"creat list of directories
            Args :
                path_to_directories: list of path to directories
        
                ignore_log (bool,optional): ignore if multiple dirs is to be created.
        """

        for path in path_to_directories:

            os.makedirs(path,exist_ok=True)

            if verbose:

                logger.info(f"created directory at {path}")

@ensure_annotations
def get_size(path:Path)-> str:
     
     """ get size in KB

        Args: 
            path (Path): path to the file

        Returns :

            str : size in KB
     """

     size_kb=round(os.path.getsize(path)/1024)

     return f"~ {size_kb} KB"



        