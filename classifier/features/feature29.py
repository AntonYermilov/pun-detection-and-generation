# existence of substring '???', '?!', '?', '!'


def get_score(text):
    if '???' in text:
        return 4
    if '?!' in text:
        return 3
    if '?' in text:
        return 2
    if '!' in text:
        return 1
    return -1
