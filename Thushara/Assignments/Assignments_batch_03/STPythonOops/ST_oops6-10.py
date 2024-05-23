# 6:  Python oops program to create a class with the class method.

# 7:Write a  Python Class to get the class name and module name.

class Plants:
    type ="Indoor"

    @classmethod
    def watering(cls):
        print(cls.type, "plants need less water.")

print(Plants.type)
print(Plants.watering()) #Indoor plants need less water.
pl = Plants()
print("Class name ", pl.__class__.__name__) #Class name  Plants
print("Module Name", pl.__module__) #Module Name __main__

# 8: Write a Python Class object under syntax if __name__ == ‘__main__’.
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def hello(self):
        print("I'm a ",self.breed)
        print("My name is ",self.name)

    @staticmethod
    def pet():
        favorite = "Dogs"
        print(favorite, "are favorite pets!")
if __name__=='__main__':
    dog1 = Dog("Tommy","Bull Dog")

    dog2 = Dog("Jimmy","German Shepherd")

    dog1.hello()
    dog2.hello()
    Dog.pet()
    dog1.pet()


# 9). Python class with Single Inheritance.
class Birds:
    def characteristics(self):
        print("All birds have feathers and lay eggs.")

class FlightlessBirds(Birds):
    def flightless(self):
        print("Ostriches , kiwi, Cassowaries are some of the birds that do not fly.")

bird = FlightlessBirds()
bird.characteristics() #All birds have feathers and lay eggs.
bird.flightless()#Ostriches , kiwi, Cassowaries are some of the birds that do not fly.


# 10). Python Class with Multiple Inheritance.

class Person:
    def personal_details(self, name, email,phone):
        print("Name: ", name, "Email :", email, "Phone :",phone)

class Company:
    def company_details(self, company_name):
        print("Company :",company_name)

class Employee(Person,Company):
    def emplyee_details(self,salary,id,post):
        print("Salary :", salary , "Id :", id, "Post :",post)

emp1 = Employee()

emp1.personal_details("Hari", "hari@gmail.com",56745343) #Name:  Hari Email : hari@gmail.com Phone : 56745343
emp1.company_details("SouthMiddle")  #Company : SouthMiddle
emp1.emplyee_details(50000,67 ,"Teacher")  #Salary : 50000 Id : 67 Post : Teacher


