# normalized sum of word vectors

from util import wv, morph, TAGS


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    # TODO

    return 0
