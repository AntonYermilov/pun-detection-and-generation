# percentage of nouns

from util.util import morph, get_words


def get_score(text):
    words = get_words(text)
    if len(words) == 0:
        return 0

    cnt = 0
    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if 'NOUN' == form.tag.POS:
                cnt += 1
                break
    return 1.0 * cnt / len(words)
