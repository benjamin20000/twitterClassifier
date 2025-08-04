
class Parser:
    def __init__(self ,df):
        self.df = df

    def count_classes(self):
        print(self.df.value_counts("Biased"))

