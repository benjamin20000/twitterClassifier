from load_data import Loader
from parse_data import Parser


def main():
    data_path = "../data/tweets_dataset.csv"
    loader = Loader()
    df = loader.load_data(data_path)
    parser = Parser(df)
    parser.count_classes()
    # print(df)


main()