from load_data import Loader
from parse_data import Parser


def main():
    data_path = "../data/tweets_dataset.csv"
    df = Loader.load_data(data_path)
    parser = Parser(df)
    parser.count_classes()
    parser.calculate_average_lengths()
    # print(df)


main()