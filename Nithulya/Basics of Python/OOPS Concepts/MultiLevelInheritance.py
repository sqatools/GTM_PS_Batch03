"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""

#1).Multi Level Inheritance : class A -> class B -> class C
class GrandFather():
    def __init__(self,GfName,GfProperty):
        self.GfName = GfName
        self.GfProperty = GfProperty
    def GFDetails(self):
        print("Grand Father Name :", self.GfName)
        print("Grand Father Property :", self.GfProperty)

class Father(GrandFather):
    def __init__(self,fName,fBusiness,fHouse,GfName,GfProperty):
        super().__init__(GfName,GfProperty)
        self.fName = fName
        self.fBusiness = fBusiness
        self.fHouse = fHouse
    def fatherName(self):
        print("Father Name :", self.fName)

    def fatherBusiness(self):
        print("Father Business :", self.fBusiness)
    def fatherHouse(self):
        print("Father house :", self.fHouse)
    def fatherDetails(self):
        self.fatherName()
        self.fatherBusiness()
        self.fatherHouse()

class Son(Father):
    def __init__(self,sName,sEducation,fName,fBusiness,fHouse,GfName,GfProperty):
        super().__init__(fName,fBusiness,fHouse,GfName,GfProperty)
        self.sName = sName
        self.sEducation = sEducation
    def sonName(self):
        print('Son Name : ',self.sName)

    def sonEducation(self):
        print('Son Education : ', self.sEducation)

    def sonDetails(self):
        self.sonName()
        self.sonEducation()
    def familyDetails(self):
        self.GFDetails()
        self.fatherDetails()
        self.sonDetails()


obj1 = Son('Nihith','BTec','Midhun','Developer','SingleHome','Ram','10Acr')
obj1.familyDetails()




