# average word length

from util.util import get_words


def get_score(text):
    words = get_words(text)
    if len(words) == 0:
        return 0

    length = sum(map(len, words))
    return length / len(words)
