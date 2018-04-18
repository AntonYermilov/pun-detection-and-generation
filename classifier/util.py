import pymorphy2
from gensim.models import KeyedVectors


CURRENT_MODEL = 'ruscorpora'
MODELS = {'ruscorpora': 'ruwikiruscorpora_upos_skipgram_300_2_2018.vec',
          'araneum': 'araneum_upos_skipgram_300_2_2018.vec'}


wv = KeyedVectors.load_word2vec_format(MODELS[CURRENT_MODEL], binary=False)
morph = pymorphy2.MorphAnalyzer()
