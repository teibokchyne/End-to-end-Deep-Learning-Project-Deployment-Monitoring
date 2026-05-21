from src.config.config import Config
from src.utils.file_handler import FileHandler
from src.utils.logger import Logger

class InstantiateObjects:
    def __init__(self):
        self.config_obj = Config()
        self.logger = Logger()
        self.file_handler_obj = FileHandler(logger = self.logger, config = self.config_obj)
