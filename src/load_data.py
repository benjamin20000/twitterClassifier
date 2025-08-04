import pandas as pd
class Loader:
    def load_data(self,path):
        df = pd.read_csv(path)
        return df