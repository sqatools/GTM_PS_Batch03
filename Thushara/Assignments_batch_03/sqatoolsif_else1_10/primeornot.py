# 6). Python program to check given number is a prime number or not.
num = int(input("Enter a number :"))
flag = 0
for i in (2,num-1):
    if num % i == 0:
        flag = 1
        break
if flag != 0:
    print("The given number is not prime.")
else:
    print("The given number is prime.")