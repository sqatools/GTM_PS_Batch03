# Python program to check a given number is part of the Fibonacci series from 1 to 10.
fib = [1, 1, 2, 3, 5, 8,]

num = int(input("Enter a number between 1 and 10 :"))
if num in fib:
    print("The given number is part of the fibonacci series.")
else:
    print("The number is not in the fibonacci series.")