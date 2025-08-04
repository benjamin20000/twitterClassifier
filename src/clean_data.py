class Cleaner:
    def drop_punctuation_marks(self, df):
        symbols = "!#$%&()*+-./:,;<=>?[]^_`{|}~\n"
        dataClean = df['Text']
        dataClean = dataClean.str.translate({ord(symbol): "" for symbol in symbols})
        print(dataClean)
        # print(df['Text'])
    def clean(self, df):
        self.drop_punctuation_marks(df)
