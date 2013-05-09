"""
term_sentiment.py -- Assigns a sentiment score to unscored terms based on tweet sentiment.
"""
__author__ = 'Jamison White'

from assignment1_lib import *
from collections import defaultdict


def assign_new_term_sentiment(tweets, sentiments, normalize=normalize_default):
    terms = defaultdict(list)
    for tweet in tweets:
        tweet_score = calc_sentiment(tweet, sentiments)
        new_words = [word for word in [normalize(word) for word in tweet.split()] if word not in sentiments]
        for word in new_words:
            terms[word].append(tweet_score)
    terms = {k: float(sum(v)) / float(len(v)) for k, v in terms.iteritems()}
    return terms


def main():

    tweets_file, sentiments_file = get_file_names()
    #tweets_file, sentiments_file = get_file_names(tweets='C:\Data\TwitterStream\output.txt', sentiments='AFINN-111.txt')

    sentiments = load_dict_from_file(sentiments_file)

    tweets = read_tweet_text(tweets_file)

    terms = assign_new_term_sentiment(tweets, sentiments) #, normalize_strip_links)

    # #all
    # for k in sorted(terms, key=terms.get, reverse=True):
    #     print "{0} {1:.4f}".format(k, terms[k])

    #print "---------- TOP -------------"
    for k in sorted(terms, key=terms.get, reverse=True)[:50]:
        print "{0} {1:.4f}".format(k, terms[k])

    #print "---------- BOTTOM -------------"
    for k in sorted(terms, key=terms.get, reverse=True)[-50:]:
        print "{0} {1:.4f}".format(k, terms[k])


if __name__ == '__main__':
    main()
