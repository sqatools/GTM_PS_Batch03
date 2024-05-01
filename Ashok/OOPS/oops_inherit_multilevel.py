# Multi level inheritance - class A -> Class B -> Class C

class GFather:
    def __init__(self, gfname, gfbusiness, gfhouse):
        self.gfname = gfname
        self.gfbusiness = gfbusiness
        self.gfhouse = gfhouse

    def show_gf_details(self):
        print("GF name:", self.gfname)
        print("GF business:", self.gfbusiness)
        print("GF house:", self.gfhouse)


class Father(GFather):
    def __init__(self, fname, fbusiness, fhouse, gfname, gfbusiness, gfhouse):
        super().__init__(gfname, gfbusiness, gfhouse)
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
    def __init__(self, sname, sbusiness, shouse, fname, fbusiness, fhouse, gfname, gfbusiness, gfhouse):
        super().__init__(fname, fbusiness, fhouse, gfname, gfbusiness, gfhouse)
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
        self.show_gf_details()
        self.show_father_name()
        self.show_father_business()
        self.show_father_house()
        self.show_son_name()
        self.show_son_business()
        self.show_son_business()


obj1 = Son("Ashok", "Engineer", "2BHK", "Durga", "Fancy", "4BHK",
           "venkat", "Fancy world", "6BHK")
obj1.show_son_name()
obj1.show_son_business()
obj1.show_son_house()
obj1.show_father_name()
obj1.show_father_business()
obj1.show_father_house()
obj1.show_son_family_details()
