"""
yelp01.py --

CSV Format

business_id
business_review_count
business_stars
user_id
user_review_count
user_average_stars
review_id
review_stars
review_sentiment
review_useful
"""
__author__ = 'Jamison White'

from assignment1_lib import *
import csv
import math


def get_businesses(business_file):
    businesses = {}
    with open(business_file, 'r') as bf:
        for line in bf:
            b = json.loads(line)
            businesses[b['business_id']] = b
    return businesses


def get_users(user_file):
    users = {}
    with open(user_file, 'r') as uf:
        for line in uf:
            u = json.loads(line)
            users[u['user_id']] = u
    return users


def process_review(review_file, user_file, business_file, sentiments):

    businesses = get_businesses(business_file)
    users = get_users(user_file)

    for review in read_tweet_file(review_file):
        #print(review)
        row = []

        #look up business
        business_id = review['business_id']
        row.append(business_id)
        if business_id in businesses:
            row.append(businesses[business_id]['review_count'])
            row.append(businesses[business_id]['stars'])
        else:
            row.append(0)
            row.append(0)

        #look up user
        user_id = review['user_id']
        row.append(user_id)
        if user_id in users:
            row.append(users[user_id]['review_count'])
            row.append(users[user_id]['average_stars'])
        else:
            row.append(0)
            row.append(0)

        row.append(review['review_id'])
        row.append(review['stars'])
        row.append(calc_sentiment(review['text'], sentiments))
        if 'votes' in review:
            row.append(review['votes']['useful'])
        else:
            row.append('?')
        yield row


def create_review_csv_file(review_file, user_file, business_file, output_file, sentiments, process_review_func = process_review):
    rows = 0
    with open(output_file, 'wb+') as output:
        csvwriter = csv.writer(output, delimiter=',', quotechar='"', dialect='excel', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(['business_id','business_review_count', 'business_stars', 'user_id', 'user_review_count', 'user_average_stars', 'review_id', 'review_stars', 'review_sentiment', 'review_useful'])
        for review in process_review_func(review_file, user_file, business_file, sentiments):
            csvwriter.writerow(review)
            rows += 1
        output.close()

def create_predictions_csv_file(input_file, output_file):
    """
    Linear Regression Model
    review_useful =
      0.0004 * business_review_count +
      0.0921 * business_stars +
      0.0034 * user_review_count +
     -0.0668 * user_average_stars +
     -0.1192 * review_stars +
      0.0333 * review_sentiment +
      1.0156
    """
    rows = 0
    with open(input_file, 'r+') as input:
        csvreader = csv.reader(input, delimiter=',', quotechar='"', dialect='excel')
        with open(output_file, 'wb+') as output:
            csvwriter = csv.writer(output, delimiter=',', quotechar='"', dialect='excel', quoting=csv.QUOTE_MINIMAL)
            csvwriter.writerow(['id', 'votes'])
            next(csvreader, None) #skip headers
            for row in csvreader:
                review_id = row[6]
                business_review_count = float(row[1])
                business_stars = float(row[2])
                user_review_count = float(row[4])
                user_average_stars = float(row[5])
                review_stars = float(row[7])
                review_sentiment = float(row[8])

                review_useful = (
                    0.0004 * business_review_count +
                    0.0921 * business_stars +
                    0.0034 * user_review_count +
                    -0.0668 * user_average_stars +
                    -0.1192 * review_stars +
                    0.0333 * review_sentiment +
                    1.0156
                )
                if review_useful < 0.0:
                    review_useful = 0.0
                csvwriter.writerow([review_id, math.ceil(review_useful)])
                rows += 1
            output.close()


def main():

    # sentiments = load_dict_from_file('./AFINN-111.txt')
    # review_file = '../../data/yelp_recruiting/training/yelp_training_set_review.json'
    sentiments = load_dict_from_file('.\\AFINN-111.txt')

    # #create training file
    # training_review_file = 'C:\\Data\\yelp_recruiting\\training\\yelp_training_set_review.json'
    # training_user_file = 'C:\\Data\\yelp_recruiting\\training\\yelp_training_set_user.json'
    # training_business_file = 'C:\\Data\\yelp_recruiting\\training\\yelp_training_set_business.json'
    # create_review_csv_file(training_review_file, training_user_file, training_business_file,
    #                        'review_training.csv', sentiments, process_review)

    # #create test file
    # test_review_file = 'C:\\Data\\yelp_recruiting\\test\\yelp_test_set_review.json'
    # test_user_file = 'C:\\Data\\yelp_recruiting\\test\\yelp_test_set_user.json'
    # test_business_file = 'C:\\Data\\yelp_recruiting\\test\\yelp_test_set_business.json'
    # create_review_csv_file(test_review_file, test_user_file, test_business_file,
    #                        'review_test.csv', sentiments, process_review)

    #create prediction file
    create_predictions_csv_file('review_test.csv', 'predictions.csv')


if __name__ == '__main__':
    main()
