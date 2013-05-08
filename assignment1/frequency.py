"""
frequency.py -- Calculates term frequency
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


def term_frequency_count(tweets, normalize=normalize_word):
    tf = defaultdict(int)
    for tweet in tweets:
        for word in tweet.split():
            tf[normalize(word)] += 1
    return tf


def term_frequency_percentage(tweets, normalize=normalize_word):
    tfb = term_frequency_count(tweets, normalize)
    total_terms = sum(tfb.values())
    tf = {k: float(v) / total_terms for k, v in tfb.iteritems()}
    return tf


def main():

    tweets, sentiments = get_file_names(tweets='C:\Data\TwitterStream\output.txt')

    #calculate term frequency
    terms = term_frequency_percentage(read_tweet_text(tweets))

    #print results sorted
    for k in sorted(terms, key=terms.get, reverse=True)[:100]:
        print "{0} {1:.10f}".format(k, terms[k])

    print "{0} terms".format(len(terms))

if __name__ == '__main__':
    main()
