"""
21). Write a program to find the sum of the first and last digits of a number using python.

"""
num = input("Enter the number :")
for i in range(len(num)):
    if i == 0:
        f=num[i]
    elif i== len(num)-1:
        l=num[i]
print("The sum of the first and last digits of the given number is :", int(l)+int(f))
"""
22). Write a program to calculate the sum of digits of a number using python.
"""
num = input("Enter a multi digit number :")
str1 = str(num)
sum = 0
for i in num:
    sum += int(i)
print("Sum of the digits of the given number: ", sum)
"""
23). Write a program to calculate the product of digits of a number using python.

"""
num = input("Enter a multi digit number :")
str1 = str(num)
pdt = 1
for i in num:
    pdt = pdt*int(i)
print("The product of the digits of the given number: ", pdt)
"""
24).Python loops program to enter a number and print its reverse using python.
"""
num = int(input("Enter a number to get it's reverse :"))
rev = 0
while num>0:
    r = num%10
    rev =(rev*10)+r
    num = num//10
print("The reverse of the given number :", rev)
"""
25). Write a program to check whether a number is a palindrome or not using python loops.
"""
num = int(input("Enter a number to get it's reverse :"))
num1 = num
rev = 0
while num>0:
    r = num%10
    rev =(rev*10)+r
    num = num//10
print("The reverse of the given number :", rev)

if num1 == rev:
    print("The given number is a palindrome number")
else:
    print("Not a palindrome number")
"""
26). Program to find the frequency of each digit in a given integer using Python Loops.
"""
"""
27). Python loops program to enter a number and print it in words.
"""
num = input("Enter a number :")
str1=""
for i in str(num):
    if i == "1":
        str1 +="One"
    elif i == "2":
        str1 += "Two"
    elif i =="3":
        str1+="Three"
    elif i =="4":
        str1+="Four"
    elif i =="5":
        str1+="Five"
    elif i =="6":
        str1+="Six"
    elif i =="7":
        str1+="Seven"
    elif i =="8":
        str1+="Eight"
    elif i =="9":
        str1+="Nine"
    elif i =="0":
        str1+="Zero"
print (num,str1)

"""
28). Python loops program to find the power of a number using Python for loop.
 Take values as an input base number and power, and get the total value using a loop.
"""
num = int(input("Enter a number to find the power"))
pow = int(input("Enter the power"))
result = 1
for i in range(pow):
    result =result*num
print(result)
"""
29). Python loops program to find all factors of a number using Python. 
Get all the numbers that can divide this number from 1 to n.
 
"""
num = int(input("Enter a number"))
for i in range(1,num+1):
    if num%i == 0:
        print(i)
"""
30). Write a program to calculate the factorial of a number using Python Loops.
"""
num = int(input("Enter a number to find factorial"))
fact = 1
for i in range(num,1,-1):
    fact = fact*i
print(fact)