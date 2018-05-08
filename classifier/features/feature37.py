from util.util import get_words
from util.special.lg_util import norm_forms, collect_by_relation


def get_score(text):
    """
    Counts words with multiple domain;
    Relations from RuWordNet are used.
    :param text: string;
    :return: int.
    """
    words = get_words(text)
    words_with_multiple_domain = 0
    for word in words:
        norms = norm_forms(word)
        if norms and len(collect_by_relation(norms, 'domain')) > 1:
            words_with_multiple_domain += 1
    return words_with_multiple_domain
