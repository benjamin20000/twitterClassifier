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

    def drop_un_classified_rows(self):
        mask = (self.df['Biased'] == 0) | (self.df['Biased'] == 1)
        self.df = self.df[mask]

    def clean(self):
        text_col = self.df['Text'] ## get the text col
        clean_text = self.drop_punctuation_marks(text_col)#clean col from punctuation_marks
        lower_text = self.convert_to_lowercase(clean_text)#convert it to lowercase
        self.df['Text'] = lower_text ## set the new clean col as a df col
        self.drop_un_classified_rows()
