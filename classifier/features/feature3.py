# percentage of nouns

from util import morph


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    cnt = 0

    for word in words:
        is_noun = False
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            is_noun |= 'NOUN' == form.tag.POS
        if is_noun:
            cnt += 1

    return 1.0 * cnt / len(words)
