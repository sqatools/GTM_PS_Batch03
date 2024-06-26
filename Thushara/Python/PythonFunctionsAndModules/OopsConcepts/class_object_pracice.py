class Student:
    def __init__(self,name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade

class Course:
    def __init__(self,name, max_students):
        self.name = name
        self. max_students = max_students
        self.students =[]

    def add_student(self,Student):
        if len(self.students) < self.max_students:
            self.students.append(Student)
            return True
        return False
    def get_average_grade(self):
        value=0
        for student in self.students:
            value += student.get_grade()
            return (value / len(self.students))

s1 = Student("Hari",20,95)
s2 = Student("Bill",19,75)
s3 = Student("Jaya", 18, 89)

course= Course("Science",2)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.students)
print(course.get_average_grade())