import logging
import sys

logger = logging.getLogger("LushaTest")


def init_logger(logger_level):
    logger.setLevel(logger_level)
    ch = logging.StreamHandler(sys.stdout)
    logger.addHandler(ch)
