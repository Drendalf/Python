def num_translate(number):
    if number in dic:
        print(dic[number])
    else:
        print("Число больше 10")


dic = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять",
       "six": "шесть", "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять", }

num_translate("six")


