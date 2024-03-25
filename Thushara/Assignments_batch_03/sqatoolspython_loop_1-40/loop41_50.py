"""
41).  Python loops program to print the pattern T using Python Loops.

       Output :

       * * * * * * * * *
       * * * * * * * * *
               * * *
               * * *
               * * *
               * * *
               * * *

"""
for row in range(8):
    for column in range(9):
        if(row==1 or row ==2):
            print("*",end=" ")
        elif(3<=row<=8 and 3<=column<=5):
            print("*", end=" ")
        else:
            print(" ",end = " ")

    print()
"""
42).  Write a program to print number patterns using Python Loops.
 
     Output:
 
     1
     2   3
     4   5   6
     7   8   9   10
     11  12  13  14  15
     14  13  12  11
     10  9   8
     7   6
     5

"""
num=1
for row in range(6):
    for column in range(row):
        print(num,end=" ")
        num+=1
    print()
num=14
for row in range(4,0,-1):
    for column in range(row):
        print(num,end=" ")
        num-=1
    print()

"""
43). Write a program to print the pattern A using Python Loops.
 
    Output :
 
       *  *  *
    * * * * * *
    * *      * *
    * *      * *
    * * * * * *
    * * * * * *
    * *      * *
    * *      * *
    * *      * *
"""
for row in range (8):
    for column in range(6):
        if row==0 and (column ==0 or column ==5):
            print(" ",end=" ")
        elif (row==2 or row==3) and (column== 3 or column==2):
            print(" ", end=" ")
        elif (row==6 or row ==7) and (column ==3 or column==2):
            print(" ",end=" ")
        else:
            print("*",end=" ")
    print()

"""
 44). Write a program to print the pyramid structure using Python Loops.
 
    Output:
 
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
print("#"*50)
a=3
b=5
for row in range(5):
    for column in range(9):
        if a<column<b:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    a -= 1
    b += 1

    print()

"""
45). Write a program to count total numbers of even numbers between 1-100 using Python Loops.
Output = 50
"""
count=0
for i in range(1,101):
    if i%2 == 0:
        count+=1
    else:
        continue
print("Total numbers of even numbers between 1-100 :",count)
"""
46). Write a program to count the total numbers of odd numbers between 1-100 using Python Loops.
Output = 50
"""
count=0
for i in range(1,100):
    if i%2 != 0:
        count+=1
    else:
        continue
print("Total numbers of odd numbers between 1-100 :",count)

print("*"*50)
"""
47). Write a program to get input from the user if it is a number insert it into an empty list using Python Loops.
Input :
L=[]
125python
Output = [1,2,5]
"""
str1= input("Enter a string including numbers:")
l=[]
for char in str1:
    if char.isnumeric():

        l.append(int(char))
print(l)
