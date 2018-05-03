import json
import urllib.request


ONELINERS = 'joke_datasets/one-liners.json'
NEWS = 'http://eranik.me:5222/puns/news/get'
PROVERBS = 'http://eranik.me:5222/puns/proverbs/get'  # allproverbs.ru
BOOKS = 'http://eranik.me:5222/puns/books/get'
FREQUENCIES = 'tools/frequencies.txt'
SENSES = 'tools/senses.txt'


def load_jokes():
    jokes = []
    data = json.load(open(ONELINERS, 'r'))
    for pun in data:
        text = pun['text']
        answer = pun['answer']
        if text != answer:
            text += ' ' + answer
        jokes.append(text)
    return jokes


def load_web(url):
    request = ''.join(x.decode('utf-8') for x in urllib.request.urlopen(url).readlines())
    texts = [text['text'] for text in json.loads(request)['texts']]
    return texts


def load_news():
    return load_web(NEWS)


def load_proverbs():
    return load_web(PROVERBS)


def load_books():
    return load_web(BOOKS)


def load_frequencies():
    frequencies = {}
    with open(FREQUENCIES, 'r') as f:
        for line in f.readlines():
            word, num = line.split()
            frequencies[word] = int(num)
    return frequencies


def load_senses():
    return json.load(open(SENSES, 'r'))
