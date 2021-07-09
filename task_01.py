def odd_nums(number):
    for num in range(1, number + 1, 2):
        yield num


odd_to_15 = odd_nums(15)
print(next(odd_to_15))
print(next(odd_to_15))

# второй способ
number_2 = int(input("Введите число"))
numb = (i for i in range(1, number_2 + 1, 2))
print(next(numb))
print(next(numb))
print(next(numb))
