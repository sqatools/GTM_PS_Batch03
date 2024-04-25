"""
class : class is nothing but the blueprint of the object, where we define all feature attributes/methods
        and variable related to the object
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
inheritance
polymorphism
data hiding
abstraction
"""

#1).
# class ABC:
#
#     Team = "CSK" # class variable
#
#     def __init__(self, num1, num2):
#         print("objected initiated")
#         self.x = num1  # instance variable
#         self.y = num2  # instance variable
#
#     # instance method
#     def greeting(self):
#         print("Welcome to OOPS concept")
#
#     # instance method
#     def addition(self):
#         print("Addition :", self.x + self.y)
#
#     def multiplication(self, n1, n2):
#         print("multiplication :", n1*n2)
#
#     def print_ipl_team_name(self):
#         print("IPL Team name :", self.Team)
#
#
#     @classmethod
#     def show_class_variable(cls):
#         print("class variable value :", cls.Team)
#
#
# obj = ABC(30, 40) # creating the object of the class
# obj.greeting()
# obj.addition()
# obj.multiplication(5, 6)
# print("Team name :", obj.Team)
#
# obj.print_ipl_team_name()
# obj.Team = "Mumbai"
#
# obj.print_ipl_team_name()
#
# print("_"*50)
# obj2 = ABC(350, 400)
# obj2.print_ipl_team_name()
# obj2.Team = "RCB"
# obj2.print_ipl_team_name()
# obj2.show_class_variable()


#2).
# class Car:
#     company ='BMW'
#     model='M5'
#     price=2500000000
#     color ='Black'
#     def displayDetails(self):
#         print("Printing all details")
# obj1 = Car()
# print('Company :',Car.company)
# print('Model :',Car.model)
# print('Price :',Car.price)
# print('Color :',Car.color)
# obj1.displayDetails()

#3).
class Employee:
    company='ABCD Technologies'
    location='Kerala'
    def __init__(self,id,name,salary):
        self.empID = id
        self.empName=name
        self.empSalary=salary
    def details(self,location):
        self.location1=location
        print('Good Morning!!',self.empName)
obj1=Employee('AB123','NIVYA',25000)
print('Employee ID :',obj1.empID,',','Employee Name : ',obj1.empName,',','Employee Salary : ',obj1.empSalary)
print('Company :',Employee.company)
print('Location :',Employee.location)
obj1.details('Kannur')
obj2= Employee('CD123','Arya',20000)

