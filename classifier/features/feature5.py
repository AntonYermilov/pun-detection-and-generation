# percentage of adjectives

from util import morph


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    cnt = 0

    for word in words:
        is_adjective = False
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            is_adjective |= 'ADJF' == form.tag.POS or 'ADJS' == form.tag.POS or 'COMP' == form.tag.POS
        if is_adjective:
            cnt += 1

    return 1.0 * cnt / len(words)
