import os
from datetime import datetime
import logging

LOGGER_MINIMUM_SEVERITY = os.getenv("LOGGER_MINIMUM_SEVERITY", "INFO").upper()
if LOGGER_MINIMUM_SEVERITY.isdigit():
    logger_minimum_severity = int(LOGGER_MINIMUM_SEVERITY)
    # Values from Logger.MessageSeverity
    if logger_minimum_severity < 600:
        LOGGER_MINIMUM_SEVERITY = "INFO"
    elif logger_minimum_severity < 700:
        LOGGER_MINIMUM_SEVERITY = "WARNING"
    elif logger_minimum_severity < 800:
        LOGGER_MINIMUM_SEVERITY = "ERROR"
    else:
        LOGGER_MINIMUM_SEVERITY = "EXCEPTION"

logging.basicConfig(level=LOGGER_MINIMUM_SEVERITY)


class MiniLogger:
    # TODO Can we so one generic function call by all
    # TODO Shall we user the Python logging package?

    @staticmethod
    def start(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            logging.info(f"{datetime.now()} - START - {message}")
        else:
            logging.info(f"{datetime.now()} - START - {message} - {object}")

    @staticmethod
    def end(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
        """
        if object is None:
            logging.info(f"{datetime.now()} - END - {message}")
        else:
            logging.info(f"{datetime.now()} - END - {message} - {object}")

    @staticmethod
    def info(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            logging.info(f"{datetime.now()} - INFO - {message}")
        else:
            logging.info(f"{datetime.now()} - INFO {message} - {object}")

    @staticmethod
    def warning(message: str = "", object: dict = None):
        """
        Print a log message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            logging.warning(f"{datetime.now()} - WARNING - {message}")
        else:
            logging.warning(f"{datetime.now()} - WARNING {message} - {object}")

    @staticmethod
    def error(message: str = "", object: dict = None):
        """
        Print a log error message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict): The object to be printed.
        """
        if object is None:
            logging.error(f"{datetime.now()} - ERROR - {message}")
        else:
            logging.error(f"{datetime.now()} - ERROR - {message} - {object}")

    @staticmethod
    def exception(message: str = "", object: Exception or dict = None):
        """
        Print a log error message with the current time.

        Parameters:
            message (str): The message to be printed.
            object (dict / Exception): The object / Exception to be printed.
        """
        if isinstance(object, Exception):
            exception = object
        elif isinstance(object, dict):
            exception = object.get("exception")
        else:
            exception = None

        if object is None:
            logging.exception(f"{datetime.now()} - EXCEPTION - {message}")
        else:
            logging.exception(f"{datetime.now()} - EXCEPTION- {message} - {object}", exc_info=exception)
