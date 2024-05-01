# Topics : Constructor Overloading, Constructor Chaining, Returning the values,
# Counting objects.

"""
Constructor overloading: It is a concept of having more than one constructor with a different parameters list in such a
way so that each constructor can perform different task.
Python does not support constructor overloading. If we define multiple constructors then, the interpreter will
consider only the last constructor and throws an error if the sequence of the arguments doesn’t match as per the last
constructor
"""

# This will throw error as TypeError: OverStudent.__init__() missing 1 required positional argument: 'age'
# class OverStudent:
#     # one argument constructor
#     def __init__(self, name):
#         print("One argument constructor")
#         self.name = name
#
#     # Two argument constructor
#     def __init__(self, name, age):
#         print("Two arguments constructor")
#         self.name = name
#         self.age = age
#
#
# # creating first object
# obj4 = OverStudent("Ashok")

"""
Constructor chaining: It is the process of calling one constructor from another constructor. It is useful when you want 
to invoke multiple constructors, one after another, by initializing only one instance.

In Python, constructor chaining is convenient when we are dealing with inheritance. When an instance of a child class 
is initialized, the constructors of all the parent classes are first invoked and then, in the end, the constructor of 
the child class is invoked. 

Using the super() method we can invoke the parent class constructor from a child class.
"""


class Vehicle:
    def __init__(self, engine):
        print("Vehicle Constructor")
        self.engine = engine


class Car(Vehicle):
    def __init__(self, engine, max_speed):
        super().__init__(engine)
        print("Car Constructor")
        self.max_speed = max_speed


class Electric_car(Car):
    def __init__(self, engine, max_speed, km_range):
        super().__init__(engine, max_speed)
        print("Electric Car Constructor")
        self.km_range = km_range


obj6 = Electric_car('1500cc', 240, 750)
print(f"Engine = {obj6.engine}, Max_speeed = {obj6.max_speed}, Km_range={obj6.km_range} ")

# Counting the number of objects of a class #
""" While creating an object it will call constructor by default every time once. To count the number of objects
of a class we can add the counter."""


class Employee:
    count = 0

    def __init__(self):
        Employee.count = Employee.count + 1


e1 = Employee()
e2 = Employee()
e3 = Employee()
e4 = Employee()
print(Employee.count)

# Constructor return value #
""" In Python, the constructor does not return any value. Therefore, while declaring a constructor, we don’t 
have anything like return type. Instead, a constructor is implicitly called at the time of object instantiation. 
Thus, it has the sole purpose of initializing the instance variables.

The __init__() is required to return None. We can not return something else. If we try to return a 
non-None value from the __init__() method, it will raise TypeError
"""


# class Test:
#     def __init__(self, i):
#         self.id = i
#         return True
#
# d = Test(10)