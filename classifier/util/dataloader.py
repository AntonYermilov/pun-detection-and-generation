import json
import urllib.request

NEWS_URL = 'http://eranik.me:5222/puns/news/get'
PROVERBS_URL = 'http://eranik.me:5222/puns/proverbs/get'  # allproverbs.ru
BOOKS_URL = 'http://eranik.me:5222/puns/books/get'
PUNS_URL = 'http://eranik.me:5222/puns/humorous/get'

ONELINERS = 'dataset/oneliners.json'
NEWS = 'dataset/news.json'
PROVERBS = 'dataset/proverbs.json'
BOOKS = 'dataset/books.json'
PUNS = 'dataset/puns.json'

LEARN_DATASET = 'final_dataset/learn.json'
TEST1_DATASET = 'final_dataset/test1.json'
TEST2_DATASET = 'final_dataset/test2.json'
VALIDATION_DATASET = 'final_dataset/validation.json'

FREQUENCIES = 'tools/frequencies.txt'
SENSES = 'tools/senses.txt'
INTRODUCTORY_WORDS = 'tools/introductory_words.txt'


def load_web():
    for url in [NEWS_URL, PROVERBS_URL, BOOKS_URL, PUNS_URL]:
        request = ''.join(x.decode('utf-8') for x in urllib.request.urlopen(url).readlines())
        file = {NEWS_URL: NEWS, PROVERBS_URL: PROVERBS, BOOKS_URL: BOOKS, PUNS_URL: PUNS}[url]
        with open(file, 'w') as output:
            output.write(request)


def load_oneliners():
    jokes = []
    data = json.load(open(ONELINERS, 'r'))
    for pun in data:
        text = pun['text']
        answer = pun['answer']
        if text != answer:
            text += ' ' + answer
        jokes.append(text)
    return jokes


def load_news():
    return [text['text'] for text in json.load(open(NEWS, 'r'))['texts']]


def load_proverbs():
    return [text['text'] for text in json.load(open(PROVERBS, 'r'))['texts']]


def load_books():
    return [text['text'] for text in json.load(open(BOOKS, 'r'))['texts']]


def load_puns():
    return [text['text'] for text in json.load(open(PUNS, 'r'))['texts']]


def load_dataset(path):
    request = json.load(open(path, 'r'))['texts']
    texts = [None] * len(request)
    for text in request:
        texts[text['id']] = (text['label'], text['text'])
    return texts


def load_learn_dataset():
    return load_dataset(LEARN_DATASET)


def load_test1_dataset():
    return load_dataset(TEST1_DATASET)


def load_test2_dataset():
    return load_dataset(TEST2_DATASET)


def load_validation_dataset():
    return load_dataset(VALIDATION_DATASET)


def load_frequencies():
    frequencies = {}
    with open(FREQUENCIES, 'r') as f:
        for line in f.readlines():
            word, num = line.split()
            frequencies[word] = int(num)
    return frequencies


def load_senses():
    return json.load(open(SENSES, 'r'))


def load_introductory_words():
    words_set = set()
    with open(INTRODUCTORY_WORDS, 'r') as f:
        for line in f.readlines():
            words_set.add(line.strip())
        if '' in words_set:
            words_set.remove('')
    return words_set
