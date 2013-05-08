"""
frequency.py -- Calculates term frequency
"""
__author__ = 'Jamison White'

import json
import sys
from collections import defaultdict

def read_tweet_text(tweet_filename):
    """
    read_tweets -- generator reads tweet json from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            if 'text' in tweet_json:
                text = tweet_json['text']
                yield text.encode('utf-8')


def term_frequency_boolean(tweets):
    tf = defaultdict(int)
    for tweet in tweets:
        for word in tweet.split():
            tf[word] += 1
    return tf


def term_frequency_percentage(tweets):
    tfb = term_frequency_boolean(tweets)
    total_terms = sum(tfb.values())
    tf = {k: float(v) / total_terms for k, v in tfb.iteritems()}
    return tf


def main():
    #get the args
    if len(sys.argv) >= 2:
        tweet_filename = sys.argv[1]
    else:
        tweet_filename = '../../data/output.txt'

    #calculate term frequency
    terms = term_frequency_percentage(read_tweet_text(tweet_filename))

    #print results sorted
    for k in sorted(terms, key=terms.get, reverse=True):
        print "{0} {1:.10f}".format(k, terms[k])


if __name__ == '__main__':
    main()
