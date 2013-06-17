"""
yelp01.py --
"""
__author__ = 'Jamison White'

from assignment1_lib import *
import csv

def process_review(review_file, sentiments):
    for review in read_tweet_file(review_file):
        #print(review)
        row = []
        row.append(review['stars'])
        row.append(calc_sentiment( review['text'], sentiments))
        row.append(review['votes']['cool'])
        row.append(review['votes']['funny'])
        row.append(review['votes']['useful'])
        #todo user review_count, averate_stars, votes
        #todo busness city, starts, reviews, name sent
        yield row


def main():

    sentiments = load_dict_from_file( './AFINN-111.txt')
    review_file = '../../data/yelp_recruiting/training/yelp_training_set_review.json'

    # rows = 0
    # for review in process_review(review_file, sentiments):
    #     print review
    #     rows = rows + 1
    #     if rows > 100:
    #         break

    rows = 0
    with open('reviews.csv', 'w+') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['review_stars', 'review_sentiment', 'review_cool', 'review_funny', 'review_useful'])
        for review in process_review(review_file, sentiments):
            csvwriter.writerow(review)
            rows = rows + 1
        csvfile.close()








    # sentiments = load_dict_from_file(sentiments_file)
    #
    # for tweet in read_tweet_file(tweets_file, get_tweet_text, normalize_default):
    #     print calc_sentiment(tweet, sentiments)


if __name__ == '__main__':
    main()
