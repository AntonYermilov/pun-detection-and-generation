# percentage of stop-words

from util.util import morph, get_words

good_tags = {'PREP', 'CONJ', 'PRCL', 'INTJ'}


def get_score(text):
    words = get_words(text)
    if len(words) == 0:
        return 0

    cnt = 0
    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if form.tag.POS in good_tags:
                cnt += 1
                break
    return cnt / len(words)
