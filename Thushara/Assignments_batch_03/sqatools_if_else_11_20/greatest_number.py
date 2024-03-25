# 14). Python program to find the largest number among three numbers.
num1 = int(input("Enter first number :"))
num2 = int(input("Enter second number :"))
num3 = int(input("Enter third number :"))

if num1>num2:
    if num1>num3:
        print("The first number is the greatest :")
    else:
        print("The third number is the greatest:")
else:
    if num2>num3:
        print("The second number is greatest")
    else:
        print("The third number is the greatest")
