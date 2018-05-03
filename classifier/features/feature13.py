# max dist between word senses (uses w2v)

from util import wv, morph, senses, TAGS


def get_normalized_form(normal_form):
    opt_form = max(morph.parse(normal_form), key=lambda x: x.score)
    for key, value in TAGS.items():
        if key not in opt_form.tag:
            continue
        return normal_form.replace('ё', 'е') + value
    return None


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    max_dist = -1

    for word in words:
        all_senses = []
        for form in morph.parse(word):
            normal_form = form.normal_form
            if normal_form not in senses:
                continue
            for sense in senses[normal_form]:
                if sense not in all_senses:
                    all_senses.append(sense)

        if len(all_senses) == 0:
            continue

        for i in range(len(all_senses)):
            for j in range(len(all_senses[i])):
                if not all_senses[i][j].isalnum():
                    text = text.replace(all_senses[i][j], ' ')
            all_senses[i] = all_senses[i].split()

            for j in range(len(all_senses[i])):
                normal_form = max(morph.parse(all_senses[i][j]), key=lambda x: x.score).normal_form
                all_senses[i][j] = get_normalized_form(normal_form)

        for i in range(len(all_senses)):
            for j in range(i + 1, len(all_senses)):
                for w1 in all_senses[i]:
                    if w1 is None or w1 not in wv.vocab:
                        continue
                    for w2 in all_senses[j]:
                        if w2 is None or w1 == w2 or w2 not in wv.vocab:
                            continue
                        max_dist = max(max_dist, wv.similarity(w1, w2))

    return max_dist
