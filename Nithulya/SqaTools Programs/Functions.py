#1). Python function program to add two numbers.
# def addNumber():
#     a=int(input("Enter the first number : "))
#     b=int(input("Enter the second number : "))
#     total=a+b
#     print("total : ",total)
# addNumber()

#2). Python function program to print the input string 10 times.
# def inString():
#     str1=input("Enter the string : ")
#     return str1*10
# print(inString())

#(OR)
# def inString(str1):
#     print(str1*10)
# str2=input("Enter the string : ")
# inString(str2)


#3). Python function program to print a table of a given number.
# def mulTable(a):
#  for i in range(1,11):
#         print(i," * ",a,' = ',a*i)
# num1=int(input("Enter the number : "))
# mulTable(num1)


#4). Python function program to find the maximum of three numbers.Input: 17, 21, -9, Output: 21
# def maxNum(a,b,c):
#     print('Max Number : ',max(a,b,c))
# c=int(input("Enter the 1st number : "))
# d=int(input("Enter the 2nd number : "))
# e=int(input("Enter the 3rd number : "))
# maxNum(c,d,e)                                   # Max Number :  21

#5). Python function program to find the sum of all the numbers in a list.Input : [6,9,4,5,3],Output: 27
# def totalValue(list1):
#     val1=0
#     for i in list1:
#         val1 += i
#     print("Total : ",val1)
# list_1=[6,9,4,5,3]
# totalValue(list_1)                      # Total :  27

#6). Python function program to multiply all the numbers in a list. Input : [-8, 6, 1, 9, 2],Output: -864
# def mulValue(list1):
#     val1=1
#     for i in list1:
#         val1 *= i
#     print("Total : ",val1)
# list_1=[-8, 6, 1, 9, 2]
# mulValue(list_1)                         # Total :  -864


#7). Python function program to reverse a string.Input: Python1234,Output: 4321nohtyp
def reverseString(str1):
 return str1[::-1]
str2=input("Enter the string : ")
print(reverseString(str2))                 # 4321nohtyP

