"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

from assignment1_lib import *


def read_tweet_text_state(tweet, normalize=normalize_default):
    text = ''
    state = ''

    if 'text' in tweet:
        text = tweet['text']

    if 'place' in tweet:
        if tweet['place'] != None:
            if tweet['place']['country_code'] == 'US':
                state = tweet['place']['full_name'][-2:]

    return normalize(text), normalize(state)


def state_sentiments(tweets, sentiments, normalize=normalize_default):
    states = defaultdict(list)
    for tweet in tweets:
        text, state = read_tweet_text_state(tweet, normalize)
        states[state].append(calc_sentiment(text, sentiments))

    states = {k: sum(v) / len(v) for k, v in states.iteritems()}
    return states


def main():

    tweets_file, sentiments_file = get_file_names()

    sentiments = load_dict_from_file(sentiments_file)

    states = state_sentiments(read_tweet_json(tweets_file), sentiments)

    for k in sorted(states, key=states.get, reverse=True)[:100]:
        print k, states[k]



if __name__ == '__main__':
    main()
