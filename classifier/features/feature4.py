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
            is_adjective |= 'ADJF' in form.tag or 'ADJS' in form.tag or 'COMP' in form.tag
        if is_adjective:
            cnt += 1

    return 1.0 * cnt / len(words)
