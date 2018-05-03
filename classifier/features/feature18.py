# question-answer form of text


def get_score(text):
    text = text.strip()
    parts = text.lower().split('?')
    return int(len(parts) > 1 and text[-1] != '?')
