from load_data import Loader

def main():
    data_path = "../data/tweets_dataset.csv"
    loader = Loader()
    loader.load_data(data_path)
