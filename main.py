from src.pipeline.data_cleaning import DataCleaner
from src.pipeline.data_sampling import DataSampler
from src.pipeline.data_transformation import DataTransformer
from src.pipeline.feature_selection import FeatureSelector
from src.pipeline.model_preparation import ModelPreparator
from src.pipeline.model_testing import ModelTester
from src.pipeline.model_training import ModelTrainer
from src.utils.instantiate_objects import InstantiateObjects

class Orchestrator:
    def __init__(self):
        self.instantiate_objects_obj = InstantiateObjects()
        self.config_obj = self.instantiate_objects_obj.config_obj
        self.logger = self.instantiate_objects_obj.logger
        self.file_handler_obj = self.instantiate_objects_obj.file_handler_obj
        self.data_cleaner_obj = DataCleaner(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.data_sampler_obj = DataSampler(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.data_transformer_obj = DataTransformer(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.feature_selector_obj = FeatureSelector(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.model_preparator_obj = ModelPreparator(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.model_trainer_obj = ModelTrainer(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)
        self.model_tester_obj = ModelTester(logger = self.logger, file_handler = self.file_handler_obj, config = self.config_obj)

    def run(self):
        # Read file
        data = self.file_handler_obj.read_file(self.config_obj.INPUT_FILE_PATH)
        # Run the data cleaning process
        clean_data = self.data_cleaner_obj.clean_data(data)
        # Run the data transformation process
        transformed_data = self.data_transformer_obj.transform_data(clean_data)
        # Run the data sampling process
        sampled_data_training, sampled_data_testing = self.data_sampler_obj.sample_data(transformed_data)
        # Run the feature selection process
        predictor_labels, target_labels = self.feature_selector_obj.select_features(sampled_data_training)
        # Prepare the data for model training and testing
        train_data = self.data_sampler_obj.prepare_train_data(sampled_data_training, predictor_labels, target_labels)
        test_data = self.data_sampler_obj.prepare_test_data(sampled_data_testing, predictor_labels, target_labels)
        # Run the model training process
        trained_model = self.model_trainer_obj.train_model(train_data)
        # Run the model testing process
        test_results = self.model_tester_obj.test_model(trained_model, test_data)
        self.file_handler_obj.save_file(test_results, self.config_obj.TEST_RESULTS_FILE_PATH)
        # Run the model preparation process
        trained_model_path = self.model_preparator_obj.prepare_model(trained_model, train_data)
        # Run the API server
        # Send a request to the API server to create an API for the trained model

if __name__ == "__main__":
    orchestrator_obj = Orchestrator()
    orchestrator_obj.run()