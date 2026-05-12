# abc means Abstract base class
from abc import ABC, abstractmethod

class Vechile(ABC):
    
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):
    
    def go(self):
        print("You drive the car.")

    def stop(self):
        print("You stop the car.")

car = Car()
car.go()

class Motorcycle(Vechile):

    def go(self):
        print("You ride the motorcycle.")
    
    def stop(self):
        print("You stop the motorcycle.")


motorcycle = Motorcycle()

motorcycle.go()