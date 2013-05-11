"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

from assignment1_lib import *


def count_tweet_hashtags(tweets, normalize=normalize_default):
    hashtags = defaultdict(int)
    for tweet in tweets:
        #check for hashtags
        if 'entities' not in tweet:
            continue
        if tweet['entities'] == None:
            continue
        if 'hashtags' not in tweet['entities']:
            continue
        if tweet['entities']['hashtags'] == None:
            continue
        if len(tweet['entities']['hashtags']) == 0:
            continue

        for hashtag in tweet['entities']['hashtags']:
            hashtags[normalize(hashtag['text'])] += 1

    return hashtags


def main():

    tweets_file, sentiments_file = get_file_names()

    hashtags = count_tweet_hashtags(read_tweet_file(tweets_file, read_tweet_json))

    for k in sorted(hashtags, key=hashtags.get, reverse=True)[:100]:
        print k, hashtags[k]



if __name__ == '__main__':
    main()
