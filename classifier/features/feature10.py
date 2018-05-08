# max number of tags

from util.util import morph, get_words

good_tags = {'NOUN', 'VERB', 'INFN', 'GRND', 'ADJF', 'ADJS', 'COMP', 'PRTF', 'PRTS', 'NUMR', 'ADVB', 'COMP'}


def get_score(text):
    words = get_words(text)
    max_tags = 0

    for word in words:
        tags = set()
        for form in morph.parse(word):
            if form.tag.POS in good_tags:
                tags.add(form.tag.POS)
        max_tags = max(max_tags, len(tags))

    return max_tags
