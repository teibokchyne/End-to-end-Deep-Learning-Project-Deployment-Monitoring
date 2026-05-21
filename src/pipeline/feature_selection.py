class FeatureSelector:
    def __init__(self, logger, file_handler, config):
        self.config_obj = config
        self.file_handler_obj = file_handler
        self.logger = logger.get_logger(self.__class__.__name__)

    def select_features(self, sampled_data_training):
        predictor_labels = [col for col in sampled_data_training.columns if col != sampled_data_training.columns[-1] and sampled_data_training[col].dtype in ['int64', 'float64']]
        target_labels = [sampled_data_training.columns[-1]]
        return predictor_labels, target_labels