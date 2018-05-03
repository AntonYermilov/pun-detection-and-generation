# existence of oppositional alliances


def get_score(text):
    for i in range(len(text)):
        if not str.isalnum(text[i]):
            text = text.replace(text[i], ' ')

    words = text.lower().split()
    for alliance in ['а', 'но', 'да', 'зато', 'однако']:
        if alliance in words:
            return 1
    return 0
