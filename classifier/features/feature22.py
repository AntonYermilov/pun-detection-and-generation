# sum of senses in the first half of the text

from util import morph, senses
from math import log


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    sum_senses = 0

    for word in words[:len(words) / 2]:
        max_senses = 1
        for form in morph.parse(word):
            normal_form = form.normal_form
            if normal_form in senses:
                max_senses = max(max_senses, len(senses[normal_form]))
        sum_senses += log(max_senses)

    return sum_senses

