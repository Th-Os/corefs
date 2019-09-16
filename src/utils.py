import logging
from sys import stdout
import os


def init_logging(name="root", debug=False, with_file=True):
    formatter = logging.Formatter('[%(name)s] - %(asctime)s.%(msecs)03d %(threadName)s: '
                                  '%(message)s', datefmt="%Y-%m-%d %H:%M:%S")
    if with_file:
        if os.path.isdir("logs") is False:
            os.mkdir("logs")
        fh = logging.FileHandler(os.path.join("logs", name + ".log"))
    sh = logging.StreamHandler(stream=stdout)

    if with_file:
        fh.setFormatter(formatter)
    sh.setFormatter(formatter)

    logger = logging.getLogger() if name == "root" else logging.getLogger(name)

    if len(logger.handlers) > 0:
        logger.handlers = []

    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    if with_file:
        logger.addHandler(fh)
    logger.addHandler(sh)

    # duplicate logs:
    # https://stackoverflow.com/questions/19561058/duplicate-output-in-simple-python-logging-configuration/19561320
    logger.propagate = False

    return logger
