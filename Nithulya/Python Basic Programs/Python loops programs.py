#1). Write a Python loops program to find those numbers which are divisible by 7 and multiple of 5,
#between 1500 and 2700 (both included).
# for i in range(1500,2701,5):
#     if i%7==0:
#         print(i,' ',end='')
#(OR)
# for i in range(1500,2701):
#     if i%7==0 and i%5==0:
#         print(i,' ',end='')


#2). Python Loops program to construct the following pattern, using a nested for loops.
# Output :
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

# for i in range(1,6):
#     print('* ' * i)
# for j in range(4,0,-1):
#     print('* '*j)


#2). Python Loops program to count the number of even and odd numbers from a series of numbers using python.
#Input : (1, 2, 3, 4, 5, 6, 7, 8, 9)
# input1 = (1,2,3,4,5,6,7,8,9)
# total1=0
# total2=0
# for i in input1:
#     if i%2==0:
#         total1=total1+1
#     else:
#         total2=total2+1
# print("Total number of even numbers : ", total1)
# print("Total number of odd numbers : ",total2)


#3). Write a program that prints all the numbers from 0 to 6 except 3 and 6 using python.
# for i in range(0,7):
#     if i!=3 and i!=6:
#         print(' ',i,end='')


#4).Write a program that iterates the integers from 1 to 30 using python. For multiples of three print “Fizz” instead
# of the number and for multiples of five print “Buzz”. For numbers that are multiples of both three and five print “FizzBuzz”.
# for i in range(1,31):
#     if i%3==0 and i%5==0:
#         print("FizzBuzz")
#     elif i%3==0:
#         print("Fizz")
#     elif i%5==0:
#         print("Buzz")


#5). Python loops program that accepts a string and calculates the number of digits and letters using python.
# input1=input("Enter the letters : ")
# cout=0
# for i in input1:
#     cout=cout+1
# print(f"Total number of digit in {input1}  : ",cout)


#6). Python for loop program to print the alphabet pattern ‘O’ using python.
# Output:
#   ***
# *       *
# *       *
# *       *
# *       *
# *       *
#    ***
# for i in range(1,8):
#     for j in range(1, 8):
#         if


#7). Python Loops program to print all even numbers between 1 to 100 in python.
# for i in range(2,101,2):
#     print(i,' ',end='')
#(OR)
# for i in range(1,101):
#     if i%2==0:
#         print(i,' ',end='')

#8). Python Loops program to print all odd numbers between 1 to 100 using python.
# for i in range(1,101,2):
#       print(i,' ',end='')
#(OR)
# for i in range(1,101):
#     if i%2!=0:
#         print(i,' ',end='')

#9). Python program to find the sum of all even numbers between 1 to n using python.
# num1=int(input("Enter the last number : "))
# total = 0
# for i in range(1,(num1+1)):
#     if i%2==0:
#         total +=1
# print("Total number of even numbers : ",total)

#10). Python Loops program to find the sum of all odd numbers between 1 to n using python.
# num1=int(input("Enter the last number : "))
# total = 0
# for i in range(1,(num1+1)):
#     if i%2!=0:
#         total +=1
# print("Total number of odd numbers : ",total)

#11). Python Loops program to find the sum of all natural numbers between 1 to n using python.
# num=int(input("Enter the number : "))
# total = 0
# for i in range(1,(num+1)):
#         total =total+i
# print("Sum of all natural numbers : ",total)

#12). Python program to find the sum of all even numbers between 1 to n using python.
# num=int(input("Enter the number : "))
# total = 0
# for i in range(1,(num+1)):
#     if i%2==0:
#         total =total+i
# print("Sum of all even numbers : ",total)

#13). Python Loops program to find the sum of all odd numbers between 1 to n using python.
# num=int(input("Enter the number : "))
# total = 0
# for i in range(1,(num+1)):
#     if i%2!=0:
#         total =total+i
# print("Sum of all odd numbers : ",total)

#14). Write a program to count the number of digits in a number using python.
# num=str(input('Enter the digits : '))
# total = 0
# for i in num:
#         total =total+1
# print("The number of digits in a number : ",total)

#15). Write a program to find the first and last digits of a number using python.
# num=str(input('Enter the digits : '))
# total = 0
# for i in num:
#         total =total+1
# print("The number of digits in a number : ",total)


#16). Python Loops program to construct the following pattern,
# 1
# 22
# 333
# 4444
# 55555
# num = int(input('Enter the number : '))
# for i in range(1,num+1):
#    for j in range(i):
#        print(i,end='')
#    print('')


##16). Python Loops program to construct the following pattern,
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

# num = int(input('Enter the number : '))
# for i in range(1,num+1):
#    for j in range(1,i+1):
#        print(j,end='')
#    print('')


#17). Python Loops program to construct the following pattern,
#5 5 5 5 5
#4 4 4 4
#3 3 3
#2 2
#1

# num = int(input('Enter the number : '))
# for i in range(num,0,-1):
#    for j in range(i):
#        print(i,end=' ')
#    print('')



#18). Python Loops program to construct the following pattern,
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 15 14 13 12
# 11 10 9
# 8 7
# 6
# cout=1
# for i in range(5):
#     for j in range(i+1):
#         print(cout,end=' ')
#         cout=cout+1
#     print()
# for k in range(5,0,-1):
#     for l in range(k-1):
#         cout = cout - 1
#         print(cout,end=' ')
#     print()

#19). Python Loops program to construct the following pattern,
 #         *
 #       * *
 #     * * *
 #   * * * *
 # * * * * *

# limit=6
# for i in range(limit):
#     for j in range(limit-i):
#         print(" ",end=' ')
#     for k in range(i):
#         print('*',end=' ')
#     print()

#20). Python Loops program to construct the following pattern,
#   * * *
# * * * * *
# * *   * *
# * *   * *
# * * * * *
# * * * * *
# * *   * *
# * *   * *

for i in range(5):
    if i==0 or i==4:
        print(' ', end=' ')
    else:
        print('*', end=' ')
print()
for i in range(5):
    print('*', end=' ')
print()
for i in range(5):
    if i==2:
        print(' ', end=' ')
    else:
        print('*', end=' ')
print()
for i in range(5):
    if i==2:
        print(' ', end=' ')
    else:
        print('*', end=' ')
print()
for i in range(5):
    print('*', end=' ')
print()
for i in range(5):
    print('*', end=' ')
print()
for i in range(5):
    if i==2:
        print(' ', end=' ')
    else:
        print('*', end=' ')
print()
for i in range(5):
    if i==2:
        print(' ', end=' ')
    else:
        print('*', end=' ')