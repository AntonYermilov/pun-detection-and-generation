# existence of conditions


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.split()
    return int('если' in words or 'когда' in words)
