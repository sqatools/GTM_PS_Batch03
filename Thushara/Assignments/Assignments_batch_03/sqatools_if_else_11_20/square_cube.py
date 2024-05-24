# 11). Python program to print a square or cube if the given number is divided by 2 or 3 respectively.
num = int(input("Enter a number :"))
if num%2 == 0:
    num = num**2
    print("The number is divisible by 2 and the square of the number is :", num)
elif num%3 == 0:
    num = num**3
    print("The number is divisible by 3 and the cube of the number is :", num)
else:
    print("The number is neither divided by 2 nor 3")
