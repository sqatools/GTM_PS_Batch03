class School:
    def __init__(self,school_name, school_address,school_phone):
        self.school_name = school_name
        self.school_address = school_address
        self.school_phone = school_phone
    def school_details(self):
        print("School: ",self.school_name,"\n Address :", self.school_address,"\nPhone :", self.school_phone)




class Admin(School):
    def __init__(self,admin_name, admin_post ,admin_email,school_name,school_address,school_phone):
        super().__init__(school_name, school_address, school_phone)
        self.admin_name = admin_name
        self.admin_post= admin_post
        self.admin_email= admin_email

    def admin_details(self):
        print("Admin_name :",self.admin_name, "\n Post :" ,self.admin_post,"\nEmail :", self.admin_email)
        self.school_details()

class Teachers(School):
    def __init__(self, teacher_name, subject, room,school_name, school_address,school_phone):
        super().__init__(school_name, school_address,school_phone)
        self.t_name = teacher_name
        self.t_subject =subject
        self.t_room =room
    def teacher_details(self):
        print("Teacher :",self.t_name , "\n Subject :", self.t_subject, "\n Room :", self.t_room)
        self.school_details()


class SchoolBus(School):
    def __init__(self, bus_driver, bus_no, bus_route, school_name,school_address,school_phone):
        super().__init__(school_name,school_address,school_phone)
        self.driver = bus_driver
        self.no = bus_no
        self.route=bus_route
    def bus_details(self):
        print("Bus Driver :", self.driver,"\n Bus Number :" ,self.no, "\n Bus Route :", self.route)
        self.school_details()



if __name__=='__main__':

    a = Admin("Ms.Abbey", "Secretary","abby@gmail.com","SouthMiddle","Grimes",657657)
    a.admin_details()
    print("*"*50)
    t = Teachers("Mrs.Jacobson","Language Arts",677, "North View", "Waukesha",76876)
    t.teacher_details()
    print("*"*50)
    b= SchoolBus("Mr.Ben",122,"Route 17","Head Start","Salt Lake City",4646)
    b.bus_details()