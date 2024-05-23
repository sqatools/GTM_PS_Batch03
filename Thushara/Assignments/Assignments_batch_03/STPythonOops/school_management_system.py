class School:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teachers = []
        self.courses = []

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_teacher(self, teacher):
        self.teachers.append(teacher)

    def remove_teacher(self, teacher):
        if teacher in self.teachers:
            self.teachers.remove(teacher)

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def enroll_course(self, course):
        course.add_student(self)

    def drop_course(self, course):
        course.remove_student(self)


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def assign_course(self, course):
        course.add_teacher(self)

    def unassign_course(self, course):
        course.remove_teacher(self)


class Course:
    def __init__(self, name):
        self.name = name
        self.students = []
        self.teacher = None

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def add_teacher(self, teacher):
        self.teacher = teacher

    def remove_teacher(self, teacher):
        self.teacher = None


# Create a School instance
school = School("ABC School")

# Create some students
student1 = Student("John", 10)
student2 = Student("Alice", 9)
student3 = Student("Bob", 11)

# Add students to the school
school.add_student(student1)
school.add_student(student2)
school.add_student(student3)

# Create some teachers
teacher1 = Teacher("Mr. Smith", "Math")
teacher2 = Teacher("Ms. Johnson", "English")

# Add teachers to the school
school.add_teacher(teacher1)
school.add_teacher(teacher2)

# Create some courses
course1 = Course("Mathematics")
course2 = Course("English")

# Add courses to the school
school.add_course(course1)
school.add_course(course2)

# Enroll students in courses
student1.enroll_course(course1)
student2.enroll_course(course2)
student3.enroll_course(course1)

# Assign teachers to courses
teacher1.assign_course(course1)
teacher2.assign_course(course2)

# Print the details of the school, students, teachers, and courses]
print("School:", school.name)
print("Students:")
for student in school.students:
    print(student.name, "- Grade", student.grade)
print("Teachers:")
for teacher in school.teachers:
    print(teacher.name, "- Subject:", teacher.subject)
print("Courses:")
for course in school.courses:
    print(course.name)
    print("Teacher:", course.teacher.name)
    print("Enrolled Students:")
    for student in course.students:
        print(student.name)
    print("--------------------")

