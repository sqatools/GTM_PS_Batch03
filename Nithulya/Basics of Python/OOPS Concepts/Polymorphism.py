"""
polymorphism : when one method perform the multiple tasks, then it is known as polymorphism

method overloading : When one class have two methods with same name and different parameters, then it
                     is known as method overloading. but python does not allow the method overloading
                     it only consider the latest defined method.
method overriding : when child class and parent class have same method name with same parameters then
                    child class method will override the parent class method, and it is known as method
                    overriding.
operator overloading :
"""

##################### Method Overloading ##########################################
# class Addition:
#     def findSum(self,a,b):
#         print('Result = ',a+b)
#     def findSum(self,a,b,c):
#         print('Result = ', a+b+c)
# obj1 = Addition()
# #obj1.findSum(2,3)                # TypeError: Addition.findSum() missing 1 required positional argument: 'c'
# obj1.findSum(2,3,4)               # Result =  9

# We can achieve this using *args
#b).
# class Addition:
#     def findSum(self,a,b,c=None):
#         if c== None:
#             print('Result1 = ', a + b )
#         else:
#             print('Result1 = ', a+b+c)
# obj1 = Addition()
# obj1.findSum(2,3,4)   # Result1 =  9
# obj1.findSum(2,4)        # Result1 =  6


###################### Method Overriding ######################################################
# class A:
#     def func1(self):
#         print('Function1 is working')
#     def func(self):
#         print('Function is working from class A')
# class B(A):
#     def func3(self):
#         print('Function3 is working')
#     def func(self):
#         print('Function is working from class B')
# obj1 = B()
# obj1.func1()
# obj1.func3()
# obj1.func()       #Func is overring the parent class function.

#2).
# class A:
#     def func(self):
#         print('Function1 is working')
#     def func(self):
#         print('Function2 is working')
#     def func(self):
#         print('Function3 is working')
# obj1 = A()
# obj1.func()         # Function3 is working

############################ Operator Overloading ###################################################
#1).
#print(5+2)                 #print(int.__add__(5,2))

#2).
#print('a'+'bc')            # abc

#3)
# n1 = 20
# n2 = 10
# print("Addition : ", n1+n2)
# print("addition :", n1.__add__(n2))
# print(dir(int))

#4).
# s1 = 'Hello'
# s2 = 'Good Morning'
# print("Add String :", s1+s2)
# print("Add String :", s1.__add__(s2))
# print(dir(str))

#5).
# print("Multiplication :", n1*n2)
# print("Multiplication :", n1.__mul__(n2))
# print(dir(list))

#6).
# class Product:
#     def __init__(self,name,price):
#         self.name = name
#         self.price = price
#     def __add__(self, other):
#         print('Addition operator called')
#         totalPrice = self.price + other.price
#         print('Total : ',totalPrice)
#     def __sub__(self, other):
#         print('Substract operator called')
#         priceDifference = self.price - other.price
#         print('Price Difference : ', priceDifference)
# obj1 = Product('Samsung Galaxy S24',85000)
# obj2 = Product('iPhone Pro Max',95000)
# obj1+obj2            # Addition operator called, Addition operator called
# obj1-obj2            # Substract operator called, Price Difference :  -10000



