"""
Topics:
Variables : Instance Variables, Class/Static Variables.
Methods: Instance methods, Static Methods
"""

""""
Instance variable:
1. If the value of a variable varies from object to object, then such variables are called instance variables.
2. We can access instance variable in two ways.
        1.self.variableName= variableName
        2.obj.variable = value
3. To update an instance variable we can use obj.variable = value
4. Note: Instance variables always created for object.
5. We can access, update, delete, create object by using instance variable.
"""


# Instance Variable #
class B:
    def __init__(self, a, b):
        self.instanceVariable1 = a
        self.instanceVariable2 = b

    # Accessing & Modify the instance variables in instance method.
    def updateVariable(self, newValue1, newValue2):
        self.instanceVariable1 = newValue1
        self.instanceVariable2 = newValue2


# 1. Accessing the instance variable using object
obj2 = B(10, 20)
print(obj2.instanceVariable1, obj2.instanceVariable2)

# 2. Updating an existing instance variable using object
obj2.instanceVariable1 = 15
obj2.instanceVariable2 = 16
print(obj2.instanceVariable1, obj2.instanceVariable2)

# 3. Updating an instance variable in method using object
obj2.updateVariable(17, 18)
print(obj2.instanceVariable1, obj2.instanceVariable2)

# 4. Creating a new instance variable using same object.
obj2.instanceVariable3 = 100
obj2.instanceVariable4 = 200
print(obj2.instanceVariable3, obj2.instanceVariable4)

# 5. Creating an instance variable using different object and applicable to that object only.
obj3 = B(300, 400)
print(obj3.instanceVariable1, obj3.instanceVariable2)

"""
Class/Static variable:
1. The variable which we declared outside the methods and inside the class is called Class/Static variable.
2. We can create class variable outside class using className.variableName
3. We can access the class variable in two ways. 1. Using className.variableName 2. Using obj of same class
Note: Best practice to use class variables with class method.
4. If we want to access the class variables in class methods using className.variableName
5. We can Create, update, access, delete class variables using class name. But using object we can only access
the class variables.
6. In Instance method we can access the class variable using self and class name.
"""


# Example 1: Class Variable #
class A:
    staticVariable1 = 10  # Class variable
    staticVariable2 = 20  # Class variable

    def sampleMethod(self):
        print("Sample Method")

    # Accessing class variable in instance method using self and class name.
    def method1(self):
        print(self.staticVariable1, self.staticVariable2)  # with self
        print(A.staticVariable1, A.staticVariable2)        # with classname

    # Accessing class variable in class method using class name.
    @classmethod
    def method2(cls):
        print(cls.staticVariable1, cls.staticVariable2)  # with classname


# 1. Creating a new class variable using class name #
A.staticVariable3 = 30

# 2. Accessing class variable using class name #
print(A.staticVariable1)
print(A.staticVariable2)
print(A.staticVariable3)

# 3. Accessing class variable using obj #
obj1 = A()
print(obj1.staticVariable1)
print(obj1.staticVariable2)
print(obj1.staticVariable3)

# 4. Accessing class variable in instance method using self and class name.
obj1.method1()

# 5. Accessing class variable in class method using cls.
obj1.method2()

# 6. Updating class variable using class name.
A.staticVariable1 = 100
print(A.staticVariable1)

""" 
1. Instance methods: By default the methods we created in class is called instance methods.
2. Instance methods create/access/modify/delete the objects attributes.
3. Instance methods performs operations on object attributes.
"""


# 1. Creating instance methods
class Employee:
    A = 10

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def getEmployeeName(self):
        print(self.name)

    def getClassVariable(self):
        print(self.A)

    # Updating instance variable in instance method
    def updateEmployeeName(self, new_name):
        self.name = new_name

    # Updating class variable in instance method using self.__class__.ClassName
    def updateClassVariable(self, new_value):
        self.__class__.A = new_value


emp1 = Employee("Pavan", 1001, 20000)
print(emp1.name, emp1.emp_id, emp1.salary)
emp1.getEmployeeName()

emp2 = Employee("Ravi", 1002, 21000)
print(emp2.name, emp2.emp_id, emp2.salary)
emp2.getEmployeeName()
emp2.getClassVariable()

# 2. Updating instance variables using instance methods
emp2.updateEmployeeName('Pusarla')
emp2.getEmployeeName()

# 3. Updating class variable in instance methods:  self.__class__.classVariable=value
emp2.updateClassVariable(100)
print(Employee.A)

"""
Class Method: 
1. Used to access or modify the class state. In method implementation, if we use only class variables, 
then such type of methods we should declare as a class method. 
2. It should have cls parameter and the decorator @classmethod to method.
3. To perform operations on class level variables & to deal with factory methods.
"""


class Student1:
    college = "ABC"

    @classmethod
    def classmethod1(cls, newValue1):
        print(cls.college)
        cls.college = newValue1
        print("Classmethod 1 created successfully")
        print(cls.college)


Student1.classmethod1("DEF")  # calling class method with classname
stud = Student1()
stud.classmethod1("GHI")  # calling class method with object

"""
Static Method: 
1. A static method is a general utility method that performs a task in isolation. Inside this method, 
we don’t use instance or class variable because this static method doesn’t take any parameters like self and cls
2. Static method doesn't perform operations on objects and variables.
3. Static method can be called as utility function also.
"""


class Employee:
    @staticmethod
    def sample(x):
        print('Inside static method', x)


# call static method
Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)


# Example 2:

class Calculator:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def sub(a, b):
        return a - b

    @staticmethod
    def mul(a, b):
        return a * b

    @staticmethod
    def div(a, b):
        return a / b


a = Calculator.add(2, 3)
b = Calculator.sub(3, 2)
c = Calculator.mul(4, 5)
d = Calculator.div(6, 2)
print(a, b, c, d)
