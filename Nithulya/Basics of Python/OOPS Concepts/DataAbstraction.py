"""
Abstraction : abstraction means to hide the details information from the user, just to provide overview of
              the implimentation.
              abstraction can be achieved, when parent class method is implimented in the child class.
"""
#1).
# class Animal:
#     def animalVoice(self):
#         pass
#     def animalName(self):
#         pass
#     def animalCategory():
#        pass
# class Dog(Animal):
#     def animalVoice(self):
#         print('Dog Barks')
#     def animalName(self):
#         print('Animal is Dog')
#
# if __name__ == "__main__":
#     obj= Dog()
#     obj.animalVoice()

#2).Abstract class & Abstract method:
from abc import ABC,abstractmethod
class Vehicle(ABC):
    def startEngine(self):
        print('Starting Engine.')
    def applyBreak(self):
        print('Applying Break.')
    def stopEngine(self):
        print('Stopping the Engine')
    @abstractmethod
    def changeGear(self):
        pass
class Car(Vehicle):
    def openSunroof(self):
        print('Opening sun roof.')
    def changeGear(self):
        print('Changing gear automatically.')
class Truck(Vehicle):
    def loadWeight(self):
        print('Loading weight')
    def changeGear(self):
        print('Changing gear manually.')
obj1 = Car()
obj1.changeGear()
obj2 = Truck()
obj2.changeGear()