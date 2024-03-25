"""

3). If else program to assign grades as per total marks.
marks > 40: Fail
marks 40 – 50: grade C
marks 50 – 60: grade B
marks 60 – 70: grade A
marks 70 – 80: grade A+
marks 80 – 90: grade A++
marks 90 – 100: grade Excellent
marks > 100: Invalid marks
"""
marks = int(input("Enter your marks : "))
if marks < 40:
    print("Failed")
elif 40 < marks <= 50:
    print("Grade : C")
elif 51 < marks <= 60:
    print("Grade : B ")
elif 61 < marks <= 70:
    print("Grade : A ")
elif 71 < marks <= 80:
    print("Grade : A+ ")
elif 81 < marks <= 90:
    print("Grade : A++ ")
elif 91 < marks <= 100:
    print("Grade : Excellent ")
elif marks < 40:
    print("Failed")
else:
    print("Invalid marks")


