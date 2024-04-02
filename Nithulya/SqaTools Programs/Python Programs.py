#1).  Python Program to add two integer values.
import math

x= 5
y= 2
print("Total : ",x+y)

#2). Python Program to subtract two integer values.
x= 5
y = 2
print("Substract Value : ",x-y)

#3). Python program to multiply two numbers.
x= 5
y= 2
print("Multiplied Value : ",x*y)

#4). Python program to repeat a given string 5 times.
str1 = "Hello"
print(str1*5)

#5). Python program to get the Average of given numbers.
a=10
b=40
c=30
print("Average : ",a+b+c/3)

"""6). Find median. Take a list as input.Sort the given list using sort().Use the formula (n+1)/2 to find the median of the given list,
       where n is the length of the list.Print the output."""
list1 = [2,3,4,5,6,8,7]
list1.sort()
a=int(len(list1)/2)
print("Median : ",list1[a])

"""7) Take a number as input.Print the square and cube using the ** (power) method.To print the square use  **2 and
      for the cube use **3. Print the output."""
x = 2
print("Square value of 2  : ",x**2)
print("Cube value of of 2 : ",x**3)

#8).  Interchange values between variables.
a= 5
b= 6
a,b = b,a
print("Value of A : ",a)
print("Value of B : ",b)

"""9). Solve the Pythogorous theorem, which states, the square of the hypotenuse is equal to the sum of squares of other sides 
      of the right triangle."""
a = 6
b = 3
c = a**2+b**2
print("Hypotenious side : ",math.sqrt(c))

#10). Solve the given math formula. Formula : (a + b)2 = a^2 + b^2 + 2ab
a = 5
b = 6
z = a**2+2*a*b+b**2
print("(a+b)^2 : ", z)

#11). Solve the given math formula. Formula : (a – b)2 = a^2 + b^2 – 2ab
a = 5
b = 6
z = a**2-2*a*b+b**2
print("(a-b)^2 : ", z)

#12). Solve the given math formula. Formula : a2 – b2 = (a-b)(a+b)
a = 6
b = 5
z = (a+b)*(a-b)
print("a^2-b^2: ", z)

#13). Solve the given math formula. Formula : (a + b)3 = a3 + 3ab(a+b) + b3
a=3
b=2
z = a**3+3*a*b*(a+b)+b**3
print("(a+b)^3 : ", z)

#14). Solve the given math formula.Formula : (a – b)3 = a3 - 3a2b + 3ab2 - b3.
a=3
b=2
z = a**3-(3*a**2*b)+(3*a*b**2)-b**3
print("(a-b)^3 : ", z)

