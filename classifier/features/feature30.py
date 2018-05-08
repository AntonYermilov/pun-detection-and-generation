# existence of names

from util.special.nm_util import name_extractor

good_tags = {'Name', 'Patr', 'Surn'}
bad_tag = 'Init'


def get_score(text):
    matches = name_extractor(text.title())
    for match in matches:
        for token in match.tokens:
            if 'forms' in dir(token) and 'value' in dir(token) and len(token.value) > 2:
                for name_type in good_tags:
                    if name_type in token.forms[0].grams and bad_tag not in token.forms[0].grams:
                        return 1
    return 0
