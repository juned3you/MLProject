import logging
import os
from datetime import datetime
#from exception import CustomException
import sys

LOG_FILE = f"{datetime.now().strftime('%m_%d.log')}"
LOG_PATH = os.path.join(os.getcwd(),"logs",LOG_FILE)
os.makedirs(LOG_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_PATH, LOG_FILE)

logging.basicConfig (
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

#if __name__ == "__main__":
#    try:
#        1/0
#    except Exception as ex:
#        logging.info("Test")
#        raise CustomException(ex, sys)
