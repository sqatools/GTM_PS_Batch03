# 1). Write a Python loops program to find those numbers which are divisible by
# 7 and multiple of 5, between 1500 and 2700 (both included).
for i in range(1500,2701):
    if i %7 == 0 and i%5 == 0:
        print("It is divisible by 5 and 7 : ",i)

# 2). Python Loops program to construct the following pattern, using a nested for loops.
l1 = int(input("Enter the input"))
for l1 in range(1,l1):
    print("*"*l1)
for l1 in range(l1,0,-1):
    print("*"*l1)

# 3). Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str1 = ""
for i in range(len(word)):
    str1 += word[i]

print(str1)


# Python Loops program to count the number of even and odd numbers from a series of numbers using python.
num_1 = int(input("Enter the first no"))
num_2 = int(input("Enter the first no"))
even = 0
odd = 0
for i in range(num_1,num_2):
    if i%2 == 0:
        even = even+1
    else:
        odd = odd+1
print(even,odd)


# 5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
i = 0
while i<6:
    if i!=3 and i!=6:
        print(i)
    i = i+1

# 6). Write a program to get the Fibonacci series between 0 to 20 using python.
i=1
j=1
while i <=20:
    j = i+j
    j+1

# 7). Write a program that iterates the integers from 1 to 30 using python.
# For multiples of three print “Fizz” instead of the number and for multiples of five print “Buzz”.
f1 = 1
while f1<=30:
    if f1%3==0:
        print("FIZZ",end=" ")
    elif f1%5==0:
        print("BUZZ",end=" ")
    else:
        print(f1,end=" ")
    f1=f1+1


# 8). Write a program that accepts a word from the user and
# converts all uppercases in the word to lowercase using python.
a = input("Enter a word: ")
b = " "
c=0
for c in range(len(a)):
    if a[c].isupper():
        b = b+a[c].lower()
    else:
        b = b+a[c].lower()
print(b)


# 9). Python loops program that accepts a string and calculates the number of digits and letters using python.
a = input("Enter an input : ")
letter = 0
digit = 0
b = 0
while b < len(a):
    if a[b].isupper() or a[b].islower():
        letter = letter+1
    else:
        digit = digit+ 1
    b = b+1
print("letter : ",letter)
print("digit : ",digit)

# 10). Python for loop program to print the alphabet pattern ‘O’ using python.
# 11). Python Loops program to print all natural numbers from 1 to n using a while loop in python.
n = int(input("Enter the number: "))
for n in range(1,n+1):
    print(n,end=" ")


# 12). Write a program to print all natural numbers in reverse (from n to 1) using a while loop in python.
num1 = int(input("Enter the number: "))
num2 = 1
while num1>= num2:
    print(num1, end=" ")
    num1 = num1 - 1


# 13). Python Loops program to print all alphabets from a to z using for loop
 #  Take chr method help to print characters with ASCII values

for alpha in range(65,90):
    print(chr(alpha), end=" ")
for alpha in range (97,127):
    print(chr(alpha), end=" ")