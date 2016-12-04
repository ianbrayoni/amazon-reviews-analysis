# coding=utf-8
# from django.shortcuts import render

import nltk
# import cPickle
# from django.db import connection
# from django.conf import settings
from .models import TrainData


def pre_process_manually_trained_data():
    """
    Fetch all trained data from the database
    and create a list of tuples(words, sentiment)
    :return: list of tuples(words, sentiment)
    """
    # cursor = connection.cursor()
    # cursor.execute("select t2.review_text, t1.sentiment "
    #                "from classifier_labeleddata t2 "
    #                "inner join classifier_sentiment t1 "
    #                "on t2.sentiment_id = t1.id")
    # labeled_data = cursor.fetchall()
    train_data = list(
        TrainData.objects.values('sentiment__sentiment', 'review_text'))

    pre_processed_data = []

    for data in train_data:
        words = data.get('review_text')
        sentiment = data.get('sentiment__sentiment')
        pre_processed_data.append((words, sentiment))

    # a single list of tuples each containing two elements.
    # First element is an array containing the words and second element
    # is the type of sentiment.
    # We get rid of the words smaller than 2 characters
    # and we use lowercase for everything.
    processed_data = []

    for (words, sentiment) in pre_processed_data:
        words_filtered = [word.lower() for word in words.split()
                          if len(word) >= 3]
        processed_data.append((words_filtered, sentiment))

    return processed_data


def get_all_words_from_reviews(reviews):
    """
    Extract all words from reviews

    :param reviews: text to be assessed
    :return: list of words
    """
    all_words = []
    for (words, sentiment) in reviews:
        all_words.extend(words)
    return all_words


def get_word_features_by_freq_dist(wordlist):
    """
    Function creates a list from a list with every distinct word ordered
    by frequency of appearance.

    Sample wordlist

    <FreqDist:
    'this': 6,
    'car': 2,
    'concert': 2,
    'feel': 2,
    'morning': 2,
    'not': 2,
    'the': 2,
    'view': 2,
    'about': 1,
    'amazing': 1,
    ...
    >

    We shall end up with the following list of wordfeatures

    word_features = [
    'this',
    'car',
    'concert',
    'feel',
    'morning',
    'not',
    'the',
    'view',
    'about',
    'amazing',
    ...
    ]

    :param wordlist: list of words ordered by frequency of appearance
    :return: list of words

    """
    wordlist = nltk.FreqDist(wordlist)
    wordfeatures = wordlist.keys()
    return wordfeatures

# List of word features
word_features = get_word_features_by_freq_dist(
        get_all_words_from_reviews(pre_process_manually_trained_data())
    )


def extract_word_features(document):
    """
    This is a feature extractor
     Input: Sample document
        [‘love’, ‘this’, ‘car’]

     Output :
        {'contains(not)': False,
         'contains(view)': False,
         'contains(best)': False,
         'contains(excited)': False,
         'contains(morning)': False,
         'contains(about)': False,
         'contains(horrible)': False,
         'contains(like)': False,
         'contains(this)': True,
         'contains(friend)': False,
         'contains(concert)': False,
         'contains(feel)': False,
         'contains(love)': True,
         'contains(looking)': False,
         'contains(tired)': False,
         'contains(forward)': False,
         'contains(car)': True,
         'contains(the)': False,
         'contains(amazing)': False,
         'contains(enemy)': False,
         'contains(great)': False}

    :param document: list of words
    :return: a dictionary indicating what words are
        contained in the input passed
    """
    document_words = set(document)
    features = {}
    for word in word_features:
        features['contains (%s)' % word] = (word in document_words)
    return features


# apply the features to our classifier using the method `apply_features`
# The variable ‘training_set’ contains the labeled feature sets. It is
# a list of tuples which each tuple containing the feature
# dictionary and the sentiment string for each tweet.
# The sentiment string is also called ‘label’ e.g

# [({'contains(not)': False,
#    ...
#    'contains(this)': True,
#    ...
#    'contains(love)': True,
#    ...
#    'contains(car)': True,
#    ...
#    'contains(great)': False},
#   'positive'),
#  ({'contains(not)': False,
#    'contains(view)': True,
#    ...
#    'contains(this)': True,
#    ...
#    'contains(amazing)': True,
#    ...
#    'contains(enemy)': False,
#    'contains(great)': False},
#   'positive'),
#   ...]

training_set = nltk.classify.apply_features(
    extract_word_features, pre_process_manually_trained_data())


# train our classifier.
# classifier = nltk.NaiveBayesClassifier.train(training_set)

# save classifier object to avoid retraining
# save_classifier = open(settings.CLASSIFIER_OBJECT, "wb")
# cPickle.dump(classifier, save_classifier)
# save_classifier.close()

# Take it for a spin
# from review_analysis.apps.classifier.views import classifier
# review = 'Larry is my friend'
# print classifier.classify(extract_word_features(review.split()))
# positive


















