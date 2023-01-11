import logging
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Logger:
    def __init__(self, name: str):
        self.logger = logging.getLogger(__name__ + "." + name)


class Singleton(type):
    """
    Class singleton
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
