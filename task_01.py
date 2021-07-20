list_01 = []
list_02 = dict()
max = 0
ip = ""
with open("nginx_logs.txt", "r", encoding='utf-8') as f:
    for line in f:
        a = line.split()
        kor = (a[0], a[5], a[6])
        list_01.append(kor)
for el in list_01:
    spam = list_01.count(el)
    list_02[spam] = el
for key, values in list_02.items():
    if key > max:
        max = key
        ip = values
print(ip, max)
