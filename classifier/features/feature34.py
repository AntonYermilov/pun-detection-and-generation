# existence of oppositional alliances

from util.util import get_words


def get_score(text):
    words = get_words(text)

    for alliance in ['а', 'но', 'да', 'зато', 'однако']:
        if alliance in words:
            return 1
    return 0
