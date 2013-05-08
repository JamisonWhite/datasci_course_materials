"""
term_sentiment.py -- Assigns a sentiment score to unscored terms based on tweet sentiment.
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
    read_tweet_text -- generator reads tweet json from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            if 'text' in tweet_json:
                text = tweet_json['text']
                yield text.encode('utf-8')


def term_sentiment(sent_filename, tweet_filename):
    """
    term_sentiment -- assigns sentiment score to tweet by summing sentiments
    """
    sentiments = load_sentiments(sent_filename)

    new_terms = {}

    for tweet in read_tweet_text(tweet_filename):
        tweet_score = calc_sentiment(tweet, sentiments)

        tweet_new_terms = [word for word in tweet.split() if word not in sentiments]

        for word in tweet_new_terms:
            if word in new_terms:
                new_terms[word].append(tweet_score)
            else:
                new_terms[word] = [tweet_score]

    terms = {k: sum(v) / len(v) for k, v in new_terms.iteritems()}
    for k, v in terms.iteritems():
        print "{0} {1:.4f}".format(k, v)


def main():
    #get the args
    if len(sys.argv) >= 2:
        sent_filename = sys.argv[1]
    else:
        sent_filename = '../../data/oAFINN-111.txt'

    if len(sys.argv) >= 3:
        tweet_filename = sys.argv[2]
    else:
        tweet_filename = '../../data/ooutput.txt'

    #term_sentiment(sent_filename, tweet_filename)
    term_sentiment(sent_filename, tweet_filename)

if __name__ == '__main__':
    main()
