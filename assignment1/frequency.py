"""
frequency.py -- Calculates term frequency
"""
__author__ = 'Jamison White'

from collections import defaultdict
from assignment1_lib import *

def term_frequency_count(tweets, normalize=normalize_default):
    tf = defaultdict(int)
    for tweet in tweets:
        for word in tweet.split():
            tf[normalize(word)] += 1
    return tf


def term_frequency_percentage(tweets, normalize=normalize_default):
    tfb = term_frequency_count(tweets, normalize)
    total_terms = sum(tfb.values())
    tf = {k: float(v) / total_terms for k, v in tfb.iteritems()}
    return tf

def main():

    tweets_file, sentiments_file = get_file_names()
    #tweets_file, sentiments_file = get_file_names(tweets='C:\Data\TwitterStream\output.txt')

    terms = term_frequency_percentage(read_tweet_file(tweets_file, read_tweet_text, normalize_default))

    for k in sorted(terms, key=terms.get, reverse=True):
        print "{0} {1:.10f}".format(k, terms[k])

    #print "{0} terms".format(len(terms))

if __name__ == '__main__':
    main()
