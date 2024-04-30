"""
class : class is nothing but the blueprint of the object, where we define all feature attributes/methods
        and variable related to the object
object : Object is entity through which we can access feature functionality of the class
         we can create n number of objects of any specific class.
constructor : constructor which initialize the memory of the class object.
            1. Default constructor : default it being called while creating the object.
            2. Parametrize constructor : constructor which has some parameter to pass while creating
            the object of the class.
variables : variable we declare to set the values in the class
            1. Instance variable : the variable which we declare with the help of self, then it
                                   instance variable.
            2. class variable : variable we declare on class level, then it is known as class variables.

methods :  When we declare any function inside the class then it is known as method.
             1. Instance method : Method we declare self as first parameter, then it is instance method.
             2. class method : Method we declare with @classmethod decorator and default
                            parameter will be cls, that can access only class variable, then it is known as class method.
             3. static method : Static methods are associated with class name not need to create
                            object of the class.
inheritance
polymorphism
data hiding
abstraction
"""


class ABC:
    Team = "CSK"  # class variable
    city = "Mumbai"

    def __init__(self, num1, num2):
        self.user_name = None
        print("Object Initiated")
        self.x = num1
        self.y = num2

    def instanceMethod1(self):
        self.user_name = 'Ashok'

    def instanceMethod2(self):
        print(self.user_name)

    def instanceMethod3_add(self):
        print("Addition:", self.x + self.y)

    def instanceMethod4(self):
        print("Calling class variable using self:", self.Team)

    @classmethod
    def classMethod1(cls):
        print("Calling class variable using cls:", cls.Team)
        print("Calling the class variable using cls:", cls.city)
        cls.city = "Bangalore"
        print("Modifying the class variable:", cls.city)

    @staticmethod
    def static_method1(a, b):
        print(a + b)

    def internal_calling(self):
        self.instanceMethod1()
        self.instanceMethod2()
        self.instanceMethod3_add()
        self.instanceMethod4()
        self.classMethod1()
        self.static_method1(2, 3)


obj = ABC(2, 3)
obj.instanceMethod1()
obj.instanceMethod2()
obj.instanceMethod3_add()
obj.instanceMethod4()
obj.classMethod1()
obj.static_method1(2, 3)
obj.internal_calling()

print(obj.__module__)
print(obj.__class__)
print(obj.__doc__)

# Accessor and Mutators
val1 = obj.__getattribute__("x")
val2 = obj.__getattribute__("y")
print("value of x is:", val1)
print("value of y is:", val2)

obj.__setattr__("x", 500)
val3 = obj.__getattribute__("x")
print("value of x is:", val3)

obj.__setattr__("y", 600)
val4 = obj.__getattribute__("y")
print("value of y is:", val4)


