"""1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
 between 1500 and 2700 (both included).
Input1:1500
Input2:2700
"""
for i in range(1500,2701):
    if i%7 == 0 and i%5 == 0:
        print(i, end=" ")


""""
2). Python Loops program to construct the following pattern, using a nested for loops.
Output :
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
for i in range (6):
    print(i * "*")
for i in range (4,-1,-1) :
    print(i * "*")

print("*" * 50)
"""
3). Python Loops program that will add the word from the user to the empty string using python.
Input: “python”
Output : “python”
"""
word = input("Enter a word : ")
str1 =""
a = len(word)
for i in range(a):
    str1 += word[i]
print(str1)
"""
4). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
Output :
Number of even numbers: 4
Number of odd numbers: 5
"""
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)
e = 0
o = 0
for i in numbers:
    if i%2 == 0:
        e+=1
    else:
        o+=1
print("Number of even numbers : ",e)
print("Number of odd numbers : ",o)
"""
5). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
"""
for i in range(7):
    if i==3 or i == 6:
        continue
    else:
        print(i)
"""
6). Write a program to get the Fibonacci series between 0 to 20 using python.
Fibonacci Series : 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181
"""
num1 = 0
num2 = 1
temp = 0




"""
7). Write a program that iterates the integers from 1 to 30 using python. For multiples of
 three print “Fizz” instead of the number and for multiples of five print “Buzz”.
For numbers that are multiples of both three and five print “FizzBuzz”. 
"""
for i in range(1,31):
    if i%3 == 0 and i%5 ==0:
        print("FizzBuzz")
    elif i%3 ==0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
"""
8). Write a program that accepts a word from the user and converts all 
uppercase's in the word to lowercase using python.
Input : “SqaTOOlS”
Output : “sqatools”
"""
word = input("Enter the word :")
for char in word:
    if char.isupper():
        print(char.lower(),end ="" )
    else:
        print(char, end= "")

print("#"*50)
"""
9). Python loops program that accepts a string and calculates the number of digits and letters using python.
Input : “python1234”
Output :
Letters 6
Digits 4
"""
input = "python1234"
digits = 0
letters = 0
for char in input:
    if char.isnumeric():
        digits += 1
    elif char.isalpha():
        letters += 1
    else:
        continue
print("Letters :", letters)
print("Digits :", digits)


"""
10). Python for loop program to print the alphabet pattern ‘O’ using python.
Output:
  ***  
*       *
*       *
*       *
*       *
*       *
   ***  


"""
for row in range(0,7):
    for column in range (0,7):
        if (row == 0 or row ==6) and (1<column<5):
            print("*", end ="")
        elif(0< row<=5) and(column ==1 or column ==5):
            print("*", end ='')
        else:
            print(" ", end ='')
    print()