from sys import argv

if __name__ == '__main__':
    with open("bakery.csv", "r", encoding="utf-8") as f:
        a = len(argv)
        if a == 1:
            print(f.read())
        if a == 2:
            for line in f.readlines()[int(argv[1]) - 1:]:
                print(line, end="")
        if a == 3:
            for line in f.readlines()[int(argv[1]) - 1:int(argv[2])]:
                print(line.replace("\n", ""))
