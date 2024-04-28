"""
class : class is nothing but the blueprint of the object, where we define all feature attributes/methods
        and variable related to the object.
object : Object is entity through which we can access feature functionality of the class
         we can create n number of objects of any specific class.
constructor : constructor which initialize the memory of the class object.
            1. Default constructor : default it being called while creating the object.
            2. Parametrize constructor : constructor which has some parameter to pass while creating
            the object of the class.
variables : variable we declare to set the values in the class
            1. Instance variable : the variable which we declare with the help of self, then it
                                   instance variable.
            2. class variable :

methods :  When we declare any function inside the class then it is known as method.
             1. Instance method
             2. class method
             3. static method
Object is allocated in a particular memory is called Heap Memory. The size of the memory is calculating by constructor.
It depends on the variable which is available in the constructor.

inheritance
polymorphism
data hiding
abstraction
"""

#1).
# class ABC:
#     Team = 'CSK'
#
#     def __init__(self,num1,num2):
#         print('Object Initiated.')
#         self.x = num1
#         self.y = num2
#
#     def greeting(self):
#         print('Welcome to OOPS Concept')
#     def addition(self):
#         print('Addition : ',self.x+self.y)
#
#     def multiplication(self,n1,n2):
#        print('Multiplication : ',n1*n2)
#
#     def printIPLteamName(self):
#        print("IPL Team Name : ",self.Team)
#     @classmethod
#     def showClassVeriable(cls):
#         print('Class veriable value : ',cls.Team)
#         cls.Team = 'Chennai'
#         print('Class veriable value : ', cls.Team)
#
#     @staticmethod
#     def showFactorials(num):
#         fact = 1
#         for i in range(num,0,-1):
#             fact = fact*i
#         print(f"Factorials of {num}: ", fact)
#
#     def getFactorial(self,num):
#         fact = 1
#         for i in range(num,0,-1):
#             fact = fact*i
#         print(f"Factorials of {num}: ", fact)
#     def show_msg(self):
#         print("Good Morning")
#     def show_team_name(self):
#         print("Call by class name :", ABC.Team)
#         print("Call by class object (self) :", self.Team)
#
#
# obj1 = ABC(30,40)                     # Object Initiated.
# obj1.greeting()                                   # Welcome to OOPS Concept
# obj1.addition()                                   # Addition :  70
# obj1.multiplication(2,4)                   # Multiplication :  8
# print('Team Name : ',obj1.Team)                   # Team Name :  CSK
# obj1.printIPLteamName()                           # IPL Team Name :  CSK
# obj1.Team = 'Mumbai'
# obj1.printIPLteamName()                           # IPL Team Name :  Mumbai
#
# obj2 = ABC(20,30)              # Object Initiated.
# obj2.printIPLteamName()                    # IPL Team Name :  CSK
# obj2.Team = "RCB"
# obj2.printIPLteamName()                    # # IPL Team Name :  RCB
# obj2.showClassVeriable()                   # Class veriable value :  CSK
# print('Team : ',ABC.Team)                  # Class veriable value :  Chennai
#
# obj1.showFactorials(5)                     # Factorials of 5:  120
# obj1.getFactorial(5)                       # Factorials of 5:  120
# obj1.show_msg()                            # Good Morning
# obj1.show_team_name()                      # Call by class name : Chennai, Call by class object (self) : Mumbai

#2).
# class ABC:
#     Team = 'CSK'
#
#     def __init__(self,num1,num2):
#         print('Object Initiated.')
#         self.x = num1
#         self.y = num2
#     def addition(self):
#         print('Addition : ',self.x+self.y)
#     def multiplication(self,n1,n2):
#        print('Multiplication : ',self.x*self.y)
#        print('Multiplication : ', n1*n2)
#     @classmethod
#     def showClassVeriable(cls):
#             print('Class veriable value : ',cls.Team)
#             cls.Team = 'Chennai'
#             print('Class veriable value : ', cls.Team)
#     @staticmethod
#     def showFactorials(num):
#             fact = 1
#             for i in range(num,0,-1):
#                 fact = fact*i
#             print(f"Factorials of {num}: ", fact)
#     def internalCalling(self):
#         self.addition()
#         self.multiplication(2,6)
#         self.showClassVeriable()
#         self.showFactorials()
#
# obj1 = ABC(2,3)
# obj1.internalCalling()




#3).
# class ABC:
#     Team = 'CSK'
#
#     def __init__(self,num1,num2):
#         print('Object Initiated.')
#         self.x = num1
#         self.y = num2
#
#     def greeting(self):
#         print('Welcome to OOPS Concept')
#     def addition(self):
#         print('Addition : ',self.x+self.y)
#
# obj1 = ABC(2,4)             # Object Initiated.
# obj1.greeting()                        # Welcome to OOPS Concept
# obj1.addition()                        # Addition :  6
# print(obj1.__module__)                 # __main__
# print(obj1.__class__)                  # <class '__main__.ABC'>
# print(obj1.__doc__)                    # None
#
# val1 = obj1.__getattribute__('x')
# print("Value of X : ", val1)           # Value of X :  2
# val2 = obj1.__getattribute__('y')
# print("Value of Y : ", val2)           # Value of Y :  4
#
# obj1.__setattr__('x',10)
# val1 = obj1.__getattribute__('x')
# print("Value of X : ", val1)           # Value of X :  10
# val2 = obj1.__getattribute__('y')
# print("Value of Y : ", val2)           # Value of Y :  4
# obj1.addition()                        # Addition :  14

#4).
# class FirstClass():
#     car='Audi'
#     model='A5'
#     def __init__(self):
#         self.car1="BMW"
#         self.model1='m5'
#     def firstMethod(self):
#         print("Car is ",self.car1," ","and model is ",self.model1)
#     def updatedMethod(self,car2):
#         self.car1=car2
#         print("Car is ",self.car1)
#     @ classmethod
#     def classMethod1(cls,car,model):
#         print('Car is ',FirstClass.car,'and model is ',FirstClass.model)
#         cls.car2 = car
#         cls.model2 = model
#         print('Car is ', cls.car2, 'and model is ',cls.model2)
# obj1=FirstClass()
# obj1.firstMethod()
# obj1.updatedMethod('Audi')
# obj1.classMethod1('Honda','Civic Sedan')