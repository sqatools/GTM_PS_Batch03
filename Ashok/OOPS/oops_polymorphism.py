"""
polymorphism : when one method perform the multiple tasks, then it is known as polymorphism

method overloading : When one class have two methods with same name and different parameters, then it
                     is known as method overloading. but python does not allow the method overloading
                     it only consider the latest defined method. Python is dynamically typed language.
method overriding : when child class and parent class have same method name with same parameters then
                    child class method will override the parent class method, and it is known as method
                    overriding. if we want to execute the parent method then we need to use super keyword.
operator overloading :

duck typing:
"""


# Method Overloading is not supporting in python: #
class Addition:

    def findSum(self, a, b):
        print('Result=', a + b)

    def findSum(self, a, b, c):
        print("Result=", a + b + c)


# obj1 = Addition()
# # It always calls the latest method if we pass 2 or 3 parameters
# obj1.findSum(2, 3)     # TypeError: Addition.findSum() missing 1 required positional argument: 'c'
# obj1.findSum(2, 3, 4)  # It will execute successfully as it is having 3 params and latest method is having 3 args.

# We can achieve the above problem using *args
class Addition1:

    def findSum1(self, a, b, c=None):
        if c is None:
            print('Result:', a + b)
        else:
            print('Result:', a + b + c)


obj1 = Addition1()
obj1.findSum1(2, 3)
obj1.findSum1(2, 3, 4)


# Method Overloading with another module #
# from multipledispatch import dispatch
# class A:
#     @dispatch(int, int)
#     def add(self, a, b):
#         return a+b
#
#     def

# Method Overriding #






