from gensim.models import KeyedVectors
from util.dataloader import load_frequencies, load_senses
from util.util import morph

CURRENT_MODEL = 'ruscorpora'
MODELS = {'ruscorpora': 'ruwikiruscorpora_upos_skipgram_300_2_2018.vec',
          'araneum': 'araneum_upos_skipgram_300_2_2018.vec'}

TAGS = {'NOUN': '_NOUN',
        'ADJF': '_ADJ',
        'INFN': '_VERB',
        'ADVB': '_ADV',
        'Name': '_PROPN',
        'NUMR': 'NUM'}

GRAPH_SIZE = 49493

wv = KeyedVectors.load_word2vec_format(MODELS[CURRENT_MODEL], binary=False)
frequencies = load_frequencies()
senses = load_senses()


def get_pos_form(normal_form):
    opt_form = max(morph.parse(normal_form), key=lambda x: x.score)
    for key, value in TAGS.items():
        if key not in opt_form.tag:
            continue
        return normal_form.replace('ё', 'е') + value, opt_form.score
    return None, None


def get_pos_tag(normal_form):
    opt_form = max(morph.parse(normal_form), key=lambda x: x.score)
    return opt_form.tag.POS


def get_dist(src, v, u):
    src.seek(v * (2 * GRAPH_SIZE) + 2 * u)
    dist = int.from_bytes(src.read(2), byteorder='little', signed=False)
    return dist