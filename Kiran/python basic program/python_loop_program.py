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
'''
  * * *  
*       *
*       *
*       *
*       *
*       *
  * * *  
   '''
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")
print()

for i in range(1, 6):
    for j in range(1, 6):
        if j == 1 or j == 5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for i in range(1, 6):
    if i == 1 or i == 5:
        print(" ", end=" ")
    else:
        print("*", end=" ")


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
'''
* * * * *
* * * * *
* *
* *
* * * * *
* * * * *
'''
for i in range(1,3):
   print("* "*5)
for i in range(1,3):
   print("* "*2)
for i in range(1,3):
   print("* "*5)

# 14). Python Loops program to print all even numbers between 1 to 100 in python.
for i in range(1,101):
    if i%2 ==0:
        print("even no : ",i)

# 15). Python Loops program to print all odd numbers between 1 to 100 using python.
for i in range(1,101):
    if i%2 !=0:
        print("odd no : ",i)


# 16). Python Loops program to find the sum of all natural numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    j = j+k
print(j)

# 17). Python program to find the sum of all even numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    if k%2 == 0:
        j = j+k
print(j)

# 18). Python Loops program to find the sum of all odd numbers between 1 to n using python.
i = int(input("Enter the last number: "))
j = 0
for k in range(1,i+1):
    if k%2 != 0:
        j = j+k
print(j)

# 19). Write a program to count the number of digits in a number using python.
i = input("Enter the number: ")
j = 0
for digit in i:
    j= j+1
print(j)


# 20). Write a program to find the first and last digits of a number using python.
i = input("Enter the number: ")
j = 0
for j in range(len(i)):
    k=(i[0],i[-1])
print(k)

# 21). Write a program to find the sum of the first and last digits of a number using python.
i = input("Enter the number: ")
j = 0
for j in range(len(i)):
    k=int(i[0])+int(i[-1])
print(k)


# 22). Write a program to calculate the sum of digits of a number using python.
num = int(input("Enter a number : "))
sum = 0
while num>0:
    rem = num%10
    sum = sum + rem
    num = num//10
print("Addition is :", sum)

# 23). Write a program to calculate the product of digits of a number using python
num = int(input("Enter a number : "))
mul = 1
while num>0:
    rem = num%10
    mul = mul* rem
    num = num//10
print("Multiplication is :", mul)
# 24).Python loops program to enter a number and print its reverse using python.
i = input("Enter the number: ")
j=int(i[::-1])
print(j)

# 25). Write a program to check whether a number is a palindrome or not using python loops.
num = int(input("Enter the input: "))
n=num
rnum=0
while num>0:
    digit = num%10
    rnum = (rnum*10)+digit
    num = num//10
if n == rnum:
    print("It is palendrome")
else:
    print("not palendrome")

# 26). Program to find the frequency of each digit in a given integer using Python Loops.
num1=int(input("enter a number :"))
str1=str(num1)
dict1={}
for i in str1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
print(dict1)

# 27). Python loops program to enter a number and print it in words.
num = int(input("Enter the number : "))
str1 = str(num)
for i in range(len(str1)):
    if str1[i] == "0":
        print("zero", end=" ")
    elif str1[i] == "1":
        print("one", end=" ")
    elif str1[i] == "2":
        print("two", end=" ")
    elif str1[i] == "3":
        print("three", end=" ")
    elif str1[i] == "4":
        print("four", end=" ")
    elif str1[i] == "5":
        print("five", end=" ")
    elif str1[i] == "6":
        print("six", end=" ")
    elif str1[i] == "7":
        print("seven", end=" ")
    elif str1[i] == "8":
        print("eight", end=" ")
    elif str1[i] == "9":
        print("nine", end=" ")
    else:
        print("invalid")


# 28). Python loops program to find the power of a number using Python for loop.
# Take values as an input base number and power, and get the total value using a loop.
num = int(input("enter number : "))
power = int(input("enter power : "))
result = 1
for i in range(power):
    result = result * num
print(result)


# 29). Python loops program to find all factors of a number using Python. Get all the numbers that can divide this number from 1 to n.
num = int(input("enter number : "))
for i in range(1,num+1):
    if num%i ==0:
        print(i,end=" ")


# 30). Write a program to calculate the factorial of a number using Python Loops.
num = int(input("E nter a number : "))
i =1
for j in range(num,0,-1):
    i = i*j
print(i)

num = int(input("E nter a number : "))
i =1
j =1
while j <=num:
    i = i*j
    j = j+1
print(i)


# 31). Write a program to check whether a number is a Prime number or not using Python Loops.
num = int(input("Enter a number : "))
for i in range(2, num):
    if num % i == 0:
        print("It is not prime")

    else:
        print("It is prime")


# 32). Write a program to print all Prime numbers between 1 to n using Python Loops.
num = int(input("E nter a number : "))
for i in range(2,num):
    count = 0
    for j in range(2,i):
        if i%j == 0:
            count +=1
    if count ==0:
        print(i,end=" ")


# 33). Python loops program to find the sum of all prime numbers between 1 to n using Python.






# 35). Python loops program to check whether a number is an Armstrong number or not using Python Loops.
num = int(input("enter a number : "))
num2 = str(num)
v = 0
for i in num2:
    v+=int(i)**len(num2)
if v == num:
    print("It is armstrong number")
else:
    print("Not a armstrong number ")


# 36). Python loops program to print all Armstrong numbers between 1 to n using Python Loops.
