class Worker():
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

    def get_full_name(self):
        print(f"{self.name} {self.surname}")

    def get_total_income(self):
        sum1 = self._income["wage"] + self._income["bonus"]
        print(f"{self.name} в должности {self.position} получает  {sum1} усл. ед")


position = Worker("Ivan", "Alekseevich", "ruk", 30, 30)
position.get_full_name()
position.get_total_income()
