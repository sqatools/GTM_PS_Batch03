"""
Inheritance: The process of inheriting the properties of the parent class into a child class is called inheritance. The existing class is called a base class or parent class and the new class is called a
subclass or child class or derived class.

Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A, Class B, "Class C -> (Class A, Class B)"
Hierarchical Inheritance : Class A,  Class A -> Class B , Class A -> Class C
"""

# Single Inheritance: In single inheritance, a child class inherits from a single-parent class

class Father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_name(self):
        print("Father Name:", self.fname)

    def show_father_business(self):
        print("Father Business:", self.fbusiness)

    def show_father_house(self):
        print("Father House:", self.fhouse)


class Son(Father):
    def __init__(self, sname, sbusiness, shouse, fname, fbusiness, fhouse):
        super().__init__(fname, fbusiness, fhouse)
        self.sname = sname
        self.sbusiness = sbusiness
        self.shouse = shouse

    def show_son_name(self):
        print("Son Name:", self.sname)

    def show_son_business(self):
        print("Son Business:", self.sbusiness)

    def show_son_house(self):
        print("Son Name:", self.shouse)

    def show_son_family_details(self):  # calling super class methods into subclass method
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()
        self.show_son_business()
        self.show_son_business()


obj1 = Son("Ashok", "Engineer", "2BHK", "Durga", "Fancy", "4BHK")
obj1.show_son_name()
obj1.show_son_business()
obj1.show_son_house()
obj1.show_father_name()
obj1.show_father_business()
obj1.show_father_house()
obj1.show_son_family_details()

# print(obj1.__module__)

