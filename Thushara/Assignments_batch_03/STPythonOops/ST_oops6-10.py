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


