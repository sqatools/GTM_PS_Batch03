#1). Python program to check given number is divided by 3 or not.
# num1 = int(input("Enter the number : "))
# if num1%3==0 :
#     print(f"The number {num1} is divisible by 3")
# else :
#     print(f"The number {num1} is not divisible by 3")

#2).  If else program to assign grades as per total marks.
# marks=int(input("Enter your mark : "))
# if marks>=40 and marks<50:
#     print("Congrats!!, You have got grade C")
# elif marks>=50 and marks<60:
#     print("Congrats!!, You have got grade B")
# elif marks>=60 and marks<70:
#     print("Congrats!!, You have got grade A")
# elif marks>=70 and marks<80:
#     print("Congrats!!, You have got grade A+")
# elif marks>=80 and marks<90:
#     print("Congrats!!, You have got grade A++")
# elif marks>=90 and marks<=100:
#     print("Grade Excellent!!")
# elif marks>100:
#     print("Invalid marks")
# else :
#     print("You are fail. Try again")

#3). Python program to check the given number divided by 3 and 5.
# num = int(input("Enter the number : "))
# if num%3==0 and num%5==0:
#     print(f"The number {num} is divisible by both 3 and 5")
# else :
#     print(f"The number {num} is not divisible by 3 and 5")

#4). Python program to print the square of the number if it is divided by 11.
# num = int(input("Enter the number : "))
# if num%11==0:
#     print(f"The square of {num} is ",num**2)
# else :
#     print(f"The number {num} is not divisible by 11")

#5).Python program to check given number is odd or even.
# num = int(input("Enter the number : "))
# if num%2==0:
#     print(f"The number {num} is even number")
# else :
#     print(f"The number {num} is odd number")

#6). Python program to check authentication with the given username and password.
# name1 = input('Enter your name : ')
# pswrd = input("Enter your password : ")
# if name1 ==pswrd :
#     print("It is valid")
# else :
#     print("It is not valid")
#7). Python program to validate user_id in the list of user_ids.
# id1= int(input("Enter your ID : "))
# id_list = [11,12,13,14,15,16]
# if id1 in id_list:
#     print("It is valid ID")
# else :
#     print("It is invalid ID")

#8). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
# num3 = int(input("Enter the number : "))
# if num3%2==0:
#     print(f"The square value of {num3} is : ",num3**2)
# elif num3%3==0:
#     print(f"The cube value of {num3} is : ", num3**3)
# else:
#     print("Invalid number")

#9). Python program to describe the interview process.
# round1 = 'Pass'
# round2 = 'Pass'
# round3 = 'Fail'
# if round1 =="Pass":
#     print('Congrats!! Welcome to the round2')
#     if round2 == "Pass":
#         print('Congrats!! Welcome to the round3')
#         if round3 == "Pass":
#             print('Congrats!! You are selected')
#         else:
#             print("Sorry you are not selected in round3, Try again")
#     else:
#         print("Sorry you are not selected in round2 , Try again")
# else:
#     print("Sorry you are not selected in round1, Try again")

#10). Python program to determine whether a given number is available in the list of numbers or not.
# num= int(input("Enter your number : "))
# num_list = [11,12,13,14,15,16]
# if num in num_list:
#     print("It is a valid number")
# else :
#     print("It is invalid number")

#11). Python program to find the largest number among three numbers.
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# num3 = int(input("Enter the third number : "))
# if num1>num2:
#     if num1>num3:
#         print(f"The number {num1} is greater")
#     else:
#         print(f"The number {num3} is greater")
# else:
#     print(f"The number {num2} is greater")

#12). Python program to check any person eligible to vote or not.age > 18+ : eligible,age < 18: not eligible
# age = int(input("Enter your age : "))
# if age >=18:
#     print("You are eligible to vote")
# else:
#     print("You are not eligible to vote")

#13). Python program to check whether a student has passed the exam. If marks are greater than 35 students have passed the exam.
# mark = int(input("Enter your mark : "))
# if mark >=35:
#     print("Congrats!! You have passed the exam")
# else:
#     print("You have not passed the exam.")

#14). Python program to check whether the given number is positive or not.
# numa = int(input("Enter the number : "))
# if numa >=0:
#     print(f"The number {numa} is positive number, it is true")
# else:
#     print(f"The number {numa} is negative number, it is false")

#15). Python program to check whether the given number is negative or not.
# numa = int(input("Enter the number : "))
# if numa <=0:
#     print(f"The number {numa} is negative number, it is true")
# else:
#     print(f"The number {numa} is positive number, it is false")

#16). Python program to check whether the given number is positive or negative and even or odd.
# numa = int(input("Enter the number : "))
# if numa >=0:
#     if numa%2==0:
#         print(f"The number {numa} is positive and even number.")
#     else:
#         print(f"The number {numa} is positive and odd number.")
# else:
#     if numa%2==0:
#         print(f"The number {numa} is negative and even number.")
#     else:
#         print(f"The number {numa} is negative and odd number.")


#17). Python program to print the largest number from two numbers.
# num1 = int(input("Enter the first number : "))
# num2 = int(input("Enter the second number : "))
# if num1>num2:
#     print(f"The number {num1} is greater")
# else:
#     print(f"The number {num2} is greater")


#18). Python program to check whether the given number is an integer or not.
# num = int(input("Enter the first number : "))
# if type(num)==int:
#     print(f"The number {num} is integer, True")
# else:
#     print(f"The number {num} is not integer, False")

#19). Python Python program to check whether the input number if a multiple of two print “Fizz” instead of the number
# and for the multiples of three print “Buzz”. For numbers that are multiples of both two and three print “FizzBuzz”.
# num1=int(input("Enter the number : "))
# if num1%2==0 and num1%3==0:
#     print("FizzBuzz")
# elif num1%2==0:
#     print("Fizz")
# elif num1%3==0:
#     print("Buzz")
# else:
#     print("It is invalid number")

#20). Python program to check whether an alphabet is a vowel.
# alpha = input("Enter the alphabet: ")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# if alpha in vowels:
#     print(f"The alphabet{alpha} is a vowel, True")
# else:
#     print(f"The alphabet{alpha} is not a vowel, False")

#21). Python program to check whether an alphabet is a consonant.
# alpha = input("Enter the alphabet: ")
# vowels = ["A","E","I","O","U","a","e","i","o","u"]
# if alpha not in vowels:
#     print(f"The alphabet{alpha} is a consonant, True")
# else:
#     print(f"The alphabet{alpha} is not a consonant, False")

#22). Python program to check whether a triangle is equilateral or not.
#An equilateral triangle is a triangle in which all three sides are equal.
# side1 = int(input("Enter value of Side1 : "))
# side2 = int(input("Enter value of Side2 : "))
# side3 = int(input("Enter value of Side3 : "))
# if side1 == side2 == side3:
#     print("Triangle is equilateral")
# else:
#     print("Triangle is not equilateral")

#23). Python program to check whether a triangle is scalene or not.
# A scalene triangle is a triangle that has three unequal sides.
# side1 = int(input("Enter value of Side1 : "))
# side2 = int(input("Enter value of Side2 : "))
# side3 = int(input("Enter value of Side3 : "))
# if side1 != side2 and side1 != side3 and side2 != side3:
#     print("Triangle is scalene")
# else:
#     print("Triangle is not scalene")

#24). Python program to check whether a triangle is isosceles or not.
# An isosceles triangle is a triangle with (at least) two equal sides.
side1 = int(input("Enter value of Side1 : "))
side2 = int(input("Enter value of Side2 : "))
side3 = int(input("Enter value of Side3 : "))
if side1 != side2 or side1 != side3 or side2 != side3:
    print("Triangle is isosceles")
else:
    print("Triangle is not isosceles")

