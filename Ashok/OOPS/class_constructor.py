"""
A constructor is a special method and primarily used to create/declare to initialize data member/ instance variables
of a class.This constructor is executed automatically at the time of object creation.

Syntax:
-------------------------------
def __init__(self):
    # body of the constructor
-------------------------------
def: The keyword is used to define function.

__init__() Method: It is a reserved method. This method gets called as soon as an object of a class is
instantiated.

self: The first argument self refers to the current object. It binds the instance to the __init__() method.
It’s usually named self to follow the naming convention. We can write own variable like a, b, c etc..
Using self, we can access the instance variable and instance method of the object.

The __init__() method arguments are optional. We can define a constructor with any number of arguments.
-------------------------------------------------------------------------------------------------------------
For every object, the constructor will be executed only once. For example, if we create four objects,
the constructor is called four times.

In Python, every class has a constructor, but it’s not required to define it explicitly. Defining constructors
in class is optional. Python will provide a default constructor if no constructor is defined.

Three types of constructors:
Default Constructor
Non-parametrized constructor
Parameterized constructor
"""


# Example 1:

class Student:

    # constructor
    # initialize instance variable
    def __init__(self, name, age):
        self.n = name
        self.a = age
        print("All variables initialized")

    def show(self):
        print("Hello, my name is", self.n, "and age is", self.a)


# creating object of the class
const1 = Student("Ashok", 25)

# calling the instance method using the object const1
const1.show()

"""
Default Constructor: Python will provide a default constructor, if no constructor is defined in class by programmer. 
Python inserts a default constructor into your code on your behalf. It does not perform any tasks but initializes the 
objects. It is an empty constructor without a body. This constructor is known as the default constructor.
"""


# As you can see in the below example, we do not have a constructor, but we can still create an object for the class
# because Python added the default constructor during a program compilation.
class Employee:

    def display(self):
        print("Inside display")


emp = Employee()
emp.display()

"""
Non - Parameterized Constructor: A constructor without any arguments is called a non-parameterized constructor. 
This type of constructor is used to initialize each object with default values.
This constructor doesn’t accept the arguments during object creation. Instead, it initializes every object with the 
same set of values.
"""


class Company:

    # no-argument constructor
    def __init__(self):
        self.name = "Pynative"
        self.address = "ABC Street"

    # a method for printing data members
    def show(self):
        print('Name:', self.name, 'Address:', self.address)


npconst = Company()
npconst.show()

# calling the instance variables with object npconst
v1 = npconst.name
v2 = npconst.address
print("Name is:", v1, "and address is:", v2)

"""
Parametrized constructor:
A constructor with defined parameters or arguments is called a parameterized constructor. We can pass different values 
to each object at the time of creation using a parameterized constructor.

The first parameter to constructor is self that is a reference to the being constructed, and the rest of the arguments 
are provided by the programmer. A parameterized constructor can have any number of arguments.
"""


class Human:
    # parameterized constructor
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    # display object
    def show(self):
        print(self.name, self.age, self.salary)


# creating object of the Employee class
emma = Human('Emma', 23, 7500)
emma.show()

kelly = Human('Kelly', 25, 8500)
kelly.show()

""" Constructor with default arguments :
Python allows us to define a constructor with default values. The default value will be used if we do not 
pass arguments to the constructor at the time of object creation """


class Cuboid:
    def __init__(self, l=1, b=2, h=3):
        self.length = l
        self.breadth = b
        self.height = h

    def lid_area(self):  # Self must be used if we are using variables from constructor
        return self.length * self.breadth

    def total_volume(self):
        return 2 * (self.length * self.breadth * self.height)

    def volume(self):
        return self.length * self.breadth * self.height


c2 = Cuboid()
print(c2.lid_area())
print(c2.total_volume())
print(c2.volume())