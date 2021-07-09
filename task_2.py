def ans(a, b):
    for i in range(0, len(a) + 1):
        q = []
        q.append(a[i])
        q.append(b[i])
        q = tuple(q)
        yield q


tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', "Катя", "Женя"
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]
while len(tutors) != len(klasses):
    klasses.append("None")

w = ans(tutors, klasses)
print(w)
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
print(next(w))
