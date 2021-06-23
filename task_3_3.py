list_1 = ["", "a", "ов"]
pecent = int(input("Введите процент до 20"))
if pecent == 1:
    print(str(pecent) + " процент" + list_1[0])
if 1 < pecent < 5:
    print(str(pecent) + " процент" + list_1[1])
if 5 <= pecent <= 20:
    print(str(pecent) + " процент" + list_1[2])
