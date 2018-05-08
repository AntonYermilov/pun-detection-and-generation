# max w2v dist between words

from util.util import morph, get_words
from util.special.ae_util import get_pos_form, wv


def get_word_array(text):
    array = []
    for word in get_words(text):
        all_forms = {}
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            normalized_word, score = get_pos_form(form.normal_form)
            if normalized_word is not None and normalized_word in wv.vocab:
                if normalized_word not in all_forms:
                    all_forms[normalized_word] = 0
                all_forms[normalized_word] += score * form.score

        if len(all_forms) != 0:
            array.append((word, all_forms))
    return array


def get_score(text):
    word_array = get_word_array(text)
    score = -1
    for w1, forms1 in word_array:
        for w2, forms2 in word_array:
            if w1 == w2:
                continue
            for form1, score1 in forms1.items():
                for form2, score2 in forms2.items():
                    score = max(score, score1 * score2 * wv.similarity(form1, form2))
    return score
