import pymorphy2

morph = pymorphy2.MorphAnalyzer()


def get_honest_words(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]) and text[i] != '-':
            text = text.replace(text[i], ' ')
    return list(filter(lambda word: len(word) > 1, text.lower().replace('ё', 'е').split()))


def get_words(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')
    return list(filter(lambda word: len(word) > 1, text.lower().replace('ё', 'е').split()))
