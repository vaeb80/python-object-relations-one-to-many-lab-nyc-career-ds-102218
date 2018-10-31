class Car:
    _all = []

    def __init__(self, make, model, year, owner):
        self._make = make
        self._model = model
        self._year = year
        self._owner = owner
        owner.cars = self
        self._all.append(self)

        #remember to associate a car with its owner

    @property
    def owner(self):
        return self._owner

    @property
    def model(self):
        return self._model

    @property
    def year(self):
        return self._year

    @classmethod
    def all(cls):
        return cls._all

    @property
    def make(self):
        return self._make
