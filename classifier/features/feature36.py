from util.util import get_words
from util.special.lg_util import norm_forms, collect_by_relation


def get_score(text):
    """
    Counts domains in the given text.
    Relations from RuWordNet are used.
    :param text: string;
    :return: int.
    """
    words = get_words(text)
    domains_in_text = set()
    for word in words:
        norms = norm_forms(word)
        word_domains = collect_by_relation(norms, 'domain')
        if word_domains:
            domains_in_text.update(word_domains)
    return len(domains_in_text)
