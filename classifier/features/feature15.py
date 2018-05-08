# max dist between noun senses (in thesaurus graph)

from util.util import morph, get_words
from util.special.ae_util import senses, get_pos_tag, get_dist


def get_score(text):
    words = get_words(text)

    exists = False
    max_dist = 0

    with open('tools/distances.txt', 'rb') as src:
        for word in words:
            nodes = []
            for form in morph.parse(word):
                normal_form = form.normal_form
                if get_pos_tag(normal_form) != 'NOUN':
                    continue
                if normal_form not in senses:
                    continue

                for _, id in senses[normal_form].items():
                    node = int(id[1:])
                    if node not in nodes:
                        nodes.append(node)

            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    dist = get_dist(src, nodes[i], nodes[j])
                    if not exists or dist > max_dist:
                        exists = True
                        max_dist = dist

    return max_dist
