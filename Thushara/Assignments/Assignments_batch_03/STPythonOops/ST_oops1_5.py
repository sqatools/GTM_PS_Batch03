# 1: Python oops program to create a class with a constructor
# 5: Python oops program to create a class with a static method.

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

dog1 = Dog("Tommy","Bull Dog")

dog2 = Dog("Jimmy","German Shepherd")

dog1.hello()
dog2.hello()
Dog.pet()
dog1.pet()

# 2). Python oops program to create a class with an instance variable.

class Bird:
    def __init__(self):
        self.name = "Rio"
        self.greeting ="Good Morning you all!"

bird = Bird()
print(bird.name)
print(bird.greeting)



# 3). Python oops program to create a class with Instance methods.

class Games:

    def __init__(self, name, sport):
        self.name = name
        self.sport = sport

    def player(self):
        print("I'm a ", self.name,".")
        print ("I used to a", self.sport ,"player!")

    def change(self, new_sport):
        self.new_sport = new_sport
        print("I am a ",new_sport, "player now.")



p1= Games("Hari","cricket")
p1.player()
p1.change("soccer")



# 4). Python oops program to create a class with class variables.

class Human:
    behavior = "civilized"

print(Human.behavior)


