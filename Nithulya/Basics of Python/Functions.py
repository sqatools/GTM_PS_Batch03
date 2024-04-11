#1.
# def my_function():              # def - definition
#     print("This is my first function")
# my_function()    # This is my first function
# my_function()    # This is my first function


#2.
# def my_function(country):
#     print("I am from",country)
# my_function('India')       # I am from India
# my_function('USA')         # I am from USA
# my_function('Korea')       # I am from Korea


#3.
# def addition(param1, param2):
#     print("value of param1 :", param1)             # value of param1 : 5     ,     value of param1 : 6
#     print("value of param2 :", param2)             # value of param2 : 6     ,     value of param2 : 4
#     print("addition of param :", param1+param2)    # addition of param : 11  ,     addition of param : 10

# addition(5,6)
# addition(6,4)


#4. pass by reference :
# def addition(x,y):
#    print('Enter the value of x : ',x)           # Enter the value of x :  10
#    print('Enter the value of y : ',y)           # Enter the value of y :  5
#    print('Total:',x+y)                          # Total: 15

# x=10
# y=5
# addition(x,y)

#5.
# def addition(y,x):
#
#    print('Enter the value of x : ',x)           # Enter the value of x :  5
#    print('Enter the value of y : ', y)          # Enter the value of y :  10
#    print('Total:',x+y)                          # Total: 15
#
# addition(10,5)

#6. # write a python program for simple calculator and perform math operations like :addition,multiplication,
# subtraction, division with help of function.

def addition(x,y):
    print('Enter the value of x : ', x)
    print('Enter the value of y : ', y)
    print('Total:', x + y)
def multiplication(x,y):
    print('Enter the value of x : ', x)
    print('Enter the value of y : ', y)
    print('Total:', x * y)
def substraction(x,y):
    print('Enter the value of x : ', x)
    print('Enter the value of y : ', y)
    print('Total:', x - y)
def division(x,y):
    print('Enter the value of x : ', x)
    print('Enter the value of y : ', y)
    print('Total:', x / y)
print("Select operation")
print("1.Addition")
print("2.Multiplication")
print("3.Subtraction")
print("4.Division")
choice=int(input('Enter the choice:'))
print('Choice : ',choice)
x=int(input('Enter the value of x :'))
y=int(input('Enter the value of y :'))
if choice==1:
    addition(x,y)
elif choice==2:
    multiplication(x,y)
elif choice==3:
    substraction(x,y)
elif choice==4:
    division(x,y)










