class Matrix:

    def __init__(self, param):
        self.param = param

    def __str__(self):
        return "\n".join("\t".join([str(el) for el in line]) for line in self.param)

    def __add__(self, other):
        try:
            n = [[int(self.param[line][el]) + int(other.param[line][el]) for el in range(len(self.param[line]))]
                 for line in range(len(self.param))]

            return Matrix(n)
        except IndexError:
            print("Ошибка")


mc = [[99, 9], [2, 6]]
mc2 = [[56, 36], [1, 3]]

mat1 = Matrix(mc)
mat2 = Matrix(mc2)
mat3 = mat1 + mat2

print(mat1)
print(mat3)
