list_1 = [57.8, 46.51, 97, 102, 15.33, 99.9, 6.32, 120, 36.58, ]
list_2 = []
str_1 = ""
for i in list_1:
    rubles=int(i)
    kop=round((i-rubles)*100)
    list_2.append(f'{rubles} руб {kop:02d} коп')
print(",".join(list_2))
id1= id(list_1)
if id1 == id(list_1):
    print("id совпадает")
else:
    print("id НЕ совпадает")
my_list = sorted(list_1, reverse=True)
print(sorted(my_list[:5]))







