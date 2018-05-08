# amount of introductory words

from util.util import get_honest_words
from util.special.nm_util import introductory_words_set


def get_score(text):
    words = get_honest_words(text)
    count = 0

    for i in range(0, len(words)):
        if words[i] in introductory_words_set:
            count += 1
    for i in range(0, len(words) - 1):
        if str(words[i] + ' ' + words[i + 1]) in introductory_words_set:
            count += 2
    for i in range(0, len(words) - 2):
        if str(words[i] + ' ' + words[i + 1] + ' ' + words[i + 2]) in introductory_words_set:
            count += 3

    return count / max(1, len(words))
