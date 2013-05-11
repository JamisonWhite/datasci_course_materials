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


def normalize_default(text):
    try:
        return text.encode('utf-8')
    except UnicodeDecodeError:
        return ''


def normalize_lower(text):
    return normalize_default(text).lower()


def normalize_upper(text):
    return normalize_default(text).upper()

def normalize_strip_syntax(text):
    return re.sub('[^a-z0-9 -]', '', normalize_lower(text)) #from hjort


def normalize_strip_links(text):
    if re.search('[/:@]', text):
        return ''
    return re.sub('[^a-z0-9 -]', '', normalize_lower(text)) #from hjort


def read_tweet_json(tweet, normalize=normalize_default):
    return tweet


def read_tweet_text(tweet, normalize=normalize_default):
    text = ''
    if 'text' in tweet:
        text = tweet['text']
    return normalize(text)


def read_tweet_state(tweet, normalize=normalize_default):
    state = ''
    if 'place' in tweet:
        if tweet['place'] != None:
            if tweet['place']['country_code'] == 'US':
                state = tweet['place']['full_name'][-2:]
    return normalize(state)


def read_tweet_file(tweet_filename, tweet_reader=read_tweet_json, normalize=normalize_default):
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            yield tweet_reader(tweet_json, normalize)


def load_dict_from_file(filename, sep='\t', normalize=normalize_default):
    result = defaultdict(float)
    with open(filename, 'r') as f:
        for line in f:
            key, sep1, value = line.partition(sep)
            result[normalize(key)] = float(value)
    return result


def calc_sentiment(text, sentiments, normalize=normalize_default):
    return sum([sentiments[word] for word in [normalize(word1) for word1 in text.split()] if word in sentiments])

