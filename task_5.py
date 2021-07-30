import random


def get_jokes(number, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    d = []
    if repeat == True:
        while number != 0:
            number = number - 1
            joke = []
            a = random.randint(0, len(nouns) - 1)
            b = random.randint(0, len(adverbs) - 1)
            c = random.randint(0, len(adjectives) - 1)
            joke.append(nouns[a])
            joke.append(adverbs[b])
            joke.append(adjectives[c])
            d.append(joke)

    else:
        try:
            while number != 0:
                number = number - 1
                joke = []
                random.shuffle(nouns)
                random.shuffle(adverbs)
                random.shuffle(adjectives)
                joke.append(nouns[0])
                nouns.pop(0)
                joke.append(adverbs[0])
                adverbs.pop(0)
                joke.append(adjectives[0])
                adjectives.pop(0)
                d.append(joke)

        except(IndexError):
            z = print("все")
    return d


print(get_jokes(7, True))
