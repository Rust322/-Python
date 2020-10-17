import random

class Car:

    speed = random.randint(1, 180)

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def show_speed(self):
        print("Текущая скорость", self.speed)

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self):
            if random.random() > 0.5:
                print(f"{self.name} повернула направо")
            else:
                print(f"{self.name} повернула налево")



class TownCar(Car):

    def show_speed(self):
        print(f"Скорость {self.name} составялет {self.speed} ")
        if self.speed > 60:
            print(f"{self.color} {self.name} вы превысили скорость!")
            self.stop()


class WorkCar(Car):

    def show_speed(self):
        print(f"Скорость {self.name} составялет {self.speed} ")
        if self.speed > 40:
            print(f"{self.color} {self.name} вы превысили скорость!")
            self.stop()


class SportCar(Car):

    def show_speed(self):
        print(f"Скорость {self.name} составялет {self.speed} ")


class PoliceCar(Car):

    def show_speed(self):
        print(f"Скорость {self.name} составялет {self.speed} ")


police = PoliceCar(random.randint(1, 180), "Black&White", "Police Car", True)
police.show_speed()
police.go()
police.turn()
police.stop()
sport = SportCar(random.randint(1, 180), "Red", "Ferrari", True)
sport.name = "Koenigsegg"
sport.show_speed()
work = WorkCar(random.randint(1, 180), "Black", "Toyota", True)
work.show_speed()
town = TownCar(random.randint(1, 180), "White", "Town Car", True)
town.show_speed()
