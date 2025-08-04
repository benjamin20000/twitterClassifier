from collections import Counter
import pandas as pd
from pandas.core.computation.common import result_type_many


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

        ## count the words in all tweets
        all_tweets_count = non_antisemitic_words_count + antisemitic_words_count

        ##create the result dict
        result = {"antisemitic":antisemitic_words_count/total_tweets["antisemitic"],
                  "non_antisemitic":non_antisemitic_words_count/total_tweets["non_antisemitic"],
                  "total":all_tweets_count/total_tweets["total"]}
        return result

    def longest_tweets(self):
        ## find the 3 longest antisemitic tweets
        antisemitic_tweets = self.df[self.df["Biased"] == 1]['Text']
        longest_antisemitic_tweets =  antisemitic_tweets.map(lambda x:len(x)).nlargest(3)
        antisemitic_tweets_arr = []
        ##insert the longest tweets text into arr
        for tweet_index in longest_antisemitic_tweets.index:
                antisemitic_tweets_arr.append(antisemitic_tweets[tweet_index])

        ## find the 3 longest non-antisemitic tweets
        non_antisemitic_tweets = self.df[self.df["Biased"] == 0]['Text']
        longest_non_antisemitic_tweets =  non_antisemitic_tweets.map(lambda x:len(x)).nlargest(3)
        non_antisemitic_tweets_arr = []
        ##insert the longest tweets text into arr
        for tweet_index in longest_non_antisemitic_tweets.index:
                non_antisemitic_tweets_arr.append(non_antisemitic_tweets[tweet_index])

        ## create the result dict
        result = {"antisemitic":antisemitic_tweets_arr,
                    "non_antisemitic":non_antisemitic_tweets_arr}
        return result

    def most_common_words(self):
        common_words = Counter(" ".join(self.df["Text"]).split()).most_common(10)
        common_words_arr = []
        for word in common_words:
            common_words_arr.append(word[0])
        result = {"total":common_words_arr}
        return result

    def uppercase_counter(self):
        """convert all the text in 'Text' column to a list if all the words"""
        words_arr = " ".join(self.df[self.df["Biased"]==1]["Text"]).split()
        """convert the word list to a pandas series"""
        words_series = pd.Series(words_arr)
        """filter the uppercase words into true and sum the trues"""
        antisemitic_uppercase_words = words_series.str.isupper().sum()

        """doing the same BUT on the non-antisemitic words"""
        non_antisemitic_words_arr = " ".join(self.df[self.df["Biased"] == 0]["Text"]).split()
        non_antisemitic_words_series = pd.Series(non_antisemitic_words_arr)
        non_antisemitic_uppercase_words = non_antisemitic_words_series.str.isupper().sum()

        result = {"antisemitic":antisemitic_uppercase_words,
                  "non_antisemitic":non_antisemitic_uppercase_words,
                  "total":antisemitic_uppercase_words+non_antisemitic_uppercase_words}

        return result

    def parse(self):
        total_tweets = self.count_classes()
        average_lengths = self.calculate_average_lengths(total_tweets)
        longest_3_tweets = self.longest_tweets()
        common_words = self.most_common_words()
        uppercase_words = self.uppercase_counter()
        print(uppercase_words)






