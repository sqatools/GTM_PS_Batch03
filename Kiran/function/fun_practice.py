# 1). Python function program to add two numbers.

def addition(num1,num2):
    print(num1+num2)
addition(50,40)
########################################################
def addition(num1,num2):
    print(num1+num2)
x = int(input("Enter first number : "))
y = int(input("Enter second number : "))
addition(x,y)


# 2). Python function program to print the input string 10 times.
def str1(n):
    print(n*10)
n = input('enter a string : ')
str1(n)


# 3). Python function program to print a table of a given number.
def table(n):
    for i in range(1,11):
        print(n,"*",i,"=",n*i)
num = int(input("Enter a number : "))
table(num)


# 4). Python function program to find the maximum of three numbers.
def maximum(a,b,c):
    if a>b and a>c:
        print("A is greater : ",a)
    elif b>a and b>c:
        print("B is greater : ",b)
    elif c>a and c>b:
        print("C is greater : ",c)
num1 = int(input("Enter a number : "))
num2 = int(input("Enter a number : "))
num3 = int(input("Enter a number : "))
maximum(num1,num2,num3)


# 5). Python function program to find the sum of all the numbers in a list.
def sum(num1):
    output =0
    for i in num1:
        output+=int(i)
    print(output)
num1 = list(input("Enter a number : ").split(","))
sum(num1)


# 6). Python function program to multiply all the numbers in a list.
def multiplication(n):
    output = 1
    for i in n:
        output = output*int(i)
    print(output)
n = list(input("Enter a list : ").split(','))
multiplication(n)


# 7). Python function program to reverse a string.
def reverse1(n):
    output=n[::-1]
    print(output)
n = input("Enter a string : ")
reverse1(n)

# 8). Python function program to check whether a number is in a given range.
def number(n):
    if 0 < n < 100:
        print("It is in given range : ",n)
    else:
        print("Number is out of range!!! ")
num = int(input("Enter the number : "))
number(num)


# 9). Python function program that takes a list and returns a new list with unique elements of the first list.
def unique_num(n):
    print(set(n))
num = list(input("Enter the number : ").split(","))
unique_num(num)


# 10). Python function program that take a number as a parameter and checks whether the number is prime or not.
def prime_num(n):
    count = 0
    for i in range(2,n):
        if n%i ==0:
            count+=1
    if count ==0:
        print("It is a prime number : ",n)
    else:
        print("It is not prime")
num = int(input("Enter the number : "))
prime_num(num)


# 11). Python function program to find the even numbers from a given list.
def even_num(n):
    if n%2 == 0:
        print("It is even number : ",n)
    else:
        print("It is odd number ")
num = int(input("Enter the number : "))
even_num(num)


# 12). Python function program to create and print a list where the values are squares of numbers between 1 to 10.
def square_num(*args):
    for args in range(1,11):
        print(args**2,end=" ")

square_num(1,2,3,4,5,6,7,8,9,10)


# 13). Python function program to execute a string containing Python code.
v = '''
x = 2
y =5
print(x+y)
'''
exec(v)
print(v)


# 14). Python function program to access a function inside a function.
def add(a,b):
    def sub(c):
        nonlocal a,b
        return a+b-c
    return sub
resu = add(10,5)
print(resu(9))


# 15). Python function program to find the LCM of two numbers.
