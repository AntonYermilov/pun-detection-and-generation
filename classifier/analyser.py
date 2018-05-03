import dataloader


def average_words(texts):
    cnt = 0
    for text in texts:
        cnt += len(text.split())
    return cnt / len(texts)


def main():
    print('JOKES AVERAGE=' + str(average_words(dataloader.load_jokes())))
    print('NEWS AVERAGE=' + str(average_words(dataloader.load_news())))
    print('PROVERBS AVERAGE=' + str(average_words(dataloader.load_proverbs())))
    print('BOOKS AVERAGE=' + str(average_words(dataloader.load_books())))


if __name__ == '__main__':
    main()
