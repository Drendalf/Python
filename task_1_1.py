duration = int(input("Введите число в секудах"))

if duration <= 60:
    print(str(duration) + " сек")
elif duration > 60 and duration < 3600:
    minut = duration // 60
    sec = duration % 60
    print(str(minut) + " мин " + str(sec) + " сек")
elif duration >= 3600 and duration < 86400:
    hour = (duration // 60) // 60
    minut = (duration // 60) % 60
    sec = duration % 60
    print(str(hour) + " час " + str(minut) + " мин " + str(sec) + " сек")
else:
    day = (duration // 60) // 60 // 24
    hour = (duration // 60) // 60 % 24
    minut = (duration // 60) % 60
    sec = duration % 60
    print(str(day) + " дни " + str(hour) + " час " + str(minut) + " мин " + str(sec) + " сек")