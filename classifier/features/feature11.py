# max number of senses

from util.util import morph, get_words
from util.special.ae_util import senses


def get_score(text):
    words = get_words(text)
    max_senses = 1

    for word in words:
        for form in morph.parse(word):
            normal_form = form.normal_form
            if form.tag.POS == 'NOUN' and normal_form in senses:
                max_senses = max(max_senses, len(senses[normal_form]))

    return max_senses
