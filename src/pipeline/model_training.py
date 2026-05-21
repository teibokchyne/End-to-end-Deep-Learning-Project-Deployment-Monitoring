from sklearn.linear_model import LogisticRegression


class ModelTrainer:
    def __init__(self, logger, file_handler, config):
        self.config_obj = config
        self.file_handler_obj = file_handler
        self.logger = logger.get_logger(self.__class__.__name__)

    def train_model(self, train_data):
        X_train, y_train = train_data
        model = LogisticRegression()
        model.fit(X_train, y_train)
        return model
