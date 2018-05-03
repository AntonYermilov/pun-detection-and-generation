# max number of senses

from util import morph, senses


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    max_senses = 1

    for word in words:
        for form in morph.parse(word):
            normal_form = form.normal_form
            if normal_form in senses:
                max_senses = max(max_senses, len(senses[normal_form]))

    return max_senses
