# min word frequency (uses ruscorpora text corpus)

from util.util import morph, get_words
from util.special.ae_util import frequencies


def get_score(text):
    words = get_words(text)
    if len(words) == 0:
        return 0

    exists = False
    min_frequency = 0

    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if form.normal_form in frequencies:
                if not exists or frequencies[form.normal_form] < min_frequency:
                    exists = True
                    min_frequency = frequencies[form.normal_form]
            else:
                return 0

    return min_frequency
