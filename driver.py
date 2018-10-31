# remeber to import the trip class here
from trip import Trip

class Driver:

    _all = []

    def __init__(self, name):
        self._name = name
        self._trips = []
        self._all.append(self)

    @classmethod
    def all(cls):
        return cls._all

    @property
    def name(self):
        return self._name

    @property
    def trips(self):
        return self._trips

    @trips.setter
    def trips(self, trip):
        self.trips.append(trip)

    def my_trips(self):
        return self.trips

    def my_trip_summaries(self):
        return [f"{x.start} to {x.destination}" for x in self.my_trips()]
