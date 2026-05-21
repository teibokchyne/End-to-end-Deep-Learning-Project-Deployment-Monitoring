import json
import numpy as np

class ModelInference:
    def __init__(self, logger, file_handler):
        self.logger = logger.get_logger(self.__class__.__name__)
        self.file_handler = file_handler

    def _clean_result(self, result):
        cleaned = {
            "churn_prediction": result[0][0].tolist(),
            "churn_probabilities": result[1]
        }

        json_string = json.dumps(cleaned)

        return json_string

    def _preprocess_input_data(self, input_data):
        # Implement the logic to preprocess the input data for the model
        self.logger.info("Preprocessing input data")
        # Example: Convert input data to numpy array or tensor as required by the model
        np_array = np.array(
            [list(input_data.values())],
            dtype=np.float32
        )
        return np_array
    
    def _run_model(self, model, input_data):
        # Implement the logic to run the model with the input data
        self.logger.info("Running model with input data")
        input_name = model.get_inputs()[0].name
        result = model.run(None, {input_name: input_data})
        return result

    def _verify_input_data(self, input_data):
        # Implement the logic to verify the input data
        self.logger.info("Verifying input data")
        # Add more verification logic as needed
        return True
    
    def perform_inference(self, model, input_data: dict):
        # Implement the logic to perform inference using the model and input data
        self.logger.info("Performing inference")
        if self._verify_input_data(input_data):
            np_array = self._preprocess_input_data(input_data)
            result = self._run_model(model, np_array)
            cleaned = self._clean_result(result)
            return cleaned
        else:
            self.logger.error("Failed to verify input data")
            return {"error": "Invalid input data"}