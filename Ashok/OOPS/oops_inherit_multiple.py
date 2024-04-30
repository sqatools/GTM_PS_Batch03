# Multiple Inheritance: In multiple inheritance, one child class can inherit from multiple parent classes
# Multiple Inheritance : Class A, Class B, Class C -> (Class A, Class B)
class Mother:
    def __init__(self, mname, mbusiness):
        self.mname = mname
        self.mbusiness = mbusiness

    def show_mother_details(self):
        print("Mother Name :", self.mname)
        print("Mother Business:", self.mbusiness)


class Father:
    def __init__(self, fname, fbusiness, fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse

    def show_father_details(self):
        print("Father Name :", self.fname)
        print("Father Business :", self.fbusiness)
        print("Father House :", self.fhouse)


# MRO : Method Resolution Order
class Son(Father, Mother):

    def __init__(self, sname, seducation, fname, fbusiness, fhouse, mname, mbusiness):
        super().__init__(fname, fbusiness, fhouse)
        self.sname = sname
        self.seducation = seducation
        self.mname = mname
        self.mbusiness = mbusiness

    def show_son_details(self):
        print('Son Name:', self.sname)
        print('Son Education:', self.seducation)

    def show_family_details(self):
        self.show_son_details()
        self.show_father_details()
        self.show_mother_details()


obj1 = Son("Ashok", "B.tech", "Durgarao", "Fancy", "4bHk",
           "Nirmala", "Housewife")
obj1.show_son_details()
obj1.show_father_details()
obj1.show_mother_details()
obj1.show_family_details()
