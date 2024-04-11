def greeting():
    print("Welcome to Python Programming")


# greeting()
# greeting()
# greeting()
# greeting()

def greeting_new(msg):
    print(msg)

# greeting_new("Good Morning")
# greeting_new("Good Evening")
# greeting_new("Welcome")


def addition(param1, param2):
    print("value of param1 :", param1)
    print("value of param2 :", param2)
    print("addition of param :", param1+param2)


# pass by value
addition(40, 50)

print("_"*50)
# pass by reference
x = 500
y = 800
addition(x, y)

print("_"*50)
# change the param sequence to call
addition(param2=x, param1=y)

# Home-work:
# write a python program for simple calculator and perform math operations like
# addition
# multiplication
# subtraction
# division
# with help of function
