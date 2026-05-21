from src.config.config import Config

class DataSampler:
    def __init__(self, logger, file_handler, config):
        self.config_obj = config
        self.file_handler_obj = file_handler
        self.logger = logger.get_logger(self.__class__.__name__)

    def sample_data(self, transformed_data):
        index = int(len(transformed_data) * (1 - self.config_obj.TEST_SIZE))
        sampled_data_training = transformed_data[:index]
        sampled_data_test = transformed_data[index:]
        return sampled_data_training, sampled_data_test
    
    def prepare_train_data(self, sampled_data_training, predictor_labels, target_labels):
        train_data = sampled_data_training[predictor_labels + target_labels]
        return (train_data[predictor_labels], train_data[target_labels])
    
    def prepare_test_data(self, sampled_data_test, predictor_labels, target_labels):
        test_data = sampled_data_test[predictor_labels + target_labels]
        return (test_data[predictor_labels], test_data[target_labels])