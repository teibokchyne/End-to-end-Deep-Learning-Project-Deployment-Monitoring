import logging

class Logger:
    is_configured = False

    def __init__(self):
        pass

    @classmethod
    def configure(cls):
        if not cls.is_configured:
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            cls.is_configured = True

    @classmethod
    def get_logger(cls, name):
        if cls.is_configured is False:
            cls.configure()
        return logging.getLogger(name)
