# max word frequency (includes only nouns, verbs and adjectives and derived forms, uses ruscorpora text corpus)

from util.util import morph, get_words
from util.special.ae_util import frequencies

good_tags = {'NOUN', 'VERB', 'INFN', 'GRND', 'ADJF', 'ADJS', 'COMP', 'PRTF', 'PRTS', 'NUMR', 'ADVB', 'COMP'}


def get_score(text):
    words = get_words(text)
    max_frequency = 0

    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if form.tag.POS not in good_tags:
                continue

            if form.normal_form in frequencies:
                max_frequency = max(max_frequency, frequencies[form.normal_form])

    return max_frequency
