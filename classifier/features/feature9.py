# max word frequency (includes only nouns, verbs and adjectives and derived forms, uses ruscorpora text corpus)

from util import morph, frequencies


def satisfies(tag):
    for good_tag in {'NOUN', 'VERB', 'INFN', 'GRND',
                     'ADJF', 'ADJS', 'COMP', 'PRTF', 'PRTS', 'NUMR', 'ADVB', 'COMP'}:
        if good_tag == tag.POS:
            return True
    return False


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    max_frequency = 0

    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if not satisfies(form.tag):
                continue

            if form.normal_form in frequencies:
                max_frequency = max(max_frequency, frequencies[form.normal_form])

    return max_frequency
