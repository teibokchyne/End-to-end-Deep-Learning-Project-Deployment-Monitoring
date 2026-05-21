from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class ModelTester:
    def __init__(self, logger, file_handler, config):
        self.config_obj = config
        self.file_handler_obj = file_handler
        self.logger = logger.get_logger(self.__class__.__name__)

    def test_model(self, model, test_data):
        X_test, y_test = test_data
        test_results = model.predict(X_test)
        accuracy = accuracy_score(y_test, test_results)
        report = classification_report(y_test, test_results)
        cm = confusion_matrix(y_test, test_results)

        results = {
            "accuracy": accuracy,
            "classification_report": report,
            "confusion_matrix": cm.tolist(),  # Convert to list for JSON serialization
            "predictions": test_results.tolist()  # Convert to list for JSON serialization
        }
        return results