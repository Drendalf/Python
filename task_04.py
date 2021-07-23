def val_checker(x):
    def _val_checker(func):
        def calcul(*args):
            for el in args:
                if el > 0:
                    f = func(*args)
                    return f
                elif el < 0:
                    raise ValueError('Цифры должны быть больше 0')
        return calcul
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3

z = calc_cube(-15)
print(z)
