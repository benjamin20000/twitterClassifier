from io_csv import IoCsv
from parse_data import Parser
from json_write import JsonWriter
from clean_data import Cleaner

def main():
    data_path = "../data/tweets_dataset.csv"
    df = IoCsv.load_data(data_path)
    parser = Parser(df)
    data_result = parser.parse()
    JsonWriter.write2json(data_result)
    cleaner = Cleaner(df)
    clean_df = cleaner.clean()
    data_result_path = "../results/tweets_dataset_cleaned.csv"
    IoCsv.write_data(data_result_path, clean_df)



main()