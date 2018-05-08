# existence of numerals

from util.util import get_words


def get_score(text):
    words = get_words(text)

    for word in words:
        if word.isnumeric():
            return 1
    return 0
