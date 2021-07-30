class Road():
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def run(self, v, s):
        sum = self._length * self._width * v * s
        print(f"Масса асфальта равна {sum}")


a = Road(10, 5)
a.run(1, 3)
