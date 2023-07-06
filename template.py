import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

projet_name="textSummarizer"

list_of_files=[
    ".github/workflow/.gitkeep",
    f"src/{projet_name}/__init__.py",
    f"src/{projet_name}/__init__.py",
    f"src/{projet_name}/components/__init__.py",
    f"src/{projet_name}/utils/__init__.py",
    f"src/{projet_name}/utils/common.py",
    f"src/{projet_name}/logging/__init__.py",
    f"src/{projet_name}/config/configuration.py",
    f"src/{projet_name}/pipeline/__init__.py",
    f"src/{projet_name}/entity/__init__.py",
    f"src/{projet_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in list_of_files:
    file_path=Path(file)
    file_dir,file_name=os.path.split(file_path)

    if file_dir !="":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory: {file_dir} for the file {file_name}")

    if ( not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):

        with open(file_path,'w') as f:

            pass
            logging.info(f"creating empty file: {file_path}")

    else:

        logging.info(f"{file_name} already exists")
        
