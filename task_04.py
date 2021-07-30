class Car():
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(self, direction):
        print(f"Машина повернула на {direction}")

    def show_speed(self, ):
        print(f"Скорость {self.speed}")


class TownCar(Car):
    def show_speed(self, ):
        if self.speed > 60:
            print(f"Скорость скорость превышена на {self.speed - 60}")


class WorkCar(Car):
    def show_speed(self, ):
        if self.speed > 40:
            print(f"Скорость скорость превышена на {self.speed - 40}")


townCar = TownCar(150, "red", "VAZ")
sportCar = Car(150, "green", "VG")
workCar = WorkCar(70, "yellow", "Toyota")
policeCar = Car(100, "white", "ZAZ", is_police=True)
townCar.show_speed()
sportCar.turn("Право")
