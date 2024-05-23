# 30). Python program to check whether a given year is a leap or not.
# Input = 2000
# Output = The given year is a leap year

year = 2024
if (year%100 != 0 or year%400 == 0) and year%4 == 0:
    print("The given year is a leap year")
else:
    print("THe given year is not a leap year")