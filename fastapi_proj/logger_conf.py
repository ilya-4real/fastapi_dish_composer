import json
import logging
import logging.config

from fastapi_proj.config import settings

logger = logging.getLogger(__name__)


def configure_logger():
    logger_config = None
    config_file = (
        "fastapi_proj/logger_config_dev.json"
        if settings.MODE == "DEV"
        else "fastapi_proj/logger_config.json"
    )
    print(config_file)
    with open(config_file) as json_conf:
        logger_config = json.load(json_conf)

    logging.config.dictConfig(config=logger_config)
