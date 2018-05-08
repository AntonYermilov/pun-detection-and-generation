# max dist between word senses (uses w2v)

from util.util import morph, get_words
from util.special.ae_util import senses, wv, get_pos_form


def get_score(text):
    words = get_words(text)
    max_dist = -1

    for word in words:
        all_senses = []
        for form in morph.parse(word):
            normal_form = form.normal_form
            if normal_form not in senses:
                continue
            for sense, _ in senses[normal_form].items():
                if sense not in all_senses:
                    all_senses.append(sense)

        if len(all_senses) == 0:
            continue

        for i in range(len(all_senses)):
            for j in range(len(all_senses[i])):
                if not all_senses[i][j].isalnum():
                    all_senses[i] = all_senses[i].replace(all_senses[i][j], ' ')
            all_senses[i] = all_senses[i].split()

            for j in range(len(all_senses[i])):
                normal_form = max(morph.parse(all_senses[i][j]), key=lambda x: x.score).normal_form
                all_senses[i][j], _ = get_pos_form(normal_form)

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
