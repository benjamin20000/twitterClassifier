from collections import Counter
import pandas as pd

class Parser:
    def __init__(self ,df):
        self.df = df

    def count_classes(self):
        target_counts = self.df.value_counts("Biased")
        total =  target_counts[0] + target_counts[1]
        unspecified = len(self.df) - total
        result = {"antisemitic": target_counts[1],
                    "non_antisemitic":target_counts[0],
                    "total":total,
                    "unspecified": unspecified}
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

    def calculate_target_longest_tweets(self, target)->list:
        ## find the 3 longest antisemitic tweets
        tweets = self.df[self.df["Biased"] == target]['Text']
        longest_antisemitic_tweets = tweets.map(lambda x: len(x)).nlargest(3)
        longest_tweets_arr = []

        ##insert the longest tweets text into arr
        for tweet_index in longest_antisemitic_tweets.index:
            longest_tweets_arr.append(tweets[tweet_index])
        return longest_tweets_arr

    def longest_tweets(self):
        antisemitic_tweets_arr = self.calculate_target_longest_tweets(1)
        non_antisemitic_tweets_arr = self.calculate_target_longest_tweets(0)

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

    def count_uppercase_by_target(self, target):
        """convert all the text in 'Text' column to a list if all the words"""
        words_arr = " ".join(self.df[self.df["Biased"] == target]["Text"]).split()
        """convert the word list to a pandas series"""
        words_series = pd.Series(words_arr)
        """filter the uppercase words into true and sum the trues"""
        uppercase_words_sum = words_series.str.isupper().sum()
        return uppercase_words_sum

    def uppercase_counter(self):
        """calling count_uppercase_by_target on the 1 - antisemitic
         and on 0 - non_antisemitic,
        to compare tweets on their usage of UPPERCASE WORDS"""
        antisemitic_uppercase_words = self.count_uppercase_by_target(1)
        non_antisemitic_uppercase_words = self.count_uppercase_by_target(0)

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
        result = {"total_tweets":total_tweets,
                  "average_lengths":average_lengths,
                  "longest_3_tweets":longest_3_tweets,
                  "common_words":common_words,
                  "uppercase_words":uppercase_words}
        return result






