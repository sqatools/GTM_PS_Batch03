#Functions:
#1. Arguments:
#1a.Positional Arguments
#1b.Keyword Arguments
#1c. Arbitrary Positional Argumnet
#1d. Arbitrary Keyword Argument
#1e. Default Argument


#1a.Positional Arguments
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

# def addition(x,y):
#     print('Enter the value of x : ', x)
#     print('Enter the value of y : ', y)
#     print('Total:', x + y)
# def multiplication(x,y):
#     print('Enter the value of x : ', x)
#     print('Enter the value of y : ', y)
#     print('Total:', x * y)
# def substraction(x,y):
#     print('Enter the value of x : ', x)
#     print('Enter the value of y : ', y)
#     print('Total:', x - y)
# def division(x,y):
#     print('Enter the value of x : ', x)
#     print('Enter the value of y : ', y)
#     if y==0:
#         print("Division by zero is not defined")
#         exit()
#     else:
#         print('Total:', x / y)
# while True:
#     print("Select operation")
#     print(" 1. Addition\n","2. Multiplication\n","3. Subtraction\n","4. Division")
#     choice=int(input('Enter the choice:'))
#     print('Choice : ',choice)
#     if choice<1 or choice>4:
#         print('Please enter valid choice.')
#         break
#     x=int(input('Enter the value of x :'))
#     y=int(input('Enter the value of y :'))
#     if choice==1 :
#         addition(x,y)
#     elif choice==2:
#         multiplication(x,y)
#     elif choice==3:
#         substraction(x,y)
#     elif choice==4:
#         division(x,y)

#(OR)
# def calculator():
#     def addition(x,y):
#         print('Total:', x + y)
#     def multiplication(x,y):
#         print('Total:', x * y)
#     def substraction(x,y):
#         print('Total:', x - y)
#     def division(x,y):
#         if y==0:
#             print("Division by zero is not defined")
#             exit()
#         else:
#             print('Total:', x / y)
#     while True:
#         print("Select operation")
#         print(" 1. Addition\n","2. Multiplication\n","3. Subtraction\n","4. Division")
#         choice=int(input('Enter the choice:'))
#         print('Choice : ',choice)
#         if choice<1 or choice>4:
#             print('Please enter valid choice.')
#             break
#         x=int(input('Enter the value of x :'))
#         y=int(input('Enter the value of y :'))
#         if choice==1 :
#             addition(x,y)
#         elif choice==2:
#             multiplication(x,y)
#         elif choice==3:
#             substraction(x,y)
#         elif choice==4:
#             division(x,y)
# calculator()


############## Default Argument ###################
# Passing the default value to function parameter
# Rules
# -> if param has default value then no need to pass value for default param while calling the function
# - User can overwrite the default param value while calling the function.
# - Default parameters always set on right of all param,
# - Default parameter should always follow the non default parameters.
##############################################################################
# def addition_value(n1,n2,n3=6):
#     print("Addition :", n1 + n2 + n3)
#
# addition_value(2, 3)            # Addition : 11
# addition_value(2, 4, 3)     # Addition : 9
#################################################################################
#1. Set param data type :

# def multiplication_value(num1 : int, num2: int):
#     print("Multiplication output:", num1*num2)
#
# multiplication_value(3, 2)                 # Multiplication output: 6
# multiplication_value("Hello", 2)           # Multiplication output: HelloHello
# multiplication_value("Hello", "Hari")      # can't multiply sequence by non-int of type 'str'


####################################################################################
#1. Arbitrary Positional Argument of function(*arg/*a/*n).

# -> *args should always come at the end of the param list.
# *args : accepts n number of values and consider tuple of values

#1.
# def functionValue(x,y,*args):
#     print("Value of x :", x)
#     print("Value of y :", y)
#     print("args:",args)

#functionValue(1,2,3,4,5,6,7,8,9,10)  # Value of x : 1, Value of y : 2, args: (3, 4, 5, 6, 7, 8, 9, 10)

#2.
# def functionValue(*args,x,y):
#     print("Value of x :", x)
#     print("Value of y :", y)
#     print("args:",args)
# functionValue(1,2,3,4,5,6,x=7,y=8)    # Value of x : 7, Value of y : 8, args: (1, 2, 3, 4, 5, 6)
######################################################################################################
#### Arbitrary keyword arguments:

# **kwargs : This accepts the param values in key value formate
# default structure is dictionary format to get all the values
#1
# def user_info(**kwargs):
#     print(kwargs)
#     for key, val in kwargs.items():
#         print(key,":", val)
#user_info(name='Hari', email='hari@gmail.com', phone=3245678, address='Kerala')

#2.
# def user_info_details(param1, *args, **kwargs):
#     print("param1 :", param1)            # param1 : 2
#     print("args :", *args)               # args : 3 4 5 6
#     print("kwargs:",kwargs)              # kwargs: {'user_id': 'user001', 'city': 'Kochi', 'state': 'Kerala', 'country': 'India'}
#     for key, val in kwargs.items():
#         print(key,":", val)
# user_info_details(2, 3,4,5,6, user_id='user001', city='Kochi',state='Kerala',country='India')

#3.
# def login(**kwargs):
#     db_username = 'user123'
#     db_password = 'User@123'
#
#     if kwargs['username'] == db_username and kwargs['password'] == db_password:
#         print("Login Successful")
#     else:
#         print("Access Denied")
#
# login(username='user123', password='User@123')           # Login Successful
# login(username='user123', password='User@1234')          # Access


#4. Get return value from the function :
# def calculation(n1,n2,n3):
#     return n1+n2+n3
#
# result = calculation(2,3,5)
# print("Result :", result)                       # Result : 10
#
# def mul_add(n11, n12, n13, m1):
#     result = calculation(n11, n12, n13)
#     print("Multiplication :", result*m1)        # Multiplication : 18
#     return result*m1
#
# mul_result = mul_add(2,1,3,3)
# print("Mul result :", mul_result)                 # Mul result : 18
#
# def multi_ops(n1, n2):
#     return n1+n2, n1*n2, n1-n2
#
# results = multi_ops(40, 20)
# print("Result :", results)                # Result : (60, 800, 20)
#
# add, mul, sub = multi_ops(50, 10)
# print("Addition :", add)                   # Addition : 60
# print("Multiplication :", mul)             # Multiplication : 500
# print("Subtraction :", sub)                # Subtraction : 40

################# Function Documentation ####################################
# def factorials(num1):
#     """
#     This function will get the factorials of any given number and return it
#     :param num1: this is required input number
#     :return: int
#     """
#     fact = 1
#     for i in range(num1, 0, -1):
#         fact = fact*i
#     return fact
#
# print(factorials(5))
# print(factorials.__doc__)
# """
# This function will get the factorials of any given number and return it
#     :param num1: this is required input number
#     :return: int
#
# """
# help(factorials)
#
# """
# Help on function factorials in module __main__:
#
# factorials(num1)
#     This function will get the factorials of any given number and return it
#     :param num1: this is required input number
#     :return: int
#
# """
#
#
#################### Function Recursion #####################################################
#1.
# temp = 1
# def fun1():
#     global temp
#     print(temp)
#     temp = temp + 1
#     if temp == 11:
#         exit()
#     fun1()                 # RecursionError: maximum recursion depth exceeded
# fun1()


#2  Get factorials of all the numbers between 1 to 10
# def fact_value(n):
#     fact = 1
#     for i in range(n,0,-1):
#         fact = fact*i
#     print(f"fact of {n}:", fact)
#     n = n - 1
#     if n == 0:
#         exit()
#     fact_value(n)
#
# fact_value(10)

#(OR)

# def fact1(num):
#     if num<=1:
#         return 1
#     else:
#         return num*fact1(num-1)
# print(fact1(5))
############################################################################################

#### Function Variable :

#1. global variable    :   The variable that can access by every function of the module.
#2.local variable      :   The variable which we declare on function level and can be access inside the function.
#                          scope is limited to function
#3.non-local variable  :   The variable we declare in the outer function, and it is available to access all the
#                          inner functions, then it is known as non-local variable.


#### global variable :

#1.
# var1=4
# def function1():
#     print("________function1_________")
#     var2 = 20           # local variable
#     sum1=var1+var2
#     print("Global variable value var1 :", var1)       # Global variable value var1 : 4
#     print("Local variable value var2 :", var2)        # Local variable value var2 : 20
#     print("Sum :",sum1)                               # Sum : 24
# function1()

#2.
# var1=4
# def function1():
#     print("________function1_________")
#     global var1
#     var1 = 30
#     var2 = 20
#     sum1=var1+var2
#     print("Global variable value var1 :", var1)       # Global variable value var1 : 30
#     print("Local variable value var2 :", var2)        # Local variable value var2 : 20
#     print("Sum :",sum1)                               # Sum : 24
# function1()


#3.
# var1 = 20
# def function1():
#     print("________function1_________")
#     global var1
#     var1 = 25
#     var2 = 30
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 25
#     print("Local variable value var2:", var2)          # Local variable value var2: 30
# def function2():
#     var3 = 40
#     print("________function2_________")
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 25   <=
#     print("local variable value var3 :", var3)         # local variable value var3 : 40
#
# function1()
# function2()

#4.
# var1 = 20
# def function1():
#     print("________function1_________")
#     global var1
#     var1 = 25
#     var2 = 30
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 25
#     print("Local variable value var2:", var2)          # Local variable value var2: 30
# def function2():
#     var3 = 40
#     print("________function2_________")
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 20   <=
#     print("local variable value var3 :", var3)         # local variable value var3 : 40
#
# function2()
# function1()


#5.
# var1 = 200
# def function1():
#     print("________function1_________")
#     global var1
#     var2 = 30
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 200
#     print("Local variable value var2:", var2)          # Local variable value var2: 30
# def function2():
#     print("________function2_________")
#     var3=40
#     print("Global variable value var1 :", var1)        # Global variable value var1 : 200
#     print("local variable value var3 :", var3)         # local variable value var3 : 40
# function1()
# function2()


#6.
var1 = 50
def outer_function():
    var2= 40
    def inner_fun1():
        print("----------Inner Function1---------")
        global var1
        nonlocal var2
        var3 = 80 # local variable
        var2 = 20
        var1 = 200
        print("Global var1 :", var1)           # Global var1 : 200
        print("Non local var2 :", var2)        # Non local var2 : 20
        print("Local var3 :", var3)            # Local var3 : 80

    def inner_fun2():
        print("----------Inner Function2---------")
        var4=100
        print("Global var1 :", var1)          # Global var1 : 200
        print("Non local var2 :", var2)       # Non-local var2 : 20
        print("Local var4 :", var4)           # Local var4 : 100

    inner_fun1()
    inner_fun2()

outer_function()









