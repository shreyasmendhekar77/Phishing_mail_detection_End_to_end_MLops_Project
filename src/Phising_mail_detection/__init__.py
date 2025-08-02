import logging
import os 
import sys


logging_str="[%(asctime)s:%(levelname)a:%(module)s:%(message)s]"


log_file_dir='logs'

log_file_path= os.path.join(log_file_dir,"Running_logs.log")
os.makedirs(log_file_dir,exist_ok=True)


logging.basicConfig(

    level=logging.INFO,
    format=logging_str,

    handlers=[
    logging.FileHandler(log_file_path),
    logging.StreamHandler(sys.stdout)
    ]
)


logger=logging.getLogger("Phishing_Project_Logger")



