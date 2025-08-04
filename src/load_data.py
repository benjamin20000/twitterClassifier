import pandas as pd
class Loader:
    @staticmethod
    def load_data(path):
        try:
            df = pd.read_csv(path)
        except Exception as e:
            raise RuntimeError("error when trying to load csv") from e
        return df