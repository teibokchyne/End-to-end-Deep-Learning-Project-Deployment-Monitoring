from skl2onnx import to_onnx
import numpy as np

class ModelPreparator:
    def __init__(self, logger, file_handler, config):
        self.config_obj = config
        self.file_handler_obj = file_handler
        self.logger = logger.get_logger(self.__class__.__name__)

    def convert_to_onnx(self, model, sample_row):
        sample_input = sample_row.to_numpy().astype(np.float32)
        onnx_model = to_onnx(
            model,
            sample_input,
            target_opset=12
        )
        return onnx_model
    
    def prepare_model(self, trained_model, train_data):
        # Save the trained model to a file
        # convert to onnx format
        onnx_model = self.convert_to_onnx(trained_model, train_data[0][:1])
        with open(self.config_obj.TRAINED_MODEL_PATH, "wb") as f:
            f.write(onnx_model.SerializeToString())

        return self.config_obj.TRAINED_MODEL_PATH