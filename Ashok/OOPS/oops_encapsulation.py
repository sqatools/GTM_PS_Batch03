"""
Encapsulation in Python describes the concept of bundling data members and methods within a single unit.
When you create a class, it means you are implementing encapsulation.

Datahiding : In python data hiding is achieved by defining the variable and methods with single under score
and double underscore as prefix.

1. If we defined any variable/method name with single underscore as prefix then those class will not available in
suggestion list, but we can directly access with the class object.
(protected - Accessible within the class and its sub-classes)

2. If we defined any variable/method name with double underscore as prefix then those class members will not available
in suggestion list, but we can directly access with the class name. (private - Accessible within the class)
e.g _<classname>__<method/variable>

"""


# Public Member: Public data members are accessible within and outside a class. All member variables of the class
# are by default public.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show(self):
        # accessing public data members in method
        print("Name: ", self.name, 'Salary:', self.salary)


# creating object of a class
emp = Employee('Jessa', 10000)

# accessing public data members
print(emp.name, emp.salary)

# calling public method of the class
emp.show()


# 2. Private Members - We can protect variables in the class by marking them private. To define a private variable
# add two underscores as a prefix at the start of a variable name. Private members are accessible only within the class,
# and we can’t access them directly from the class objects.

# Ex 1: Trying to access private member outside class it will throw error.
class Student1:
    def __init__(self, name, salary):
        self.__salary = None
        self.name = name
        self.__salary = salary  # private variable


# creating object of a class
stud1 = Student1("Ashok", 7000)


# accessing private data members
# print("Salary is:", stud1.__salary)  # AttributeError: 'Student' object has no attribute '__salary'

# Ex 2: Trying to access private member with in the class, it will be accessible
class Student2:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self.name = name
        # private member
        self.__salary = salary

    # public instance methods
    def show(self):
        # private members are accessible from a class
        print("Name: ", self.name, 'Salary:', self.__salary)


# creating object of a class
stud2 = Student2('Jessa', 10000)

# calling public method of the class
stud2.show()


# Ex 3: Trying to access private member

class Student3:
    # constructor
    def __init__(self, name, salary):
        # public data member
        self._Student3__salary = None
        self.name = name
        # private member
        self.__salary = salary


# creating object of a class
stud3 = Student3('Jessa', 20000)

print('Name:', stud3.name)
# direct access to private member using name mangling
print('Salary:', stud3._Student3__salary)


# Protected Member are accessible within the class and also available to its sub-classes. To define a
# protected member, prefix the member name with a single underscore_
# Ex: Protected member in inheritance.

# base class
class Company:
    def __init__(self):
        # Protected member
        self._project = "NLP"


# child class
class Employee(Company):
    def __init__(self, name):
        self.name = name
        Company.__init__(self)  # calling parent class constructor with class name.

    def show(self):
        print("Employee name :", self.name)
        # Accessing protected member in child class
        print("Working on project :", self._project)


c = Employee("Jessa")
c.show()

# Direct access protected data member
print('Project:', c._project)


# Example from Deepesh Python class #
class Car:
    def __init__(self, car_name, car_comp, car_price):
        self.car_name = car_name
        self._car_company = car_comp
        self.__car_price = car_price

    def show_car_name(self):
        print("Car name :", self.car_name)

    def _show_car_company(self):
        print("Car company :", self._car_company)

    def __show_car_price(self):
        print("Car price :", self.__car_price)


obj = Car('Harier', 'TATA', '25L')

obj._show_car_company()   # Accessing the protected method
obj._Car__show_car_price()   # Accessing the private method with class name.
print(dir(obj))
