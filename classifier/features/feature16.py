# min dist between word senses (in thesaurus graph)

from util import morph, senses


GRAPH_SIZE = 49492


def satisfies(normal_form):
    form_tag = max(morph.parse(normal_form), key=lambda x: x.score).tag
    for tag in ['NOUN', 'INFN', 'ADJF']:
        if tag == form_tag.POS:
            return True
    return False


def get_dist(src, v, u):
    src.seek(v * (2 * GRAPH_SIZE) + 2 * u)
    dist = int.from_bytes(src.read(2), byteorder='little', signed=False)
    return dist


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    min_dist = 65535

    with open('tools/distances.txt', 'rb') as src:
        for word in words:
            nodes = []
            for form in morph.parse(word):
                normal_form = form.normal_form
                if not satisfies(normal_form):
                    continue
                if normal_form not in senses:
                    continue

                for _, id in senses[normal_form].items():
                    node = int(id[1:]) - 1
                    if node not in nodes:
                        nodes.append(node)

            for i in range(len(nodes)):
                for j in range(i + 1, len(nodes)):
                    min_dist = min(min_dist, get_dist(src, nodes[i], nodes[j]))

    return min_dist
