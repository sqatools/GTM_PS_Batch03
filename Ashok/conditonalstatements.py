"""
In python, there are three forms of if...else statements
1. if statement
2. if...else statements
3. if...elif...else statements
"""

num1 = 100
num2 = 200
print(num1 == num2)
if num1 == num2:
    print("Both values are equal :", num1, num2)
else:
    print("Both values are not equal :", num1, num2)

print("*" * 50)

# check give number is divisible by 3 or not
a = input("Enter a number")

if int(a) % 3 == 0:
    print("The number is divisible by 3 :", a)
else:
    print("The number can not divide by 3 :", a)

print("*" * 50)

# check given number is even or odd
temp = int(input("Enter a number"))
if temp % 2 == 0:
    print("The give number is even", temp)
else:
    print("The give number is odd", temp)

print("*" * 50)

# write a python program to check given number is divisible by 3 and 7
_b = int(input("Enter a number"))
if _b % 3 == 0 and _b % 7 == 0:
    print("The number can divide by 3 and 7")
else:
    print("The number can not divide by 3 and 7")

print("*" * 50)

# write a python program to check given number is available in the list or not
b1 = int(input("Enter a number"))
list1 = [1, 2, 3, 35, 25, 'hi']
if b1 in list1:
    print("Value is available in the list")
else:
    print("value is not available in the list")

print("*" * 50)
# program1 : write a python program to check given is even the print square or value else cube of value
num_1 = int(input("Enter a number"))
if num_1 % 2 == 0:
    print("The given number is even", num_1 ** 2)
else:
    print("The given number is odd", num_1 ** 3)

print("*" * 50)


# program2 : write a python to check given number divisible 3 and 7 and not by 11

num_2 = int(input("Enter a number"))
if num_2 % 3 == 0 and num_2 % 7 == 0 and num_2 % 11 != 0:
    print("The given number is divisible by 3 and 7 not by 11 is", num_2)
else:
    print("The given number is divisible by 3 and 7 and 11 is ", num_2)

# program 3:
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

