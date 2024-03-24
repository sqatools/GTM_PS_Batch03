"""
In python, there are three forms of if...else statements
1. if statement
2. if...else statements
3. if...elif...else statements
"""

# Class Program 1:
num1 = 100
num2 = 200
print(num1 == num2)
if num1 == num2:
    print("Both values are equal :", num1, num2)
else:
    print("Both values are not equal :", num1, num2)

# Class Program 2:
main_door = "have access"
bed_room = "have access"
locker_room = "have access"
if main_door == "have access":
    print("Welcome to house")
    if bed_room == "have access":
        print("Welcome to bedroom")
        if locker_room == "have access":
            print("Welcome to bedroom")
        else:
            print("Don't have access for locker room")
    else:
        print("Don't have access for bed room")
else:
    print("Don't have access for main room")

print("*" * 50)

# Class Prog 3: Write a python program to check given num is even the print square or value else cube of value
num_1 = int(input("Enter a number"))
if num_1 % 2 == 0:
    print("The given number is even", num_1 ** 2)
else:
    print("The given number is odd", num_1 ** 3)
print("*" * 50)

# Class prog 4: Write a python to check given number divisible 3 and 7 and not by 11
num_2 = int(input("Enter a number"))
if num_2 % 3 == 0 and num_2 % 7 == 0 and num_2 % 11 != 0:
    print("The given number is divisible by 3 and 7 not by 11 is", num_2)
else:
    print("The given number is divisible by 3 and 7 and 11 is ", num_2)

##################################################################################
# 1. Check give number is divisible by 3 or not
a = input("Enter a number")
if int(a) % 3 == 0:
    print("The number is divisible by 3 :", a)
else:
    print("The number can not divide by 3 :", a)

# 2. If else program to get all the numbers divided by 3 from 1 to 30.

# 3. If else program to assign grades as per total marks.
marks = int(input("Enter marks:"))
if marks < 40:
    print("Failed in exam")
elif marks >= 40 and marks <= 50:
    print("Your grade is C")
elif marks >= 51 and marks <= 60:
    print("Your grade is B")
elif marks >= 61 and marks <= 70:
    print("Your grade is A")
elif marks >= 71 and marks <= 80:
    print("Your grade is A+")
elif marks >= 81 and marks <= 90:
    print("Your grade is A++")
elif marks >= 91 and marks <= 100:
    print("Your grade is Excellent")
else:
    print("Your have entered invalid marks")

# 4. Python program to check the given number divided by 3 and 5.
number = int(input("Enter number which is divisible by 3 and 5:"))
if number % 3 == 0 and number % 5 == 0:
    print("The given number is divisible by 3 and 5:", number)
else:
    print("The given number is not divisible by 3 and 5:", number)

# 5. Python program to print the square of the number if it is divided by 11
number_1 = int(input("Enter number "))
if number_1 % 11 == 0:
    print("The number is divisible by 11 and square of the num is:", number_1 ** 2)
else:
    print("The number is not divisible by 11")

# 6. Python program to check given number is a prime number or not.

# 7. Check given number is even or odd
temp = int(input("Enter a number"))
if temp % 2 == 0:
    print("The give number is even", temp)
else:
    print("The give number is odd", temp)


# 8. Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [1, 1, 2, 3, 5, 8, 11]
f = int(input("Enter a number"))
if f in fib:
    print("The given number is in fibonacci series:", f)
else:
    print("This number is not in fibonacci series:", f)

# 9. Python program to check authentication with the given username and password.
un = input("Enter username:")
pwd = input("Enter pwd:")
if un == "Ashok" and pwd == "Hi":
    print("User is authenticated")
else:
    print("User is not authenticated")

# 10. Python program to validate user_id in the list of user_ids.
list_user_id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
user_id = int(input("Enter a user id:"))
if user_id in list_user_id:
    print("This is valid")
else:
    print("This is not valid")


# 11. Python program to print a square or cube if the given number is divided by 2 or 3 respectively
num_3 = int(input("Enter a number"))
if num_3 % 2 == 0:
    print("The given number is divisible by 2 and square of num is:", num_3 ** 2)
elif num_3 % 3 == 0:
    print("The given number is divisible by 3 and square of num is:", num_3 ** 3)
else:
    print("The given number is not divisible by 2 or 3:", num_3)

# 12. Python program to describe the interview process.
round_1 = int(input("Enter 1st round marks"))
if round_1 >= 50:
    print("You have selected in first round")
    round_2 = int(input("Enter 2nd round marks"))
    if round_2 >= 70:
        print("You have selected in second round")
        round_3 = int(input("Enter 3rd round marks"))
        if round_3 >= 90:
            print("You have selected in third round and cleared all rounds.")
        else:
            print("You have selected in first & second round but failed in third round")
    else:
        print("You have selected in first round but failed in second round")
else:
    print("Failed in 1st round")

# 13. Write a python program to check given number is available in the list or not
b1 = int(input("Enter a number"))
list1 = [1, 2, 3, 35, 25, 'hi']
if b1 in list1:
    print("Value is available in the list")
else:
    print("value is not available in the list")

# 14. Python program to find the largest number among three numbers.

a = int(input("Enter A:"))
b = int(input("Enter B:"))
c = int(input("Enter C:"))
if a > b and a > c:
    print("A is greater number:", a)
elif b > a and b > c:
    print("B is greater number:", b)
else:
    print("C is greater:", c)

# 15.  Python program to check any person eligible to vote or not
# age > 18+ : eligible
# age < 18: not eligible

age = int(input("Enter Age:"))
if age >= 18:
    print("Eligible for vote:")
else:
    print("Not eligible for vote:")

# 16. Python program to check whether any given number is a palindrome.
# 17.  Python program to check if any given string is palindrome or not.

# 18. Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed
# the exam.
stud_marks = int(input("Enter student marks"))
if stud_marks >= 35:
    print("Passed")
else:
    print("Failed")

# 19. Python program to check whether the given number is positive or not.
n = int(input("Enter number"))
if n >= 0:
    print("It is positive number")
else:
    print("It is negative number")

# 20. Python program to check whether the given number is negative or not.
n = int(input("Enter number"))
if n < 0:
    print("It is negative")
else:
    print("It is positive")

# 21. Python program to check whether the given number is positive or negative and even or odd.
n2 = int(input("Enter number:"))
if n2 > 0:
    if n2 % 2 == 0:
        print("The number is positive and even")
    else:
        print("The number is positive and odd")
else:
    if n2 % 2 == 0:
        print("The number is negative and even")
    else:
        print("The number is negative and odd")

# 22. Python program to print the largest number from two numbers.
a = int(input("Enter A:"))
b = int(input("Enter B:"))
if a > b:
    print("A is greater number:", a)
else:
    print("B is greater number:", b)

# 23. Python program to check whether a given character is uppercase or not
alphabet = input("Enter alphabet:")
if alphabet.isupper():
    print("The given character is an Uppercase")
else:
    print("The given character is Lowercase")

# 24. Python program to check whether the given character is lowercase or not.
alphabet = input("Enter alphabet:")
if alphabet.islower():
    print("The given character is an Lowercase")
else:
    print("The given character is Uppercase")

# 25. Python program to check whether the given number is an integer or not.
num4 = 56
if (type(num4)) == int:
    print("Integer")
else:
    print("Not an Integer")

# 26. Python program to check whether the given number is float or not.
num5 = 56.45
if (type(num5)) == float:
    print("Float number")
else:
    print("Not an Float number")

# 27. Python program to check whether the given input is a string or not
str1 = input("Enter word:")
if (type(str1)) == str:
    print("True")
else:
    print("False")

# 28. Python program to print all the numbers from 10-15 except 13

# 29. Python program to find the electricity bill. According to the following conditions:

units = int(input("Enter units:"))
if units <= 50:
    bill_1 = 0.50 * units
    print("Over all bill is", bill_1 + (bill_1 * 0.17))
elif units <= 100:
    bill_2 = 0.75 * units
    print("Over all bill is", bill_2 + (bill_2 * 0.17))
elif units <= 250:
    bill_3 = 1.25 * units
    print("Over all bill is", bill_3 + (bill_3 * 0.17))
elif units > 250:
    bill_4 = 1.50 * units
    print("Over all bill is", bill_4 + (bill_4 * 0.17))

# 30. Python program to check whether a given year is a leap or not.
