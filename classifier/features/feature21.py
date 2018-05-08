# sum of weighed (with idf) word vectors

from util.util import morph, get_words
from util.special.ae_util import wv, frequencies, get_pos_form
import numpy as np
from math import log


def get_score(text):
    words = get_words(text)

    vector_sum = np.array([0] * 300, dtype=np.float32)
    for word in words:
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            normalized_word, _ = get_pos_form(form.normal_form)
            if normalized_word is not None and normalized_word in wv.vocab:
                idf = log(192689044 / (frequencies.get(form.normal_form, 0) + 1))
                vector = wv[normalized_word]
                vector_sum += form.score * idf * vector

    size = np.linalg.norm(vector_sum)
    if size < 1e-4:
        return [0] * 300
    return list(vector_sum / np.linalg.norm(vector_sum))
