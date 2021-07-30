ls = []

summa = 0
for i in range(1, 1000):
    if i % 2 != 0:
        i = i ** 3 + 17
        ls.append(i)

for element in ls[:]:
    el = (element % 10 // 1) + (element % 100 // 10) + \
         (element % 1000 // 100) + (element % 10000 // 1000) + \
         (element % 100000 // 10000) + (element % 1000000 // 100000) + \
         (element % 10000000 // 1000000) + (element % 100000000 // 10000000) + \
         (element % 1000000000 // 100000000)

    if el % 7 != 0:
        ls.remove(element)

for i in range(0, len(ls) - 1, 2):
    m = ls[i] + ls[i + 1]
    summa = summa + m
print(summa)
