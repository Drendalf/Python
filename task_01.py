import time


class TrafficLight():
    __color = {"красный": 7, "желтый": 2, "зеленый": 4}

    def running(self):
        while True:
            for key in self.__color:
                print(key)
                time.sleep(self.__color[key])


a = TrafficLight()
a.running()
