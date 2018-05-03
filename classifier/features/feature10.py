# max number of tags

from util import morph


def get_score(text):
    for i in range(len(text)):
        if not text[i].isalnum():
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    max_tags = 0

    for word in words:
        tags = set()
        for form in morph.parse(word):
            for good_tag in {'NOUN', 'VERB', 'INFN', 'GRND',
                             'ADJF', 'ADJS', 'COMP', 'PRTF', 'PRTS', 'NUMR', 'ADVB', 'COMP'}:
                if good_tag == form.tag.POS:
                    tags.add(good_tag)
        max_tags = max(max_tags, len(tags))

    return max_tags
