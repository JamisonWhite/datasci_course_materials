"""
frequency.py -- Calculates term frequency
"""
__author__ = 'Jamison White'

import json
import csv
import sys


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


def frequency(tweet_filename):
    terms = {}
    for tweet in read_tweet_text(tweet_filename):
        for word in tweet.split():
            if word in terms:
                terms[word] += 1
            else:
                terms[word] = 1

    total_terms = float(len(terms))
    tf = {k: float(v) / total_terms for k, v in terms.iteritems()}

    for k, v in tf.iteritems():
        print "{0} {1:.4f}".format(k, v)


def main():
    #get the args
    if len(sys.argv) >= 2:
        tweet_filename = sys.argv[1]
    else:
        tweet_filename = 'output.txt'
    frequency(tweet_filename)

if __name__ == '__main__':
    main()
