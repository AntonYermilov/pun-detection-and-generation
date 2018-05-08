from util.util import get_words
from util.special.lg_util import count_pair_relation


def get_score(text):
    """
    Counts antonyms in the given text.
    Relations from RuWordNet are used.
    :param text: string;
    :return: int.
    """
    words = get_words(text)
    return count_pair_relation(words, 'antonym')
