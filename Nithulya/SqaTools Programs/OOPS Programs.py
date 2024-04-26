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
