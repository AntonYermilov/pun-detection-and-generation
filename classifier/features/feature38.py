from util.util import get_words
from util.special.lg_util import norm_forms, LABELS_DICT


def get_score(text):
    """
    Counts words with labels and emotional/
    :param text: string;
    :return: int - number of domains with more than 1 word in the given sentence;
    """
    words = get_words(text)
    words_with_labels = set()
    for word in words:
        norms = norm_forms(word)
        if norms:
            for norm in norms:
                labels = LABELS_DICT.get(norm, None)
                if labels:
                    words_with_labels.add(norm)
    return len(words_with_labels)
