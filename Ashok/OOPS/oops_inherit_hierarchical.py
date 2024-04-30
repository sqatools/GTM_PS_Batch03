# Hierarchical Inheritance: One parent class and can be accessed by multiple child classes.
# Hierarchical Inheritance : Class A,  Class A -> Class B , Class A -> Class C

class Vehicle:
    @staticmethod
    def info():
        print("This is Vehicle")


class Car(Vehicle):
    def car_info(self, name):
        print("Car name is:", name)
        Vehicle.info()   # calling static method in instance method using classname
        self.info()      # calling static method in instance method using self


class Truck(Vehicle):
    def truck_info(self, name):
        print("Truck name is:", name)


obj1 = Car()
obj1.info()
obj1.car_info('BMW')

obj2 = Truck()
obj2.info()
obj2.truck_info('Ford')
