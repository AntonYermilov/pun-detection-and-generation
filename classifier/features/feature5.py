# percentage of participles

from util import morph


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    cnt = 0

    for word in words:
        is_participle = False
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            is_participle |= 'PRTF' in form.tag or 'PRTS' in form.tag
        if is_participle:
            cnt += 1

    return 1.0 * cnt / len(words)
