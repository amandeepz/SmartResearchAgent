# logger utility for Smart Research Agent
import logging
import os

LOG_LEVEL = os.getenv('LOG_LEVEL', 'INFO').upper()

logger = logging.getLogger('smart_research_agent')
logger.setLevel(LOG_LEVEL)

formatter = logging.Formatter('[%(asctime)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H:%M:%S')

console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# optional: file logging
log_file = os.getenv('LOG_FILE')
if log_file:
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

# Example usage:
# from utils.logger import logger
# logger.info('Agent initialized')
