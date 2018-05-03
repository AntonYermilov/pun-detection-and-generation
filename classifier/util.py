import pymorphy2
from gensim.models import KeyedVectors
from dataloader import load_frequencies, load_senses

CURRENT_MODEL = 'ruscorpora'
MODELS = {'ruscorpora': 'ruwikiruscorpora_upos_skipgram_300_2_2018.vec',
          'araneum': 'araneum_upos_skipgram_300_2_2018.vec'}

TAGS = {'NOUN': '_NOUN',
        'ADJF': '_ADJ',
        'INFN': '_VERB',
        'ADVB': '_ADV',
        'Name': '_PROPN',
        'NUMR': 'NUM'}

wv = KeyedVectors.load_word2vec_format(MODELS[CURRENT_MODEL], binary=False)
morph = pymorphy2.MorphAnalyzer()
frequencies = load_frequencies()
senses = load_senses()
