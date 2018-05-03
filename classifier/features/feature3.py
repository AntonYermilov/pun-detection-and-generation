# percentage of verbs

from util import morph


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    cnt = 0

    for word in words:
        is_verb = False
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            is_verb |= 'VERB' in form.tag or 'INFN' in form.tag or 'GRND' in form.tag
        if is_verb:
            cnt += 1

    return 1.0 * cnt / len(words)
