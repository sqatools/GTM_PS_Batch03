"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""


#1). Single Inheritance : class A -> class B

class Father:
    def __init__(self,fname,fbusiness,fhouse):
        self.fname = fname
        self.fbusiness = fbusiness
        self.fhouse = fhouse
    def fatherName(self):
        print("Father Name : ",self.fname)
    def fatherBusiness(self):
        print("Father Business : ",self.fbusiness)
    def fatherHouse(self):
        print("Father House Type : ", self.fhouse)
    def fatherDetails(self):
        self.fatherName()
        self.fatherBusiness()
        self.fatherHouse()


class Son(Father):
    def __init__(self,sName,sEducation,fname,fbusiness,fhouse):
        super().__init__(fname,fbusiness,fhouse)
        self.sName = sName
        self.sEducation = sEducation

    def son_Name(self):
        print("Son name : ", self.sName)
    def son_Education(self):
        print('Son Education : ',self.sEducation)
    def son_Details(self):
        self.son_Name()
        self.son_Education()
    def familyDetails(self):
        self.son_Details()
        self.fatherDetails()

obj1 = Son('Nihith','BTec','Midhun','Developer','Single Home')
obj1.familyDetails()