"""
assignment1-lib -- shared methods used by problems
"""
__author__ = 'Jamison White'

import sys
import json
import re
from collections import defaultdict


def get_file_names(tweets='../../data/output.txt', sentiments='../../data/AFINN-111.txt'):
    """
    get_file_names -- gets file names based on assignment 1 instructions.
    I think the order is backwards and that tweet file should have come first.
    """
    if len(sys.argv) >= 3:
        sentiments = sys.argv[1]
        tweets = sys.argv[2]
    elif len(sys.argv) >= 2:
        tweets = sys.argv[1]
    return tweets, sentiments


def normalize_word(word):
    return word
    # return word.lower()
    #return re.sub('[^a-z0-9 -]', '', word.lower()) #from hjort


def normalize_tweet(tweet):
    return tweet.encode('utf-8')


def read_tweet_text(tweet_filename, normalize=normalize_tweet):
    """
    read_tweets -- generator reads tweet json from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            if 'text' in tweet_json:
                text = tweet_json['text']
                yield normalize(text)


def load_dict_from_file(filename, sep='\t', normalize=normalize_word):
    result = defaultdict(float)
    with open(filename, 'r') as f:
        for line in f:
            key, sep1, value = line.partition(sep)
            result[normalize(key)] = float(value)
    return result


def calc_sentiment(text, sentiments):
    return sum([sentiments[word] for word in text.split() if word in sentiments])

