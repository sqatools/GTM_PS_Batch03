# 1. Check the numbers are equal
# value1 = 34
# value2 = 43
# if value1 == value2:
#     print("The values are equal")
# else:
#     print("The values are not equal")
#
# print("_"*50)

#2. Check give number is divisible by 3 or not
#print("_"*50)
# input1 = int(input("Enter the number : "))
# if input1%3 ==0:
#     print(f"The number {input1} is divisble by 3")
# else :
#     print(f"The number {input1} can not divide by 3")

#3. Check given number is even or odd
# value1 = int(input("Enter the number : "))
# if value1%2==0:
#     print(f"The number {value1} is even number")
# else :
#     print(f"The number {value1} is odd number")

#4. Write a python program to check given number is divisible by 3 and 7
# value2 = int(input("Enter the number : "))
# if value2%3==0 and value2%7==0:
#     print(f"The number {value2} is divisible by 3 and 7")
# else :
#     print(f"The number {value2} can not divide by 3 and 7")

#5. Write a python program to check given number is available in the list or not
# num1 = 28
# list1 = [22,45,23,46,21]
# if num1 in list1:
#     print("Value is available in the list")
# else:
#     print("Value is not available in the list")

#6. Write a python program to check given number is even then print it's square value else cube of value
# num3 = int(input("Enter the number : "))
# if num3%2==0:
#     print(f"The square value of {num3} is : ",num3**2)
# else :
#     print(f"The cube value of {num3} is : ", num3**3)

#7. Write a python program to check given number is divisible by 3 and 7 and not by 11
# num4 = int(input("Enter the number : "))
# if num4%3==0 and num4%7==0 and num4%11!=0:
#     print(f"The number {num4} is divisible by 3 and 7 and not by 11 ")
# else :
#     print(f"The number {num4} can not divide by 3 and 7 and not by 11 ")

#8.
gate1 = 'Open'
gate2 = 'Open'
gate3 = 'close'
if gate1 =="Open":
    print('Welcome to the house, Gate1 is opened!!')
    if gate2 == "Open":
        print('Welcome to the room, Gate2 is opened!!')
        if gate3 == "Open":
            print('Welcome to the locker, Gate3 is opened!!')
        else:
            print("Sorry gate3 couldn't open, Try again")
    else:
        print("Sorry gate2 couldn't open, Try again")
else:
    print("Sorry gate1 couldn't open, Try again")