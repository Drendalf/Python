ls = []
ls_1 = []
summa = 0
for i in range(1, 1000):
    if i % 2 != 0:
        i = i ** 3
        ls.append(i)
for i in range(0, len(ls)):
    b = ls[i] % 1000000000 // 100000000
    v = ls[i] % 100000000 // 10000000
    q = ls[i] % 10000000 // 1000000
    t = ls[i] % 1000000 // 100000
    e = ls[i] % 100000 // 10000
    r = ls[i] % 10000 // 1000
    a = ls[i] % 1000 // 100
    j = ls[i] % 100 // 10
    c = ls[i] % 10 // 1

    z = b + v + q + t + e + r + a + j + c
    if z % 7 == 0:
        ls_1.append(ls[i])

for i in range(0, len(ls_1) - 1, 2):
    m = ls_1[i] + ls_1[i + 1]
    summa = summa + m
print(summa)
