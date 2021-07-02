list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

for item in list[:]:
    s = 0
    for i in item:
        if i.isdigit():
            while s != 1:
                s = s + 1
                a = '"'
                index = list.index(item)
                list.insert(index, a)
                list.insert(index + 2, a)
                list.insert(index + 1, )
str=""
for item in list:
    str+=item
    str += " "

print(str)

