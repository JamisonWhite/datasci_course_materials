"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

import json
import csv
import sys


def count_hash_tags(tweet_filename):
    """
    read_tweets -- generator reads tweet json from file with one tweet per line
    """
    hash_counts = {}
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)

            if 'entities' not in tweet_json:
                continue
            if tweet_json['entities'] == None:
                continue
            if 'hashtags' not in tweet_json['entities']:
                continue
            if tweet_json['entities']['hashtags'] == None:
                continue
            if len(tweet_json['entities']['hashtags']) == 0:
                continue

            #print json.dumps(tweet_json, indent=2)

            for hashtagdict in tweet_json['entities']['hashtags']:
                hashtag = hashtagdict['text']
                if hashtag in hash_counts:
                    hash_counts[hashtag] += 1
                else:
                    hash_counts[hashtag] = 1


    return hash_counts

def print_hash_tags( tweet_filename):
    """
    print_hash_tags -- assigns sentiment score to tweet by summing sentiments
    """
    hashtags = count_hash_tags(tweet_filename)


    for k in sorted(hashtags, key=hashtags.get, reverse=True)[:10]:
        print k, hashtags[k]

def main():
    #get the args
    if len(sys.argv) >= 2:
        tweet_filename = sys.argv[1]
    else:
        tweet_filename = '../../data/ooutput.txt'


    print_hash_tags(tweet_filename)

if __name__ == '__main__':
    main()
