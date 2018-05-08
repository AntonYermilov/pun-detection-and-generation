# min dist between commas

from util.special.nm_util import get_word_part_lengths


def get_score(text):
    lengths = get_word_part_lengths(text)
    if len(lengths) == 0:
        return 0
    return min(lengths)
