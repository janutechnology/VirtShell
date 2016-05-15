import logging
import logging.handlers
from config import LOGGER
from config import LOG_FILE

def get_logger(LoggerName):
    # Create logger
    logger = logging.getLogger(LoggerName)
    logger.setLevel(logging.INFO)

    # Create handler
    if LOGGER == "file":    
        handler = logging.FileHandler(LOG_FILE)
    else:
        handler = logging.handlers.SysLogHandler(address='/dev/log')
        
    #handler = SysLogHandler(address='/dev/log')
    handler.setLevel(logging.INFO)
    # Create formatter
    formatter = logging.Formatter('%(asctime)s %(name)s '
                                  '%(levelname)s %(message)s')
    # Add formatter and handler
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger
