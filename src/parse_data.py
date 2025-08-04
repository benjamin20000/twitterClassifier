class Parser:
    def __init__(self ,df):
        self.df = df

    def count_classes(self):
        target_counts = self.df.value_counts("Biased")
        result = {"antisemitic": target_counts[1],
                    "non_antisemitic":target_counts[0],
                    "total": target_counts[0] + target_counts[1]} ## TODO add unspecified
        return result

    def calculate_average_lengths(self,total_tweets):
        ## count the words in antisemitic tweets
        antisemitic_words = " ".join(self.df[self.df["Biased"] == 1]['Text'].astype(str)).split(" ")
        antisemitic_words_count = len(antisemitic_words)

        ## count the words in non-antisemitic tweets
        non_antisemitic_words = " ".join(self.df[self.df["Biased"] == 0]['Text'].astype(str)).split(" ")
        non_antisemitic_words_count = len(non_antisemitic_words)
        result = {"antisemitic":antisemitic_words_count/total_tweets["antisemitic"],
                  "non_antisemitic":non_antisemitic_words_count/total_tweets["non_antisemitic"]}
        return result


    def parse(self):
        total_tweets = self.count_classes()
        average_lengths = self.calculate_average_lengths(total_tweets)





