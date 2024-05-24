# 5). Python program to print the square of the number if it is divided by 11.

num = int(input("Enter a number :"))
if num%11 == 0:
   sqr = num**2
   print("The number is divisible by 11 and the square of the number  is :",sqr)
else:
    print("The number is not divisible by 11")
