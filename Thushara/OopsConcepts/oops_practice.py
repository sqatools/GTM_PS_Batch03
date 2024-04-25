class human(object):
    attr1 ="human"

    def __init__(self, name,Id):
        self.name = name
        self.Id = Id
    def greeting(self):
        print("Hi, {}! Welcome to Python Learning! ".format(self.name))

    def hello(self):
        print("My name is {}".format(self.name))
        print("My ID is {}".format(self.Id))
        print("I'm a {} being!".format(self.__class__.attr1))

    def details(self):
        print("My name is {}".format(self.name))
        print("My Id is {}".format(self.Id))
        print("My post is {}".format(self.post))





obj1 = human("Hari", 23)
obj1.attr1 ="Man"
obj1.name= 'Rajuu'
obj1.hello()

obj2 = human("Arjun",45)
obj2.hello()
obj1.greeting()


