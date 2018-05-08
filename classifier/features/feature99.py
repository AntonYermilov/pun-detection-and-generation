# min dist between word senses (uses w2v)

from util.util import morph, get_words
from util.special.ae_util import senses, wv, get_pos_form, get_pos_tag

good_tags = {'NOUN', 'INFN', 'ADJF'}


def get_score(text):
    words = get_words(text)
    min_dist = 1

    for word in words:
        all_senses = []
        for form in morph.parse(word):
            normal_form = form.normal_form
            if get_pos_tag(normal_form) in good_tags:
                continue
            if normal_form not in senses:
                continue

            for sense, _ in senses[normal_form].items():
                if sense not in all_senses:
                    all_senses.append(sense)

        if len(all_senses) == 0:
            continue

        bag_of_words = set()
        for i in range(len(all_senses)):
            for j in range(len(all_senses[i])):
                if not all_senses[i][j].isalnum():
                    all_senses[i] = all_senses[i].replace(all_senses[i][j], ' ')
            all_senses[i] = all_senses[i].lower().split()
            want = min(len(all_senses[i]), 3)

            for sense_word in all_senses[i][:want]:
                normal_form = max(morph.parse(sense_word), key=lambda x: x.score).normal_form
                normalized_form, _ = get_pos_form(normal_form)
                if normalized_form is not None and normalized_form not in bag_of_words and normalized_form in wv.vocab:
                    bag_of_words.add(normalized_form)

        for w1 in bag_of_words:
            for w2 in bag_of_words:
                if w1 == w2:
                    continue
                min_dist = min(min_dist, wv.similarity(w1, w2))

    return min_dist
