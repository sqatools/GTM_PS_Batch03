# 13). Python program to determine whether a given number is available in the list of numbers or not.

lst1 = [23, 45, 56, 78, 23]
num1 = int(input("Enter a number :"))
if num1 in lst1:
    print("The number is in the list.")
else:
    print("The number is not in the list")