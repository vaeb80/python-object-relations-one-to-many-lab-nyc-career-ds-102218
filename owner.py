# import car class here
from car import Car

class Owner:

    def __init__(self, name, age):
        self._name = name
        self._age = age
        self._cars = []

    @property
    def cars(self):
        return self._cars
    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @cars.setter
    def cars(self, car):
        self._cars.append(car)

    def find_my_cars(self):
        return [f"{car.make} {car.model}" for car in self.cars]
