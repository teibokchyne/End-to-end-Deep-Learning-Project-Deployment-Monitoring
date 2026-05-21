import onnxruntime as ort
from src.api_server.model_inference import ModelInference
from src.utils.instantiate_objects import InstantiateObjects

class APIModelServices:
    def __init__(self):
        self.instantiate_objects_obj = InstantiateObjects()
        self.config_obj = self.instantiate_objects_obj.config_obj
        self.file_handler_obj = self.instantiate_objects_obj.file_handler_obj
        self.logger = self.instantiate_objects_obj.logger.get_logger(self.__class__.__name__)
        self.model_inference_obj = ModelInference(
            logger = self.instantiate_objects_obj.logger, 
            file_handler = self.file_handler_obj)

    def create_model_api(self,trained_model_path):
        return "https://api.example.com/model"
    
    def load_model(self, model_path: str = None):
        if not model_path:
            model_path = self.config_obj.TRAINED_MODEL_PATH
        return ort.InferenceSession(model_path) 
    
    def predict(self, model, input_data):
        return self.model_inference_obj.perform_inference(model, input_data)
    