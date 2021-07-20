def add_sale(a):
    with open("bakery.csv", "a", encoding="utf-8") as f:
        f.write(a + "\n")


if __name__ == '__main__':
    import sys

    a = sys.argv[1]
    add_sale(a)
