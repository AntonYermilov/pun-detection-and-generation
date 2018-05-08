# min amount of syllables in word

from util.special.nm_util import get_syllables_counts


def get_score(text):
    syllables = get_syllables_counts(text)
    if len(syllables) == 0:
        return 0
    return max(syllables)
