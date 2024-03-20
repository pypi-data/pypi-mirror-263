import logging
import sys

class Logger:
    def __init__(self, name, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        self.logger.addHandler(logging.StreamHandler(sys.stdout))
        # self.logger.addHandler(logging.StreamHandler(sys.stderr))
        # self.logger.addHandler(logging.FileHandler('cybersailor.log'))
        self.logger.propagate = False

    def __getattr__(self, item):
        return getattr(self.logger, item)