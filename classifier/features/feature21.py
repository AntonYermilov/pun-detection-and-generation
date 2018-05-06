# sum of weighed (with idf) word vectors

from util import wv, morph, frequencies, TAGS
import numpy as np
from math import log


def get_normalized_form(normal_form):
    form_tag = max(morph.parse(normal_form), key=lambda x: x.score).tag
    for key, value in TAGS.items():
        if key not in form_tag:
            continue
        return normal_form.replace('ё', 'е') + value
    return None


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    sumw = np.array([0] * 300, dtype=np.float32)
    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            normalized_form = get_normalized_form(form.normal_form)
            if normalized_form is not None:
                if normalized_form in wv.vocab:
                    sumw += form.score * log(192689044 / (frequencies.get(form.normal_form, 0) + 1)) * wv[normalized_form]
    return sumw / np.linalg.norm(sumw)
