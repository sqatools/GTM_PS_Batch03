"""
These are the types of methods that can be written inside any class.
Accessor methods are useful for reading the properties of class of an object
Mutators are used for writing or updating the properties of class and its objects.
"""


class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b

    def get_length(self):
        return self.length

    def set_length(self, l):
        self.length = l

    def area(self):
        return self.length * self.breadth


r1 = Rectangle(2, 10)
print(r1.get_length())
print(r1.area())
r1.set_length(5)
print(r1.area())
