def type_logger(func):
    def calcul(*args):
        w = {}
        f = func(*args)
        for i in f:
            c = (type(i))
            w[i] = c
        yield w

    return calcul


@type_logger
def calc(*args):
    b = []
    for i in args:
        d = i ** 3
        b.append(d)
    return b


z = calc(3, 6.6, 7)
print(*z)
