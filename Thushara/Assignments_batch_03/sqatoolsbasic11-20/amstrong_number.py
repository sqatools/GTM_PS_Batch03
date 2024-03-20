# Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3

num = int(input("Enter a number :"))
num1 = num
arm = 0
while num > 0:
    a = num % 10
    arm = arm+a**3
    num = num//10
if arm == num1:
    print("The given number is an armstrong number")
else:
    print("It is not an armstrong number")
