# max w2v dist between words

from util import wv, morph, TAGS


def get_normalized_form(normal_form):
    opt_form = max(morph.parse(normal_form), key=lambda x: x.score)
    for key, value in TAGS.items():
        if key not in opt_form.tag:
            continue
        return normal_form.replace('ё', 'е') + value, opt_form.score
    return None


def get_word_array(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    array = []
    for word in text.lower().split():
        all_forms = {}
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            normalized_word, score = get_normalized_form(form.normal_form)
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
