"""
Class:
The class is a user-defined data structure that binds the data members and methods into a single unit.
Class is a blueprint or code template for object creation. To create an object we require a model or plan
or blueprint which is nothing but class.

A class contains the properties (attribute) and action (behavior) of the object. Properties represent variables,
and the methods represent actions. Hence, class includes both variables and methods.

Object:An object is an instance of a class. It is a collection of attributes (variables) and methods.
We use the object of a class to perform actions.

An object has the following two characteristics: Attribute, Behavior
For example, A Car is an object, as it has the following properties:
name, price, color as attributes
breaking, acceleration as behavior
"""


# Simple creation of class with methods.
class A:

    def method1(self):
        print("Hello welcome to method 1")

    def method2(self):
        print("Hello welcome to method 2")


obj1 = A()  # Object creation
obj1.method1()  # calling method using object
obj1.method2()  # calling method using object

obj2 = A()  # We can create multiple objects for same class
obj2.method1()
obj2.method2()


# Example 2:
class Person:

    # data members (instance variables)
    def __init__(self, name, sex, profession, years):  # Constructor
        self.name = name
        self.sex = sex
        self.profession = profession
        self.years = years

    # Behaviour (instance methods)
    def study(self):
        print(f"Name is {self.name} and gender is {self.sex} and working as a {self.profession}")

    # Behaviour (instance methods)
    def working(self):
        print(f"He/She is working in Multi speciality hospital from last {self.years} years")


# Creating an object of class
obj2 = Person("Ashok", "Male", "Doctor", "3")

# call methods
obj2.study()
obj2.working()

obj3 = Person("Mounica", "Female","Doctor", "5")
obj3.study()
obj3.working()
