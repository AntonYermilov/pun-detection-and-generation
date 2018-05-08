# existence of conditions

from util.util import get_words


def get_score(text):
    words = get_words(text)
    return int('если' in words or 'когда' in words)
