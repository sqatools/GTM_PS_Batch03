"""
Polymorphism :
---------------
1. When one method perform the multiple tasks, then it is known as polymorphism.
ex: 1 person is a human being.
a. Same person is a son to his Father
b. Same person is husband to his wife
c. Same person is a father to his children
d. Same person is working as bank employee.

Ex2: Operator overloading is another example of polymorphism.
+ operator is doing addition between number
+ operator is doing concatenation between strings

3. Compile time polymorphism or Static polymorphism - Method overloading, Operator over loading will do in
compile time phase
4. Run time polymorphism or Dynamic polymorphism    - Method overriding will do in run time phase.

Method overloading :
-------------------
1. When one class have two methods with same name and different parameters, then it is known as method overloading.
 but python does not allow the method overloading it only consider the latest defined method. Python is dynamically
 typed language.

Method overriding :
--------------------
1. When child class and parent class have same method name with same parameters then child class method will override
the parent class method, and it is known as method overriding. If we want to execute the parent method then we need to
use super keyword.

Rules:
a. Super class and Sub class must be present(Inheritance must be done between two classes)
b. Declare two classes with same method and same parameters
c. Logic must be in different parameters
d. Method overriding will be done when we access the same method in subclass. If we access in superclass then method
will not override.

Operator overloading : is another example of polymorphism.
+ operator is doing addition between number
+ operator is doing concatenation between strings

Duck typing:

"""


# Method Overloading#

# It will not support in python #
class Addition:

    def findSum(self, a, b):
        print('Result=', a + b)

    def findSum(self, a, b, c):
        print("Result=", a + b + c)


# obj1 = Addition()
# # It always calls the latest method if we pass 2 or 3 parameters
# obj1.findSum(2, 3)     # TypeError: Addition.findSum() missing 1 required positional argument: 'c'
# obj1.findSum(2, 3, 4)  # It will execute successfully as it is having 3 params and latest method is having 3 args.

# Another example to achieve method overloading


# We can achieve the above problem using below conditions.
class Addition1:

    def findSum1(self, a, b, c=None):
        if c is None:
            print('Result:', a + b)
        else:
            print('Result:', a + b + c)


obj2 = Addition1()
obj2.findSum1(2, 3)
obj2.findSum1(2, 3, 4)

# Using multiple dispatch library we can achieve the method overloading.
from multipledispatch import dispatch


class X:
    @dispatch(int, int)
    def add(self, a, b):
        print(a + b)

    @dispatch(int, int, int)
    def add(self, a, b, c):
        print(a + b + c)

    @dispatch(str, str)
    def add(self, a, b):
        print(a + b)


obj3 = X()
obj3.add(2, 3)
obj3.add(2, 3, 4)
obj3.add("hello", "world")


# Method Overriding #
class A:
    def func1(self):
        print('Function1 is working')

    def func2(self):
        print('Function2 is working in class A')


class B(A):
    def func3(self):
        print('Function3 is working')

    def func2(self):
        super().func2()  # 1st way - Using super key and calling the parent method in child class.
        A.func2(self)  # 2nd way - Using class name and calling the parent method in child class.
        print('Function2 is working in class B')


obj4 = B()
obj4.func1()
obj4.func3()
obj4.func2()  # It will call the child class and executes


# Duck typing #
class Duck:
    def talk(self):
        print("Duck is typing")

    def walk(self):
        print("Duck is walking")


class Dog:
    def talk(self):
        print("Dog is typing")

    def walk(self):
        print("Dog is walking")


def petlover(pet):
    pet.talk()
    pet.walk()


d = Duck()
e = Dog()

petlover(d)
petlover(e)

# Operator Overloading #
# 1.
print(5 + 2)
print("jessy" + "roy")
print([10, 20, 30] + ['jessa', 'emma', 'kelly'])  # merging two list

# 2.
n1, n2 = 10, 20
print("Addition is:", n1 + n2)
print("Addition is:", n1.__add__(n2))
print(dir(int))

# 3.
s1 = 'Hello'
s2 = 'Good Morning'
print("Add String :", s1 + s2)
print("Add String :", s1.__add__(s2))
print(dir(str))

# 4.
print("Multiplication :", n1 * n2)
print("Multiplication :", n1.__mul__(n2))


# 5. Operator overloading with custom objects
class Book:
    def __init__(self, pages):
        self.pages = pages

    # Overloading + operator with magic method
    def __add__(self, other):
        return self.pages + other.pages


b1 = Book(400)
b2 = Book(300)
print("Total number of pages: ", b1 + b2)
