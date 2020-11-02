from time import sleep
from random import randint

class Car:
    def __init__(self, acelerate, color, name, is_police=False):
        self.name = name
        self.acelerate = acelerate
        self.speed = self.acelerate * 7
        self.color = color
        self.is_police = is_police
    def __str__(self):
        return f"Name and surname: {self.name} {self.acelerate}"

    def go(self):
        print(f'{self.name} is started')

    def stop(self):
        print(f'{self.name} is stopped')

    def turn_right(self):
        print(f'{self.name} is turned right')

    def turn_left(self):
        print(f'{self.name} is turned left')

    def show_speed(self):
        print(f'Current speed {self.name} is {self.speed}')

class TownCar(Car):
    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 60:
            print(f'Speed of {self.name} is higher than allow for town car')
        else:
            print(f'Speed of {self.name} is normal for town car')

class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 40:
            print(f'Speed of {self.name} is higher than allow for work car')
        else:
            print(f'Speed of {self.name} is normal for work car')

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

class PoliceCar(Car):
    def __init__(self, acelerate, color, name, is_police=True):
        super().__init__(acelerate, color, name, is_police)

class TrafficLight:
    __color = [['red', 7], ['yellow', 2], ['green', 7], ['yellow', 2]]

    def running(self):
        while True:
            print('red')
            sleep(7)
            print('yellow')
            sleep(2)
            print('green')
            c = randint(0,10)
            ford.go()
            if c < 3:
                ford.turn_right()
            elif 2 < c < 5:
                ford.turn_left()
            ferrari.go()
            if 4 < c < 6:
                ferrari.turn_right()
            elif 5 < c < 7:
                ferrari.turn_left()
            toyota.go()
            if 6 < c < 8:
                toyota.turn_right()
            elif 8 < c:
                toyota.turn_left()
            gazel.go()
            sleep(7)
            print('yellow')
            ford.stop()
            ford.show_speed()
            ferrari.stop()
            ferrari.show_speed()
            toyota.stop()
            toyota.show_speed()
            gazel.stop()
            gazel.show_speed()
            sleep(2)

ford = PoliceCar(11, 'Blue', 'Ford')
ferrari = SportCar(15, 'Red', 'Ferrari', False)
toyota = TownCar(8, 'White', 'Toyota', False)
gazel = WorkCar(6, 'Black', 'Gazel', False)


first_light = TrafficLight()
first_light.running()



