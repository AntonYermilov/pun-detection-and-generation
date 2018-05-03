# min word frequency (uses ruscorpora text corpus)

from util import morph, frequencies


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.lower().replace(text[i], ' ')

    words = text.split()
    min_frequency = 1e9

    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if form.normal_form in frequencies:
                min_frequency = min(min_frequency, frequencies[form.normal_form])
            else:
                return 0

    return min_frequency
