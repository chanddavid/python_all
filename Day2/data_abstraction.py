from abc import ABC,abstractmethod
class Abstract(ABC):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def get(self):
        print(f"my name is{self.name} ")

obj5=Abstract()
# absttacrt class doesn't create an obj so it throw an error

from abc import ABC, abstractmethod

class Car(ABC):
    def __init__(self,name):
        self.name = name

    def description(self):
        print("This the description function of class car.")

    @abstractmethod
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")
        print("hello")
class new(Car):
    def price(self,x):
        print(f"The {self.name}'s price is {x} lakhs.")
obj = new("Honda City")

obj.description()
obj.price(25)