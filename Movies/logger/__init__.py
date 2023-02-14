import logging
import os
from Movies.constants import get_current_time_stamp
LOG_DIR = "movies_logs"



def get_log_file_name():
    return f"log_{get_current_time_stamp()}.log"

LOG_FILE_NAME = get_log_file_name()

os.makedirs(LOG_DIR,exist_ok = True)

LOG_FILE_PATH = os.path.join(LOG_DIR,get_log_file_name())

logging.basicConfig(filename = LOG_FILE_PATH,
 level = logging.DEBUG,
 format = '[%(asctime)s]^;%(levelname)s^;%(lineno)d^;%(filename)s^;%(funcName)s()^;%(message)s',filemode = "w")