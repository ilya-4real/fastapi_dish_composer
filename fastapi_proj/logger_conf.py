import json
import logging
import logging.config
import logging.handlers


logger = logging.getLogger(__name__)


def configure_logger():
    logger_config = None
    with open("fastapi_proj/logger_config.json") as json_conf:
        logger_config = json.load(json_conf)

    logging.config.dictConfig(config=logger_config)
