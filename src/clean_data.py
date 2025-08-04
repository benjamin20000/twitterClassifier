class Cleaner:
    def __init__(self, df):
        self.df = df

    def drop_punctuation_marks(self,text_col):
        symbols = "!#$%&()*+-./:,;<=>?[]^_`{|}~\n"
        clean_text = text_col.str.translate({ord(symbol): "" for symbol in symbols})
        return clean_text

    def convert_to_lowercase(self, text_col):
        lower_text = text_col.str.lower()
        return lower_text

    def clean(self):
        text_col = self.df['Text']
        clean_text = self.drop_punctuation_marks(text_col)
        lower_text = self.convert_to_lowercase(clean_text)
        self.df['Text'] = lower_text
        # self.drop_un_classified_rows()
