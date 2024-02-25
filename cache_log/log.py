import logging

class MyLogger:
    def __init__(self, name, filename='example.log', filemode='w', level=logging.DEBUG):
        
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Create console handler
        self.consoleHandler(level, formatter)

        # Create file handler if filename is provided
        self.fileHandler(filename, filemode, level, formatter)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)

    def consoleHandler(self, level, formatter):
        ch = logging.StreamHandler()
        ch.setLevel(level)
        ch.setFormatter(formatter)
        self.logger.addHandler(ch)

    def fileHandler(self, filename, filemode, level, formatter):
        if filename:
            fh = logging.FileHandler(filename, filemode)
            fh.setLevel(level)
            fh.setFormatter(formatter)
            self.logger.addHandler(fh)


if __name__ == "__main__":
    # Example usage:
    logger_name = 'example_logger'
    log_filename = 'critical.log'
    filemode = 'w'
    level = logging.CRITICAL
    logger = MyLogger(logger_name, log_filename, filemode, level)

    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
