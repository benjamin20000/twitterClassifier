import pandas as pd

class IoCsv:
    @staticmethod
    def load_data(path):
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise RuntimeError("error when trying to load csv") from e
        return df

    @staticmethod
    def write_data(path, df):
        try:
            df.to_csv(path, index=False)
        except Exception as e:
            raise RuntimeError("error when trying to write csv") from e

