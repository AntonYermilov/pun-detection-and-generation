# sum of verb senses

from util.util import morph, get_words
from util.special.ae_util import senses, get_pos_tag
from math import log


def get_score(text):
    words = get_words(text)

    sum_senses_left = 0
    for word in words[:len(words) // 2]:
        max_senses = 1
        for form in morph.parse(word):
            normal_form = form.normal_form
            if get_pos_tag(normal_form) == 'INFN' and normal_form in senses:
                max_senses = max(max_senses, len(senses[normal_form]))
        sum_senses_left += log(max_senses)

    sum_senses_right = 0
    for word in words[len(words) // 2:]:
        max_senses = 1
        for form in morph.parse(word):
            normal_form = form.normal_form
            if get_pos_tag(normal_form) == 'INFN' and normal_form in senses:
                max_senses = max(max_senses, len(senses[normal_form]))
        sum_senses_right += log(max_senses)

    return [sum_senses_left + sum_senses_right, sum_senses_left, sum_senses_right]
