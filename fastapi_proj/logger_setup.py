import logging
import sys
from config import LOGGING_LEVEL

logger = logging.getLogger(__package__)
logger.setLevel(LOGGING_LEVEL)

handler = logging.StreamHandler(stream = sys.stdout)
handler.setLevel(LOGGING_LEVEL)

formatter = logging.Formatter('%(name)s - %(level)s - %(message)s')

handler.setFormatter(formatter)

logger.addHandler(handler)