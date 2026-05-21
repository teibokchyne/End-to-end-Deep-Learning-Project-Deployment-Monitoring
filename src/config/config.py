class Config:
    INPUT_FILE_PATH = r"data/raw/data.csv"
    TEST_RESULTS_FILE_PATH = r"data/processed/test_results.txt"
    TRAINED_MODEL_PATH = r"/home/lenovo/projects/End-to-end-Deep-Learning-Project-Deployment-Monitoring/models/trained_model.onnx"
    TEST_SIZE = 0.2
    RANDOM_STATE = 42
    
    def __init__(self):
        pass