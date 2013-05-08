"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

import json
import csv
import sys

def load_sentiments(sent_filename):
    """
    load_sentiments -- loads TSV file of term and score file.
    """
    sentiments = {}
    with open(sent_filename, 'r') as sent_file:
        reader = csv.reader(sent_file , dialect='excel-tab')
        for line in reader:
            sentiments[line[0]] =  float(line[1])
    return sentiments

def calc_sentiment(text, sentiments):
    return sum([sentiments[word] for word in text.split(' ') if word in sentiments])

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


def print_tweet_sentiments(sent_filename, tweet_filename):
    """
    print_tweet_sentiments -- assigns sentiment score to tweet by summing sentiments
    """
    sentiments = load_sentiments(sent_filename)
    for tweet in read_tweet_text(tweet_filename):
        print calc_sentiment(tweet, sentiments)



def main():
    #get the args
    if len(sys.argv) >= 2:
        sent_filename = sys.argv[1]
    else:
        sent_filename = 'AFINN-111.txt'

    if len(sys.argv) >= 3:
        tweet_filename = sys.argv[2]
    else:
        tweet_filename = 'output.txt'

    #tweet_sentiment(sent_filename, tweet_filename)
    print_tweet_sentiments(sent_filename, tweet_filename)

if __name__ == '__main__':
    main()
