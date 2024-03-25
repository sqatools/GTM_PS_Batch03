#21). Python program to check whether the given number is positive or negative and even or odd.
num1 = int(input("Enter a number :"))
if num1>0:
    if num1%2 == 0:
        print("The number is positive and an even number.")
    else:
        print("The number is positive and an odd number.")
else:
    if num1 < 0:
        if num1%2 == 0:
            print("The number is negative and an even number.")
        else:
            print("The number is negative and an odd number.")


