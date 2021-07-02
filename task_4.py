list_1=['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for item in list_1:
    word=item.split(" ")
    name=word[-1]
    name_1=name.capitalize()
    greeting=f"Привет,{name_1}!"
    print(greeting)