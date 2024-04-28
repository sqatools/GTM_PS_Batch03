#1). Python oops program to create a class with the constructor.
# class FirstClass():
#     def __init__(self,Name,Location):
#         self.name=Name
#         self.location=Location
#     def firstMethod(self):
#         print("Hi Good Morning",self.name)                  # Hi Good Morning Nivya
#         print("Your location is ", self.location)           # Your location is  Kerala
# obj1=FirstClass('Nivya','Kerala')
# obj1.firstMethod()
import math


#2). Python oops program to create a class with an instance variable.
# class FirstClass():
#     def __init__(self):
#         self.car1="BMW"
#         self.model1='m5'
# obj1=FirstClass()
# print('Car : ',obj1.car1)                # Car :  BMW
# print('Model :',obj1.model1)             # Model : m5


#3). Python oops program to create a class with Instance methods.
# class FirstClass():
#     def __init__(self):
#         self.car1="BMW"
#         self.model1='m5'
#     def firstMethod(self):
#         print("Car is ",self.car1," ","and model is ",self.model1)
#     def updatedMethod(self,car2):
#         self.car1=car2
#         print("Car is ",self.car1)
#
# obj1=FirstClass()
# obj1.firstMethod()              # Car is  BMW   and model is  m5
# obj1.updatedMethod('Audi')      # Car is  Audi

#4). Python oops program to create a class with class variables.
# class FirstClass():
#     car='BMW'
# print(FirstClass.car)                     # BMW

#5). Python oops program to create a class with a static method.
# class FirstClass():
#     @ staticmethod
#     def staticMethod1():
#         print("Hello Good Morning!!")
# FirstClass.staticMethod1()                 # Hello Good Morning!!

#6).  Python oops program to create a class with the class method.
# class FirstClass():
#     name='Nivya'
#     @ classmethod
#     def classMethod1(cls):
#         print("Hello Good Morning!!",cls.name)   # Hello Good Morning!! Nivya
# FirstClass.classMethod1()

#7). Write a  Python Class to get the class name and module name.
# class FirstClass:
#     pass
# obj1= FirstClass()
# print(obj1.__module__)                    # __main__
# print(obj1.__class__.__name__)            # FirstClass

#8) Write a Python Class object under syntax if __name__ == ‘__main__’.
# class FirstClass:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def details(self):
#         print(f'Hi {self.name}, your age is {self.age}.')
# if __name__ == '__main__':
#     obj1=FirstClass('Nihith',5)
#     obj1.details()


#9). Python class with Single Inheritance.
# class Person:
#     def __init__(self,salary,designation):
#         self.salary = salary
#         self.designation = designation
#     def displayEmployee(self):
#         print(f'Your salary is {self.salary} and your designation is {self.designation}')
# class Employee(Person):
#     def __init__(self,name,id,salary,designation):
#         super().__init__(salary,designation)
#         self.name = name
#         self.id=id
#     def dislpayDetails(self):
#         print(f'Name is {self.name} and  ID is {self.id}')
#         self.displayEmployee()
#
# obj1=Employee('Nihith','AB123',25000,'Developer')
# obj1.dislpayDetails()



# 10). Python Class with Multiple Inheritance.
# class Dance:
#     def __init__(self,item1,item2):
#         self.item1 = item1
#         self.item2 = item2
#     def danceDetails(self):
#         print(f'I know {self.item1} and {self.item2}.')
# class Athelete:
#     def __init__(self,sport1,sport2):
#         self.sport1 = sport1
#         self.sport2 = sport2
#     def sportsDetails(self):
#         print(f'I know {self.sport1} and {self.sport2}.')
# class Student(Dance,Athelete):
#     def __init__(self,name,activity1,activity2,item1,item2,sport1,sport2):
#         super().__init__(item1,item2)
#         self.name = name
#         self.activity1= activity1
#         self.activity2 = activity2
#         self.sport1 = sport1
#         self.sport2 = sport2
#     def studentActivities(self):
#         print(f'My name is {self.name}.I like {self.activity1} and {self.activity2}.')
#         self.danceDetails()
#         self.sportsDetails()
#
# obj1 = Student('Nivya','Painting','Sewing','Keralanadanam','Mohiniyattam','Soccer','Cricket')
# obj1.studentActivities()


# 11). Python Class with Multilevel Inheritance.
# class Car:
#     def __init__(self,name,model):
#         self.name = name
#         self.model = model
#     def details(self):
#         print(f'Car name is {self.name} and model is {self.model}.')
# class Feature1(Car):
#     def __init__(self,feature1,feature2,name,model):
#         super().__init__(name,model)
#         self.feature1 = feature1
#         self.feature2 = feature2
#     def features1(self):
#         print(f'{self.feature1} and {self.feature2} are added.')
# class Feature2(Feature1):
#     def __init__(self,feature3,feature4,feature1,feature2,name,model):
#         super().__init__(feature1,feature2,name,model)
#         self.feature3 = feature3
#         self.feature4 = feature4
#     def features2(self):
#         print(f'{self.feature3} and {self.feature4} are added.')
#     def allDetails(self):
#         self.details()
#         self.features1()
#         self.features2()
# obj1 = Feature2('Head-up-Display','Heated Front Seats','Active Blind Spot Detection',
#                 'xDrive All-Wheel Drive System','BMW','M8')
# obj1.allDetails()


#12). Python Class with Hierarchical Inheritance.
# class Retailer:
#     def __init__(self,name):
#         self.name = name
#     def retailer1(self):
#         print(f'{self.name}, is an American multinational technology company.')
# class Service1(Retailer):
#     def __init__(self,service1,name):
#         super().__init__(name)
#         self.service1 = service1
#     def services1(self):
#         print(f'We are the largest {self.service1} provider')
#     def details1(self):
#         self.retailer1()
#         self.services1()
# class Service2(Retailer):
#     def __init__(self,service2,name):
#         super().__init__(name)
#         self.service2 = service2
#     def services2(self):
#         print(f'We are the largest {self.service2} retailer')
#     def details2(self):
#         self.retailer1()
#         self.services2()
# obj1 = Service1('technology','Amazon')
# obj1.details1()
# obj2 = Service2('online','Amazon')
# obj2.details2()

#(OR)

# class Retailer:
#     def retailer1(self):
#         print('Amazon, is an American multinational technology company.')
# class Service1(Retailer):
#     def services1(self):
#         print('We are the largest, Technology provider')
# class Service2(Retailer):
#     def services2(self):
#         print('We are the largest, online retailer')
# obj1 = Service1()
# obj1.retailer1()
# obj1.services1()
# obj2 = Service2()
# obj2.retailer1()
# obj2.services2()

#23). Set Instance variable data with setattr and getattr methods.
# class Retailer:
#     def __init__(self,ret1):
#         self.ret1 = ret1
#     def retailer1(self):
#         print(f'{self.ret1}, is an American multinational technology company.')
# obj1 = Retailer('Amazon')
# obj1.retailer1()                              # Amazon, is an American multinational technology company.
# obj1.__setattr__('ret1','Best Buy')
# value1 = obj1.__getattribute__('ret1')
# print('Updated Retailer : ',value1)           # Updated Retailer :  Best Buy
# obj1.retailer1()                              # Best Buy, is an American multinational technology company.


#25). Create a Python class called Rectangle with attributes length and width.
# Include methods to calculate the area and perimeter of the rectangle.
# class Rectangle:
#     def __init__(self,length,wideth):
#         self.length = length
#         self.width = wideth
#     def area(self):
#         print('Area of Retangle : ',(self.length*self.width))
#     def perimeter(self):
#         print('Perimeter of Retangle : ', 2*(self.length + self.width))
# obj1= Rectangle(2,3)
# obj1.area()
# obj1.perimeter()

#26). Create a Python class called Circle with attributes radius.
#Include methods to calculate the area and circumference of the circle.
class Circle:
    value = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print('Area of Circle : ',Circle.value *((self.radius)**2))          #(OR) math.pi *((self.radius)**2)
    def circumference(self):
        print('Circumference of Circle : ', 2*(Circle.value * self.radius))   #(OR) 2*(math.pi * self.radius)
obj1= Circle(6)
obj1.area()
obj1.circumference()