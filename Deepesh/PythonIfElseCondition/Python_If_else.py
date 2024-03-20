num1 = 100
num2 = 200
print(num1 == num2)

if num1 == num2:
    print("Both values are equal :", num1, num2)
else:
    print("Both values are not equal :", num1, num2)


print("_"*50)
"""
# check give number is divisible by 3 or not
n1 = input("Please enter the number :")
print(n1, type(n1))

if int(n1)%3 == 0:
    print("The number is divisible by 3 :", n1)
else:
    print("The number can not divide by 3 :", n1)
"""


"""
# check given number is even or odd
temp = int(input("Please enter the number :"))
if temp%2 == 0:
    print("This is even number")
else:
    print("This is odd number")
"""
"""
# logical operator
cond1 and cond2 
True and True : True
False and True : False
True and False : False
False and False : False


cond1 or cond2
True or True : True
False or True : True
True or False : True
False or False : False

> : greater than operator
< : less than operator
>= : greater than equal to
<= : less than equal to
!= : not equal to
== : equal to

"""


# write a python program to check given number is divisible by 3 and 7
"""
num1 = int(input("Please enter the number :"))
if num1%3 == 0 and num1%7 == 0:
    print("The number can divide by 3 and 7")
else:
    print("The number can not divide by 3 and 7")
"""

"""
num1 = int(input("Please enter the number :"))
if num1%3 == 0 or num1%7 == 0:
    print("The number can divide by 3 or 7")
else:
    print("The number can not divide by 3 or 7")
"""

## write a python program to check given number is available in the list or not

temp = 22
list1 = [4, 6, 8, 2, 6, 50]
if temp in list1:
    print("Value is available in the list")
else:
    print("value is not available in the list")


# program1 : write a python program to check given is even the print square or value else cube of value
# program2 : write a python to check given number divisible 3 and 7 and not by 11
