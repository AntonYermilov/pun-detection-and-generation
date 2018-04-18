#!/usr/bin/python3

import dataloader
import random
import feature1
import numpy as np


def load():
    jokes = dataloader.load_jokes()
    news = dataloader.load_news()
    random.shuffle(jokes)
    random.shuffle(news)

    size = min(len(jokes), len(news))
    learn_size = int(0.95 * size)

    return jokes[:learn_size], news[:learn_size], jokes[learn_size:size], news[learn_size:size]


def count_accuracy(jokes_scores, news_scores, threshold):
    pos_true, neg_true = 0, 0
    pos_true += len(jokes_scores) - np.searchsorted(jokes_scores, threshold)
    neg_true += np.searchsorted(news_scores, threshold)
    return pos_true / len(jokes_scores)


def count_completeness(jokes_scores, news_scores, threshold):
    pos_true, neg_true = 0, 0
    pos_true += len(jokes_scores) - np.searchsorted(jokes_scores, threshold)
    neg_true += len(news_scores) - np.searchsorted(news_scores, threshold)
    return pos_true / (pos_true + neg_true)


def count_measure(jokes_scores, news_scores, threshold, alpha):
    accuracy = count_accuracy(jokes_scores, news_scores, threshold)
    completeness = count_completeness(jokes_scores, news_scores, threshold)
    return 1 / (alpha / accuracy + (1 - alpha) / completeness)


def learn(jokes, news):
    jokes_scores = np.array([feature1.get_score(text) for text in jokes])
    news_scores = np.array([feature1.get_score(text) for text in news])
    jokes_scores.sort()
    news_scores.sort()

    threshold, opt_threshold, opt_score = -1, -1, 0
    step = 0.001
    while threshold < 1:
        score = count_measure(jokes_scores, news_scores, threshold, 0.44)
        if score > opt_score:
            opt_threshold = threshold
            opt_score = score
        threshold += step
    return opt_threshold


def test(jokes, news, threshold):
    jokes_scores = np.array([feature1.get_score(text) for text in jokes])
    news_scores = np.array([feature1.get_score(text) for text in news])
    jokes_scores.sort()
    news_scores.sort()

    measure = count_measure(jokes_scores, news_scores, threshold, 0.44)
    accuracy = count_accuracy(jokes_scores, news_scores, threshold)
    completeness = count_completeness(jokes_scores, news_scores, threshold)
    with open('feature1_results.txt', 'w') as output:
        output.write('measure=' + str(measure) + ', accuracy=' + str(accuracy)
                     + ', completeness=' + str(completeness) + '\n\n')

        output.write('Positive true:\n')
        for text, score in zip(jokes, jokes_scores):
            if score > threshold:
                output.write(text + '\n')

        output.write('Positive false:\n')
        for text, score in zip(jokes, jokes_scores):
            if score < threshold:
                output.write(text + '\n')

        output.write('Negative true:\n')
        for text, score in zip(news, news_scores):
            if score > threshold:
                output.write(text + '\n')

        output.write('Negative false:\n')
        for text, score in zip(news, news_scores):
            if score < threshold:
                output.write(text + '\n')


def main():
    jokes_learn, news_learn, jokes_test, news_test = load()
    print('Data loaded')
    opt_threshold = learn(jokes_learn, news_learn)
    print('Classifier trained')
    test(jokes_test, news_test, opt_threshold)
    print('Results saved')


if __name__ == '__main__':
    main()
