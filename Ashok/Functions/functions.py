"""
# Functions #
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return data as a result.
"""


# 1.
def greeting():
    print("Welcome to Python Programming")


# 2.
"""
Arguments Information can be passed into functions as arguments. Arguments are specified after the 
function name, inside the parentheses. You can add as many arguments as you want, just separate them
with a comma.
"""


def greeting_new(msg):
    print(msg)


greeting_new("Good Morning")
greeting_new("Good Evening")
greeting_new("Welcome")


# pass by value  or positional arguments #

def add(param1, param2):
    print("value of param1 :", param1)
    print("value of param2 :", param2)
    print("addition of param :", param1 + param2)


add(40, 50)


def sub(param3, param4):
    print("value of param1 :", param3)
    print("value of param2 :", param4)
    print("subtraction of param :", param3 - param4)


sub(30, 20)

# pass by reference or keyword arguments #

x = 500
y = 800
add(x, y)

# change the param sequence to call #
add(param2=x, param1=y)


def mul(x1, y1, z1):
    s = x1 * y1 * z1
    print(s)


mul(x1=5, y1=4, z1=2)

# Passing the default value to function parameter #
"""
Rules
# -> if param has default value then no need to pass value for default param while calling the
function
# - User can overwrite the default param value while calling the function.
# - Default parameters always set on right of all param,
# - Default parameter should always follow the non default parameters.
"""


def default_param(num1, num2, num3=20):
    print("Addition is:", num1 + num2 + num3)


default_param(20, 30)
default_param(20, 30, num3=40)

# Arbitrary Arguments or Variable length of args or *args #
"""
If you do not know how many arguments that will be passed into your function, then add a * before the 
parameter name in the function definition Ex: def my_function(*args)
# *args should always come at the end of the param list.
# *args accepts n number of values and consider tuple of values
"""


def arbitrary_arguments1(*name):
    print(name)


arbitrary_arguments1("Ashok")
arbitrary_arguments1("Ashok", "Kumar")
arbitrary_arguments1("Ashok", "Kumar", "Pusarla")
arbitrary_arguments1("Ashok", 25.5, 5)


def arbitrary_arguments2(age, num, *name):
    print(age, num, name)


arbitrary_arguments2(25, 1, "Ashok")
arbitrary_arguments2(25, 1, 12, "Hello", "Ashok")

# Arbitrary Keyword Arguments or Keyword length arguments or **kwargs #
""" 1. If you do not know how many keyword arguments that will be passed into your function,
add two asterisk: ** before the parameter name in the function definition. 
2. This accepts the param values in key value formate
3. default structure is dictionary format to get all the values
 """


def arbitrary_keyword_arguments(**age):
    print(age)


arbitrary_keyword_arguments(Name="Ashok", Dept="IT", Rollno=25, age=30)


# Using *args and **kwargs #
def user_info_details(name, *args, **kwargs):
    print(name, args, kwargs)


user_info_details("Ashok", 1, 2, 3, Age=30, Dept="IT", Email="test@test.com")


# Using mixed positional or keyword arguments #
def mixed1(a, b, /, c, d, e, f):
    return a + b + c + d + e + f


# Here before /(forward slash) arguments must be positional arguments(a, b)
# Here after /(forward slash) arguments can be positional or keyword arguments(c, d, e, f)

x = mixed1(10, 20, 30, 40, e=50, f=60)
print("Mixed value:", x)


def mixed2(a, b, /, c, d, *, e, f):
    return a + b + c + d + e + f


# Here before /(forward slash) arguments must be positional arguments(a, b)
# Here after /(forward slash) arguments can be positional or keyword arguments(c, d)
# Here after (*) arguments must be keyword arguments(e, f)

y = mixed2(10, 20, 30, d=40, e=50, f=60)
print("Mixed valued:", y)


# return value from function #
def calculation1(a, b, c):
    d = a + b + c
    return d


result1 = calculation1(10, 20, 30)
print(result1)


# returns multiple values from function #
def calculation2(e, f, g):
    h = e * e, f + f, g * g
    return h


result2 = calculation2(2, 4, 6)
print(result2)


# Function documentation #
def factorials(num1):
    """
    This function will get the factorials of any given number and return it
    :param num1: this is required input number
    :return: int
    """
    fact = 1
    for i in range(num1, 0, -1):
        fact = fact * i

    return fact


print(factorials(5))

print(factorials.__doc__)  # 1st way of printing the function documentation

help(factorials)  # 2nd way of printing the function documentation

# Function recursion #

temp = 1


def fun1():
    global temp
    print(temp)
    temp = temp + 1
    if temp == 10:
        exit()
    fun1()


# RecursionError: maximum recursion depth exceeded
# fun1()

