
class Parser:
    def __init__(self ,df):
        self.df = df

    def count_classes(self):
        counts = self.df.value_counts("Biased")
        result = {"antisemitic": counts[1],
                    "non_antisemitic":counts[0],
                    "total": counts[0] + counts[1]} ## TODO add unspecified
        return result


