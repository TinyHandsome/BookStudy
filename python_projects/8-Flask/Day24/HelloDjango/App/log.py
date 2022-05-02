
import logging

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

file_filter = logging.Filter(__name__)

file_handler = logging.FileHandler('log.txt')
file_handler.setLevel(level=logging.INFO)
file_formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(threadName)s - %(message)s")
file_handler.setFormatter(file_formatter)

logger.addFilter(file_filter)
file_handler.addFilter(file_filter)
logger.addHandler(file_handler)


logger.critical("Critical? Oh Critical.")
logger.error("Error? Oh Error.")
logger.warning("Warning? Oh Warning.")
logger.info("Info? Oh Info.")
logger.debug("Debug? Oh Debug.")
