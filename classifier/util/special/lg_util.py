import json
from util.util import morph

# others are stopwords
GOOD_POSES = {'NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB', 'INFN', 'PRTF', 'PRTS', 'GRND', 'ADVB', 'PRED'}

# to remove punctuation symbols from text
TRANSLATION = str.maketrans('', '', '!\"#$%&\'()*+,./:;<=>?@[\]^_`{|}~—')

ANALYZER = morph

with open('tools/stop_words.txt') as f:
    STOP_WORDS = set(list(map(str.strip, f.readlines())))

with open('tools/domain.json') as domains_file:
    DOMAINS_DICT = json.load(domains_file)
with open('tools/word_to_info.json') as info_file:
    WORD_INFO_DICT = json.load(info_file)
with open('tools/POS-synonymy.json') as synonyms_file:
    SYNONYMS_DICT = json.load(synonyms_file)
with open('tools/antonym.json') as antonyms_file:
    ANTONYMS_DICT = json.load(antonyms_file)
with open('tools/word_to_labels.json') as labels_file:
    LABELS_DICT = json.load(labels_file)

# jsons with relations or labels
# {synset_id : [synset_id]}
DICTIONARIES = {
    'antonym': ANTONYMS_DICT,
    'synonym': SYNONYMS_DICT,
    'domain': DOMAINS_DICT,
    'labels': LABELS_DICT
}


def norm_forms(word):
    """
    Makes list of normal forms from pymorphy2 analyser
    :param word: input word (str);
    :return: list of normalized forms of the given word.
    """
    norm_forms = set()
    if word not in STOP_WORDS:
        lexemes = ANALYZER.parse(word)
        for lexeme in lexemes:
            pos = lexeme.tag.POS
            if pos in GOOD_POSES:
                normalized_lexeme = lexeme.normalized
                norm_form = normalized_lexeme.normal_form
                if norm_form:
                    norm_forms.add(norm_form)
    return list(norm_forms)


def get_synset_id(word):
    """
    Gets synset_id of the given word or None if the word not in the RuWordNet.
    :param word: input word (str);
    :return: synset_id or None.
    """
    word_info = WORD_INFO_DICT.get(word, None)
    if word_info:
        return word_info['synset_id']
    return None


def collect_by_relation(norms, relation):
    if norms:
        for word in norms:
            dictionary = DICTIONARIES[relation]
            synset_id = get_synset_id(word)
            if synset_id:
                words_with_relation = dictionary.get(synset_id, list())
                return words_with_relation
    return list()


def make_pairs(words):
    """
    Makes pairs of words without duplicates.
    :param words: list of words;
    :return: list of pairs of the words.
    """
    pairs_of_words = set()
    for i in range(len(words)):
        word_i = words[i]
        if word_i in STOP_WORDS:
            continue
        for j in range(i + 1, len(words)):
            word_j = words[j]
            if word_j in STOP_WORDS:
                continue
            if word_i != word_j:
                tmp_list = sorted((word_i, word_j))
                pairs_of_words.add((tmp_list[0], tmp_list[1]))
    return pairs_of_words


def count_pair_relation(words, relation):
    """
    Counts pairs of words with the given relation.
    :param words: list of words;
    :param relation: string, see DICTIONARIES keys;
    :return: int.
    """
    def collect_synsets_ids(norms):
        ids = set()
        for norm in norms:
            synset_id = get_synset_id(norm)
            if synset_id:
                ids.add(synset_id)
        return ids

    pairs_of_words = make_pairs(words)
    count = 0
    for word_i, word_j in pairs_of_words:
        norms_i = norm_forms(word_i)
        synsets_i = collect_synsets_ids(norms_i)
        relations_i = collect_by_relation(norms_i, relation)
        norms_j = norm_forms(word_j)
        relations_j = collect_by_relation(norms_j, relation)
        synsets_j = collect_synsets_ids(norms_j)
        if synsets_i.intersection(relations_j) or synsets_j.intersection(relations_i):
            count += 1
    return count
