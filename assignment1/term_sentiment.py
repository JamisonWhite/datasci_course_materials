"""
term_sentiment.py -- Assigns a sentiment score to unscored terms based on tweet sentiment.
"""
__author__ = 'Jamison White'

from assignment1_lib import *
from collections import defaultdict


def assign_new_term_sentiment(tweets, sentiments, normalize=normalize_word):
    new_terms = defaultdict(list)
    for tweet in tweets:
        tweet_score = calc_sentiment(tweet, sentiments)
        new_words = [word for word in [normalize(word) for word in tweet.split()] if word not in sentiments]
        for word in new_words:
            new_terms[word].append(tweet_score)
    for k, v in new_terms.iteritems():
        new_terms[k] = float(sum(v)) / float(len(v))
    return new_terms


def main():

    #tweets_file, sentiments_file = get_file_names()
    tweets_file, sentiments_file = get_file_names(tweets='C:\Data\TwitterStream\output.txt', sentiments='AFINN-111.txt')

    sentiments = load_dict_from_file(sentiments_file)

    tweets = read_tweet_text(tweets_file)

    new_terms = assign_new_term_sentiment(tweets, sentiments)

    #all
    for k in sorted(new_terms, key=new_terms.get, reverse=True):
        print "{0} {1:.4f}".format(k, new_terms[k])

    # #top
    # print "---------- TOP -------------"
    # for k in sorted(terms, key=terms.get, reverse=True)[:10]:
    #     print "{0} {1:.4f}".format(k, terms[k])
    #
    # #bottom
    # print "---------- BOTTOM -------------"
    # for k in sorted(terms, key=terms.get, reverse=True)[-10:]:
    #     print "{0} {1:.4f}".format(k, terms[k])


if __name__ == '__main__':
    main()
