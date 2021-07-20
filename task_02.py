import json
import sys

dic_1 = {}
a_1 = []
b_1 = []
with open('users.csv', 'r', encoding='utf-8') as file_1:
    with open('hobby.csv', 'r', encoding='utf-8') as file_2:
        a = file_1.readlines()
        b = file_2.readlines()
        for item in a:
            line = (item.replace(",", " ").replace("\n", " "))
            a_1.append(line)
        for item in b:
            line = (item.replace("\n", " "))
            b_1.append(line)
        if len(a_1) < len(b_1):
            sys.exit(1)
        while len(a_1) > len(b_1):
            b_1.append("None")
        for i in range(0, len(a_1)):
            dic_1[a_1[i]] = b_1[i]
with open('answer.csv', 'w+', encoding='utf-8') as f:
    json.dump(dic_1, f, ensure_ascii=False)
with open('answer.csv', 'r', encoding='utf-8') as f_1:
    nums = json.load(f_1)
print(nums)
