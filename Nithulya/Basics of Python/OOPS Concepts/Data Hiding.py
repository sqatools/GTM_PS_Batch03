################### Data Encapsulation ###############################################################
"""
Datahiding : In python data hiding is achived by defining the variable and methods with single under score
            and double underscore as prefix.
            1. If we defined any variable/method name with single underscore as prefix then those class
               will not available in suggestion list, but we can directly access with the class object.

            2. If we defined any variable/method name with double underscore as prefix then those class members
               will not available in suggestion list, but we can directly access with the class name.
               e.g _<classname>__<method/variable>

"""

class Car:
    def __init__(self, carName, carComp, carPrice):
        self.carName = carName
        self._carComp = carComp
        self.__carPrice = carPrice

    def carName(self):
        print("Car Name :", self.carName)
    def _carCompany(self):
        print("Car Company :", self._carComp)
    def __carPrice(self):
        print("Car Price :", self.__carPrice)

if __name__ == "__main__":
    obj1 = Car('Harier', 'TATA', '25L')
    obj1._carCompany()
    obj1._Car__carPrice()
    






