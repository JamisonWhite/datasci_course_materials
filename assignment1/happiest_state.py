"""
tweet_sentiment.py -- Assigns a sentiment score to all tweets.
"""
__author__ = 'Jamison White'

from assignment1_lib import *



def state_sentiments(tweets, sentiments, normalize=normalize_default):
    states = defaultdict(list)
    for tweet in tweets:
        text = read_tweet_text(tweet, normalize)
        state = read_tweet_state(tweet, normalize).upper()
        if state != '':
            states[state].append(calc_sentiment(text, sentiments, normalize))
    return {k: sum(v) / len(v) for k, v in states.iteritems()}


def main():

    tweets_file, sentiments_file = get_file_names()

    sentiments = load_dict_from_file(sentiments_file)

    states = state_sentiments(read_tweet_file(tweets_file), sentiments, normalize_default)

    for k in sorted(states, key=states.get, reverse=True):
        print k, states[k]



if __name__ == '__main__':
    main()
