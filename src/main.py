from io_csv import IoCsv
from parse_data import Parser
from json_write import JsonWriter
from clean_data import Cleaner
from config import result_json_path, data_result_path, csv_data_path

def analyzation(df):
    parser = Parser(df)
    data_result = parser.parse()
    JsonWriter.write2json(data_result,result_json_path)

def cleaning(df):
    cleaner = Cleaner(df)
    clean_df = cleaner.clean()
    IoCsv.write_data(data_result_path, clean_df)

def main():
    df = IoCsv.load_data(csv_data_path)
    analyzation(df)
    cleaning(df)

if __name__ == "__main__":
    main()