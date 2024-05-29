
# #1) LCM
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter first number : "))
#
# if num1>num2:
#     greater = num1
# else:
#     greater = num2
#
# while(True):
#     if ((greater%num1==0) and (greater%num2==0)):
#         lcm = greater
#         break
#     greater +=1
#
# print(f"LCM of {num1} and {num2} :{lcm}")
#

#2) HCF
# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter first number : "))
#
# if num1>num2:
#     smaller = num2
# else:
#     smaller = num1
#
# for i in range(1, smaller+1)   :
#     if((num1%i == 0) and (num2%i == 0)):
#         hcf = i
# print(f"HCF of {num1} and {num2} : {hcf}")
#
#

#3)random string
# import string
# import random
# length = int(input("Enter the length of the string :"))
#
# result = ''.join(random.choices(string.ascii_letters, k=length))
# print("The generated random string :" , result)

#4) Random numbers

# import random
#
# for i in range(5):
#     print(random.random())


#5) Leap Year

# year = int(input("Enter a year :"))
#
# if(year%400 == 0  or year%100 !=0 and year%4 == 0):
#     print(f"{year} is a leap year!")
# else:
#     print(f"{year} is not a leap year")

#6) Prime Number
# num = int(input("Enter a number :"))
#
# count =0
#
# for i in range(2,num):
#     if num%i == 0:
#         count+=1
#
# if count ==0:
#     print("Prime")
# else:
#     print("Not prime")

# 7) Palindrome

# n = num = int(input("Enter a number: "))
# rev = 0
#
# while n>0:
#     rem = n%10
#     rev = rev*10+rem
#     n = n//10
#
# if num == rev:
#     print("Given number is a palindrome number")
# else:
#     print("Given number is not a palindrome number")

#8) Fibonacci Series

# num1 = 0
# num2 = 1
# count =0
# print("Fibonacci series :" , end=" ")
# while count<15:
#     print(num1 , end = " ")
#     n2 = num1 +num2
#     num1 =num2
#     num2 = n2
#     count +=1

#9) Reverse a number

# num = 12345678
# num1 = str(num)
# rev = num1[::-1]
# print(rev)

#10) factorial

# num = 3
# f=1
# while num >0:
#     f = f*num
#     num-=1
# print("Factorial :", f)

#11) current date
# import datetime
# date = datetime.datetime.now()
# print(date.strftime("%y %m %d"))


#12)Armstrong Number

# num = a = 153
# rev = 0
# while a>0:
#     rem = a%10
#     rev = rev+rem**3
#     a = a//10
#
# if rev == num:
#     print("Armstrong")
# else:
#     print("Not a prime")

#13) Armstrong

# def armstrong(num):
#     a = num
#     A = 0
#     while a>0:
#         rem = a%10
#         A= A+rem**3
#         a= a//10
#     if  num == A:
#         print("Armstrong ")
#     else:
#         print("Not an Armstrong number")
#
# armstrong(153)
#String

#1)
string = "sqatools"

#Printing output
if len(string) < 2:
    print(True)
else:
    print(string[:2]+string[-2:])

