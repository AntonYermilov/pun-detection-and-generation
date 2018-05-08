from util import dataloader
import random
import json


def create():
    puns = dataloader.load_puns()
    oneliners = dataloader.load_oneliners()
    nonhumorous = dataloader.load_books() + dataloader.load_proverbs() + dataloader.load_news()

    random.shuffle(oneliners)
    random.shuffle(nonhumorous)

    size = min(len(oneliners), len(nonhumorous))
    oneliners = oneliners[:size]
    nonhumorous = nonhumorous[:size]

    learn_size = int(0.7 * size)
    test_size = int(0.2 * size)

    learn_oneliners = oneliners[:learn_size]
    learn_nonhumorous = nonhumorous[:learn_size]
    test_oneliners = oneliners[learn_size:learn_size + test_size]
    test_nonhumorous = nonhumorous[learn_size:learn_size + test_size]
    validation_oneliners = oneliners[learn_size + test_size:]
    validation_nonhumorous = nonhumorous[learn_size + test_size:]

    with open('final_dataset/learn.json', 'w') as f:
        result = []
        id = 0
        for text in learn_oneliners:
            result.append({'label': 0, 'text': text, 'id': id})
            id += 1
        for text in learn_nonhumorous:
            result.append({'label': 1, 'text': text, 'id': id})
            id += 1
        json.dump({'texts': result}, f)

    with open('final_dataset/test1.json', 'w') as f:
        result = []
        id = 0
        for text in test_oneliners:
            result.append({'label': 0, 'text': text, 'id': id})
            id += 1
        for text in test_nonhumorous:
            result.append({'label': 1, 'text': text, 'id': id})
            id += 1
        json.dump({'texts': result}, f)

    with open('final_dataset/test2.json', 'w') as f:
        result = []
        id = 0
        for text in puns:
            result.append({'label': 0, 'text': text, 'id': id})
            id += 1
        json.dump({'texts': result}, f)

    with open('final_dataset/validation.json', 'w') as f:
        result = []
        id = 0
        for text in validation_oneliners:
            result.append({'label': 0, 'text': text, 'id': id})
            id += 1
        for text in validation_nonhumorous:
            result.append({'label': 1, 'text': text, 'id': id})
            id += 1
        json.dump({'texts': result}, f)
