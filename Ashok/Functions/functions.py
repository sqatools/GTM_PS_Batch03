def greeting():
    print("Welcome to Python Programming")


def greeting_new(msg):
    print(msg)


greeting_new("Good Morning")
greeting_new("Good Evening")
greeting_new("Welcome")


def addition(param1, param2):
    print("value of param1 :", param1)
    print("value of param2 :", param2)
    print("addition of param :", param1 + param2)


# pass by value
addition(40, 50)

print("_" * 50)
# pass by reference
x = 500
y = 800
addition(x, y)

print("_" * 50)
# change the param sequence to call
addition(param2=x, param1=y)


# Home-work:
# write a python program for simple calculator and perform math operations like
# addition
# multiplication
# subtraction
# division
# with help of function

def addition(a, b):
    print("Addition:", a + b)


def subtraction(a, b):
    print("Subtraction:", a - b)


def multiplication(a, b):
    print("Multiplication:", a * b)


def division(a, b):
    print("Division:", a / b)


calc = int(input("Enter 1. Addition, 2. Subtraction 3. Multiplication 4. Division:"))
a = int(input("Enter A Value:"))
b = int(input("Enter B value:"))

if calc == 1:
    addition(a, b)
elif calc == 2:
    subtraction(a, b)
elif calc == 3:
    multiplication(a, b)
elif calc == 4:
    division(a, b)
else:
    print('Invalid input')