
# Python Object Relationships - One to Many

## Introduction
In this lab we are going to practice creating a one to many relationship. We've learned how a belongs to relationship works -- with the "belongs to" class knowing the one instance it is associated with. Now, what if we think about it from the other side? Let's say we are talking about a `Person` class and a `Dog` class. We know the `Dog` belongs to one `Person`, but that doesn't mean the person can't have more than one dog, right?

![dog gif](https://s3.amazonaws.com/learn-verified/data-science-assets/two-dogs.gif)

So, a dog still needs to know who its owner is, but now we know that an owner can also have **many** dogs. Let's get started!

## Objectives
* Create a one to many domain model
* Practice querying an instance to demonstrate the one to many relationship
* Define a second one to many domain and create instance methods that again demonstrate the one to many relationship

## Defining Our Classes

Let's start by defining two classes, `Owner` and `Car`.
* An owner should be instantiated with a `name` and an `age`.
* A car should be instantiated with a `make`, `model`, and `year`.
* The relationship between the two classes should be such that an owner has many cars and a car belongs to an owner. It is our job to make sure our classes and instances are set up to show this.
* Think about which class(es) also must have an `_all` class variable, and be sure to have setter and getter (read and write) instance methods for each attribute for an owner and for a car as well as a class method that returns the `_all` list.


```python
from owner import Owner
jake = Owner("Jake", 25)
jess = Owner("Jess", 29)
alexa = Owner("Alexa", 33)
pete = Owner("Pete", 30)
```


```python
from car import Car
# create several instances of the Car class and associate them to owners.
# remember owners can have more than one car associated with them, but a car can only have one owner
```

## Querying For Our Cars

Okay, now that we have our classes set up, let's stat to work with them. Let's say Alexa and Pete both have several cars and it has gotten to the point that they are forgetting about some of them -- like when winter is over and you're re-discovering the bathing suits you stuffed into the abyss of your closet. Yes, Alexa and Pete are doing well for themselves.
Since we don't want them to lose track of their cars, let's write an instance method that prints out the makes and models of each car that they own, respectively. Let's call this method `find_my_cars`. It should return a list of strings which are the name of the car's make concatenated with the car's model. (i.e. `["Toyota Highlander", "Audi Q7", "Jeep Wrangler"]`)


```python
alexa.find_my_cars()
```


```python
pete.find_my_cars()
```

Great work! Now, let's try this out with another domain to get even more practice. Let's work with a `Driver` and a `Trip` class.
* The relationship between the two should be that a driver has many trips and that a trip belongs to one driver.
* A driver should be instantiated with at least a *name* and a trip should be instantiated with at least a start and a destination (i.e. `battery park` to `central park`).
* Remember a trip should know which **driver** it belongs to and the Trip class should keep track of all trip instances in the `_all` class variable.
* Define the appropriate getter and setter instance methods for both the driver and trip instance objects as well as a class method, `all`, that returns the `_all` list.


```python
from driver import Driver
steve = Driver("Steve")
danielle = Driver("Danielle")
hortense = Driver("Hortense")
```


```python
from trip import Trip
# create several instances of the Trip class and associate them to drivers.
# remember to associate a trip with a driver
```

Next, define a driver instance method that returns all the trips instance objects that a driver has given, let's call it `my_trips`. Then define an instance method that returns a list of strings that represent the trips start and end locations for each of those trips (i.e. `[home to work, work to movies]`). Let's call it `my_trip_summaries`.


```python
hortense.my_trips()
```


```python
danielle.my_trips()
```


```python
steve.my_trip_summaries()
```

## Summary
Great work! In this lab we practiced creating one to many relationships. We built on the belongs to relationship and were able to make it a bit more interesting by associating more than one instance object with another. We reinforced our knowledge by building out two different one to many domains and built intance methods that returned and operated on the one to many relationships.
