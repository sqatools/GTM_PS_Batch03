"""
Single Inheritance : class A -> class B
Multi Level Inheritance : class A -> class B -> class C
Multiple Inheritance : Class A -> Class B, Class C -> Class B
Hierarchical Inheritance : Class A -> Class B , Class A -> Class C
"""
#1).Multiple Inheritance : Class A -> Class B, Class C -> Class B

class Mother:
    def __init__(self,mName,mBusiness):
        self.mName = mName
        self.mBusiness = mBusiness
    def motherDetails(self):
        print("Mother Name :", self.mName)
        print("Mother Business:", self.mBusiness)

class Father:
    def __init__(self,fName,fBusiness,fHouse):
        self.fName = fName
        self.fBusiness = fBusiness
        self.fHouse = fHouse
    def fatherDetails(self):
        print("Father Name :", self.fName)
        print("Father Business :", self.fBusiness)
        print("Father House :", self.fHouse)

class Son(Father,Mother):

    def __init__(self,sName,sEducation,fName,fBusiness,fHouse,mName,mBusiness):
        super().__init__(fName,fBusiness,fHouse)
        self.sName = sName
        self.sEducation = sEducation
        self.mName = mName
        self.mBusiness=mBusiness

    def sonDetails(self):
        print('Son Name : ', self.sName)
        print('Son Education : ', self.sEducation)
    def familyDetails(self):
        self.motherDetails()
        self.fatherDetails()
        self.sonDetails()

obj1 = Son('Nihith','BTec','Midhun','Developer','Single Home','Nivya','Engineer')
obj1.familyDetails()


