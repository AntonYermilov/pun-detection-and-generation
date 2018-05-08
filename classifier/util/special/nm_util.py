from natasha import SimpleNamesExtractor
from util.util import morph, get_words
from util.dataloader import load_introductory_words


VOWELS = 'аяуюоёэеыи'

name_extractor = SimpleNamesExtractor()
introductory_words_set = load_introductory_words()


def get_syllables_counts(text):
    words = get_words(text)
    clean_words = []

    for word in words:
        ok = True
        for form in morph.parse(word):
            if form.score < 0.1:
                continue
            if form.tag.POS in {'PREP', 'CONJ', 'PRCL', 'INTJ'}:
                ok = False
                break
        if ok:
            clean_words.append(word)

    return [sum([word.count(letter) for letter in VOWELS]) for word in clean_words]


def split_by_every(text, delimeters):
    text = [text]
    new_text = []

    for char in delimeters:
        for word in text:
            new_text.extend(word.split(char))
        text = new_text
        new_text = []

    return text


def get_word_part_lengths(text):
    parts = split_by_every(text, ',.!?…—')
    word_parts = []

    for part in parts:
        if len(part) == 0:
            continue
        word_parts.append(len(get_words(part)))
    total_words = sum(word_parts)

    if total_words == 0:
        return []
    return [l / total_words for l in word_parts]
