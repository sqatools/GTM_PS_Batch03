"""
# range(initial value, end value, difference of values)
# The end value will always be excluded
range(1, 10, 1) # 1 2 3 4 5 6 7 8 9
range(1, 10, 2)  # 1 3 5 7 9

# default difference value is 1
range(1, 10)  # 1 2 3 4 5 6 7 8 9

# default initial value is 0
range(5)  # 0, 1, 2, 3, 4
"""

# Class Work #
for i in range(1, 10, 1):
    print(i)

for i in range(1, 10):
    print(i)

for j in range(1, 10, 2):
    print(j)

for i in range(5):
    print(i)

# print reverse order numbers
for i in range(10, 1, -1):
    print(i)

# print table of any given number
num = 6
for i in range(1, 11):
    print(num, "*", i, "=", num * i)

# Write a if condition with loop to get all the number which can divide by three
for i in range(1, 20):
    if i % 3 == 0:
        print(i)

# Apply loop on string #
str1 = "Good Morning"
for s in str1:
    print(s, end=' ')

# Apply loop on list #
list1 = [4, 7, 9, 'Hello', 'Python', 'Learning']
for l in list1:
    print(l, end=' ')

# Write a python program to get factorial of any number, fact of 5 = 5*4*3*2*1
num = 6
fact = 1
for i in range(num, 0, -1):
    fact = fact * i
print("Factorial o/p is:", fact)

# write a python program to check given number is prime or not
num = 15
prime = True
for i in range(2, num // 2):
    if num % i == 0:
        prime = False
        break
if prime:
    print("This is prime number :", num)
else:
    print("This is not prime number :", num)

# Nested loop Concept #
for i in range(0, 5):
    for j in range(0, 5):
        print(i, j)

"""
*
* * 
* * *
* * * * 
* * * * *
"""

for i in range(1, 7):
    for j in range(i):
        print("*", end=" ")
    print()

#######################################################################
# 1. Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
#  between 1500 and 2700 (both included).

for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i, end=' ')

# 2. Python Loops program to construct the following pattern, using a nested for loops.
"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
"""
for i in range(0, 6):
    for j in range(i):
        print("*", end=' ')
    print()  # Line break

for i in range(0, 5):
    print("* " * i)
for j in range(5, 0, -1):
    print("* " * j)

# 3. Python Loops program that will add the word from the user to the empty string using python.
word = input("Enter the word: ")
str1 = ""
print(len(word))
for i in range(len(word)):
    str1 = str1 + word[i]
print(str1)

