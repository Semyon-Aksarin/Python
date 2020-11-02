from time import sleep
import itertools

class TrafficLight:
    __color = [['red', 7], ['yellow', 2], ['green', 7], ['yellow', 2]]

    def running(self):
        for el in itertools.cycle(self.__color):
            print(el[0])
            sleep(el[1])

first_light = TrafficLight()
first_light.running()