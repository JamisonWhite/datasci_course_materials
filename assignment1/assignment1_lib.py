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
        return text


def normalize_lower(text):
    return normalize_default(text).lower()


def normalize_strip_syntax(text):
    return re.sub('[^a-z0-9 -]', '', normalize_lower(text)) #from hjort

def normalize_strip_links(text):
    if re.search('[/:@]', text):
        return ''
    return re.sub('[^a-z0-9 -]', '', normalize_lower(text)) #from hjort



def read_tweet_json(tweet_filename):
    """
    read_tweet_json -- generator returns tweet json from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            yield tweet_json


def read_tweet_text(tweet_filename, normalize=normalize_default):
    """
    read_tweet_text -- generator reads tweet text from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            if 'text' in tweet_json:
                text = tweet_json['text']
                yield normalize(text)


def load_dict_from_file(filename, sep='\t', normalize=normalize_default):
    result = defaultdict(float)
    with open(filename, 'r') as f:
        for line in f:
            key, sep1, value = line.partition(sep)
            result[normalize(key)] = float(value)
    return result


def calc_sentiment(text, sentiments):
    return sum([sentiments[word] for word in text.split() if word in sentiments])

