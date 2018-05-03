# average word length


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    length = sum(map(len, words))
    return length / len(words)
