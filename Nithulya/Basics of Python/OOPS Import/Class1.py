class Car:
    def __init__(self,name,model):
        self.name = name
        self.model = model
    def details(self):
        print(f'Car name is {self.name} and model is {self.model}.')
class Feature1(Car):
    def __init__(self,feature1,feature2,name,model):
        super().__init__(name,model)
        self.feature1 = feature1
        self.feature2 = feature2
    def features1(self):
        print(f'{self.feature1} and {self.feature2} are added.')
class Feature2(Feature1):
    def __init__(self,feature3,feature4,feature1,feature2,name,model):
        super().__init__(feature1,feature2,name,model)
        self.feature3 = feature3
        self.feature4 = feature4
    def features2(self):
        print(f'{self.feature3} and {self.feature4} are added.')
    def allDetails(self):
        self.details()
        self.features1()
        self.features2()

if __name__ == '__main__':
    obj1 = Feature2('Head-up-Display','Heated Front Seats','Active Blind Spot Detection',
                'xDrive All-Wheel Drive System','BMW','M8')
    obj1.allDetails()
