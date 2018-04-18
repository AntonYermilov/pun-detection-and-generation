import json
import urllib
import re


ONELINERS = 'one-liners.json'
NEWS = 'http://eranik.me:5222/puns/news/get'
PROVERBS = 'http://allproverbs.ru/index.php?name=News&op=cat&catid={}&pagenum={}'


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


def load_news():
    request = ''.join(x.decode('utf-8') for x in urllib.request.urlopen(NEWS).readlines())
    news = [title['text'] for title in json.loads(request)['texts']]
    return news


def load_proverbs():
    proverbs = []
    for catid in range(1, 61):
        pagenum = 1
        exists = True
        while exists:
            request = ''.join(x.decode('cp1251') for x in urllib.request.urlopen(PROVERBS.format(catid, pagenum)))
            exists = False
            for proverb in re.findall('<strong>.*?</strong>', request):
                proverb = proverb.lower()
                for c in proverb:
                    if not str.isalnum(c) or (ord('a') <= ord(c) <= ord('z')):
                        proverb = proverb.replace(c, ' ')
                proverb = ' '.join(proverb.split())
                proverbs.append(proverb)
                exists = True
            pagenum += 1
    return proverbs


