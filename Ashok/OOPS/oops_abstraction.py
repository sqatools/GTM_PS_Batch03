"""
Abstract class: If a class contains atleast one abstract method then it is abstract class
Abstract method: A method without definition (code or body) is called abstract method
Concreted method: Normal method in abstract class in concrete method.

rules:
1. Abstraction is the mechanism of only declaring methods but not instantiated.
2. Declared methods are implemented in sub class
3. We cannot create object for abstract class, we can create object for concrete class
4. To convert abstract class into concrete class using inheritance concept
5. To implement abstract class and abstract methods we need to import ABC module.
6. To identify abstract method we need to write the decorator as @abstractmethod
"""

from abc import ABC, abstractmethod


class Robo(ABC):  # Abstract class

    @abstractmethod
    def sana(self):
        pass

    @staticmethod
    def baby():
        print("hello world")


class Chitti(Robo):

    def sana(self):
        print("Hi Sana")


obj = Chitti()
obj.sana()
obj.baby()
