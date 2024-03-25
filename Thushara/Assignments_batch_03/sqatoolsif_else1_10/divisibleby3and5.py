# 4). Python program to check the given number divided by 3 and 5.
num = int(input("Enter a number :"))
if num%3 == 0  and num%5 == 0:
    print("The given number is divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and five")