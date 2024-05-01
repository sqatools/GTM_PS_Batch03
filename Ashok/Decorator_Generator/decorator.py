"""
A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
modifying its structure. Decorators are typically applied to functions, and they play a crucial role in enhancing or
modifying the behavior of functions. Traditionally, decorators are placed before the definition of a function you want
to decorate.

# 3 rules should follow to create a decorator
1. passing function as parameter
2. Nested function calling parameter function
3. return nested function
"""


def decorator(func):
    def inner():
        print("-" * 50)
        func()
        print("-" * 50)

    return inner


@decorator
def greeting():
    print("Welcome to python programming")


greeting()


# Example 2:

def mathDecorator(func):
    def inner(s):
        if s <= 20:
            func(s)
        else:
            func(20)

    return inner


@mathDecorator
def sqaure(n):
    for i in range(1, n):
        print(i, '=', i ** 2)


sqaure(24)
