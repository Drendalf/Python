from abc import ABC, abstractmethod


class Clothes(ABC):
    cost_count = 0

    @abstractmethod
    def cost(self):
        pass


class Coat(Clothes):
    def __init__(self, size):
        self.size = size
        Coat.cost_count += self.cost

    def __str__(self):
        return f"Пальто размером{self.size} расход {self.cost} общий расход {round(Coat.cost_count, 2)}"

    @property
    def cost(self):
        cost = self.size / 6.5 + 0.5
        return float(cost)


class Costum(Clothes):
    def __init__(self, h):
        self.h = h
        Costum.cost_count += self.cost

    def __str__(self):
        return f"Костюм ростом{self.h} расход {self.cost} общий расход {round(Costum.cost_count, 2)}"

    @property
    def cost(self):
        cost = (self.h * 2 + 0.3) / 100
        return float(cost)


cloth_coat = Coat(22)
print(cloth_coat)
cloth_costum = Costum(22)
print(cloth_costum)
cloth_coat1 = Coat(23)
print(cloth_coat1)
