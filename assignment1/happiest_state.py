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

def read_tweet_text_state(tweet_filename):
    """
    read_tweets -- generator reads tweet json from file with one tweet per line
    """
    with open(tweet_filename, 'r') as tweet_file:
        for line in tweet_file:
            tweet_json = json.loads(line)
            text = ''
            state = ''
            #print json.dumps(tweet_json, indent=2)

            if 'text' in tweet_json:
                text = tweet_json['text']

            if 'place' in tweet_json:
                if tweet_json['place'] != None:
                    if tweet_json['place']['country_code'] == 'US':
                        state = tweet_json['place']['full_name'][-2:]

            if state != '':
                yield text.encode('utf-8'), state.encode('utf-8')


def state_tweet_sentiments(sent_filename, tweet_filename):
    """
    state_tweet_sentiments -- assigns sentiment score to tweet by summing sentiments
    """
    sentiments = load_sentiments(sent_filename)
    state_sentiments = {}
    for tweet, state in read_tweet_text_state(tweet_filename):
        score = calc_sentiment(tweet, sentiments)
        if state in state_sentiments:
            state_sentiments[state].append(score)
        else:
            state_sentiments[state] = [score]

    state_sentiment = {k: sum(v) / len(v) for k, v in state_sentiments.iteritems()}

    # print state_sentiments
    # print state_sentiment
    # for w in sorted(state_sentiment, key=state_sentiment.get, reverse=True):
    #     print w, state_sentiment[w]

    print sorted(state_sentiment, key=state_sentiment.get, reverse=True)[0]

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

    state_tweet_sentiments(sent_filename, tweet_filename)

if __name__ == '__main__':
    main()
