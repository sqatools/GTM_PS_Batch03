"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object
without modifying its structure. Decorators are typically applied to functions, and they play a crucial role
in enhancing or modifying the behavior of functions.

"""
#1).
# def decorator(func):
#     def inner():
#         print('-'*50)
#         func()
#         print('-' * 50)
#     return inner
# @decorator
# def greeting():
#     print('Welcome to Python Programming')
#
# greeting()

#2).
# def function2(func):
#     print("_"*50)
#     func()
#     print("_"*50)
#
# @function2
# def programming():
#     print("Welcome to Java Programming")
#
# programming()


#3).
def mathDecorator(func):
    def inner(n):
        if n <=20:
            func(n)
        else:
            func(20)
    return inner
@mathDecorator
def square(n):
    for i in range(1,n):
        print(i,'=',i**2)

square(24)  # Condition is only print till 20, Do not show the square value of 24 here.

