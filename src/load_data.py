import pandas as pd
class Loader:
    @staticmethod
    def load_data(path):
        df = pd.read_csv(path)
        return df