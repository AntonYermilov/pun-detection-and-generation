# amount of words before first comma

from util.util import get_words


def get_score(text):
    total = len(get_words(text))
    if total == 0:
        return 0

    before = len(get_words(text.split(',')[0]))
    return before / max(1, total)
