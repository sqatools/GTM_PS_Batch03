"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""
#1). Hierarchical Inheritance : Class A -> Class B , Class A -> Class C

class Father:
    def __init__(self,fName,fBusiness,fHouse):
        self.fName = fName
        self.fBusiness = fBusiness
        self.fHouse = fHouse
    def fatherDetails(self):
        print("Father Name :", self.fName)
        print("Father Business :", self.fBusiness)
        print("Father House :", self.fHouse)
class Son1(Father):

    def __init__(self,sName1,sEducation1,fName,fBusiness,fHouse):
        super().__init__(fName,fBusiness,fHouse)
        self.sName1 = sName1
        self.sEducation1 = sEducation1
    def son1Details(self):
        print('Son Name : ', self.sName1)
        print('Son Education : ', self.sEducation1)
    def familyDetails1(self):
        self.fatherDetails()
        self.son1Details()

class Son2(Father):
    def __init__(self,sName2,sEducation2,fName,fBusiness,fHouse):
        super().__init__(fName,fBusiness,fHouse)
        self.sName2 = sName2
        self.sEducation2 = sEducation2
    def son2Details(self):
        print('Son Name : ', self.sName2)
        print('Son Education : ', self.sEducation2)
    def familyDetails2(self):
        self.fatherDetails()
        self.son2Details()


obj1 = Son1('Nihith','BTec','Midhun','Developer','Single Home')
obj1.familyDetails1()
print('-'*50)
obj2 = Son2('Niharika', 'MBBS', 'Midhun', 'Developer', 'Single Home')
obj2.familyDetails2()
