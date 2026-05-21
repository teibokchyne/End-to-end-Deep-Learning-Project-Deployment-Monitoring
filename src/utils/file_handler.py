import pandas as pd
from pathlib import Path

class FileHandler:
    def __init__(self, logger, config):
        self.config_obj = config
        self.logger = logger.get_logger(self.__class__.__name__)

    def save_file(self, test_results, file_path):
        try:
            with open(file_path, 'w') as f:
                f.write(str(test_results))
            self.logger.info(f"Test results saved successfully at: {file_path}")
        except Exception as e:
            self.logger.error(f"Error saving test results: {e}")

    def read_file(self, file_path):
        file_path_Path = Path(file_path)
        if not file_path_Path.exists():
            self.logger.error(f"File not found: {file_path}")
        
        if file_path_Path.suffix == ".csv":
            return pd.read_csv(file_path)
        elif file_path_Path.suffix == ".parquet":
            return pd.read_parquet(file_path)
        else:
            self.logger.error(f"Unsupported file format: {file_path_Path.suffix}")
    
    def save_dataframe(self, df, file_path, extension="csv"):
        if extension == "csv":
            df.to_csv(file_path, index=False)
        elif extension == "parquet":
            df.to_parquet(file_path, index=False)
        elif extension == "json":
            df.to_json(file_path, orient="records", lines=True)
        elif extension == "pkl":
            df.to_pickle(file_path)
        elif extension == "xlsx":
            df.to_excel(file_path, index=False)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
