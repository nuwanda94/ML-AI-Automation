import logging

class Logger():
    def __init__(self) -> None:
        """
        Initializes an instance of the class.

        This method does not take any parameters.

        Returns:
            None
        """
        pass

    def setup_logger(name, log_file, level=logging.INFO):
        """To setup as many loggers as you want"""
        handler = logging.FileHandler(log_file)
        handler.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger = logging.getLogger(name)
        logger.setLevel(level)
        logger.addHandler(handler)
        return logger
    

    @staticmethod
    def info(logger, msg):
        """
        Logs an informational message using the provided logger.

        Args:
            logger (logging.Logger): The logger instance to use for logging.
            msg (str): The message to be logged.

        Returns:
            None
        """
        logger.info(msg)

    @staticmethod
    def warning(logger, msg):
        """
        Logs a warning message using the provided logger.

        Args:
            logger (logging.Logger): The logger instance to use for logging.
            msg (str): The warning message to be logged.

        Returns:
            None
        """
        logger.warning(msg)

    @staticmethod
    def error(logger, msg):
        """
        Logs an error message using the provided logger.

        Args:
            logger (logging.Logger): The logger instance to use for logging.
            msg (str): The error message to be logged.

        Returns:
            None
        """
        logger.error(msg)

