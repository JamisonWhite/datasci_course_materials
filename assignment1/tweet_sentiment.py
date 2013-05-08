"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

from assignment1_lib import *


def main():

    #tweets_file, sentiments_file = get_file_names()
    tweets_file, sentiments_file = get_file_names(tweets='C:\Data\TwitterStream\output.txt', sentiments='AFINN-111.txt')

    sentiments = load_dict_from_file(sentiments_file)

    for tweet in read_tweet_text(tweets_file):
        print calc_sentiment(tweet, sentiments)


if __name__ == '__main__':
    main()
