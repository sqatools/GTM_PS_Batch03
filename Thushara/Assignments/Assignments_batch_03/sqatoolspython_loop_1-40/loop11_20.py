"""
11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
"""
num = 1
limit = int(input("Enter a number :"))
while num <= limit:
    print(num)
    num += 1
"""
12). Write a program to print all natural numbers ")in reverse (from n to 1) using a while loop in python.

"""
print("*"*50)
limit1 = int(input ("Enter a number :"))
num = limit1
while 1<= num<= limit1:
    print(num)
    num-=1
"""
13). Python Loops program to print all alphabets from a to z using for loop
        Take chr method help to print characters with ASCII values
        chr(65) = ‘A’
        A-Z ASCII Range  65-90
        a-z ASCII Range  97-122
"""
print("*"*50)
for i in range(97,123):
    print(chr(i), end =" ")
print()
for j in range (65, 91):
    print(chr(j), end = " ")
print()
print("*" * 50)
print("\n Alphabets from A-Z")
for i in range(26):
    print(chr(65+i), end = " ")
print("\n Alphabets from a-z")
for i in range(26):
    print(chr(97+i), end = " ")
"""
14). Python Loops program to print all even numbers between 1 to 100 in python.

"""
print()
print("*"*50)
for i in range(1,101):
    if i%2 == 0:
        print(i, end=" ")
"""
15). Python Loops program to print all odd numbers between 1 to 100 using python.

"""
print()
print("*"*50)
for i in range(1,101):
    if i%2 != 0:
        print(i, end=" ")

"""
16). Python Loops program to find the sum of all natural numbers between 1 to n using python.

"""
print()
print("*"*50)
i=0
sum=0
n = int(input("Enter a number:"))
for i in range (n+1):
    sum+=i
print(sum)
"""
17). Python program to find the sum of all even numbers between 1 to n using python.

"""
print("*"*50)
sum = 0
num = int(input("Enter a number:"))
for i in range(1,num+1):
    if i%2==0:
        sum+=i

print("Sum of even numbers :", sum)

"""
18). Python Loops program to find the sum of all odd numbers between 1 to n using python.

"""
print("*"*50)
sum = 0
num = int(input("Enter a number:"))
for i in range(1,num+1):
    if i%2!=0:
        sum+=i
print("Sum of odd numbers :", sum)
"""

19). Write a program to count the number of digits in a number using python.

"""
num=input("Enter a multi digit number :")
count = 0
for i in num:
    count+=1
print("The number of digits in the given number :",count)

"""
20). Write a program to find the first and last digits of a number using python.

"""
num = input("Enter the number :")
for i in range(len(num)):
    if i == 0:
        print("The first digit :",num[i])
    elif i== len(num)-1:
        print("The last digit: ", num[i])
