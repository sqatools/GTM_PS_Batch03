# 1. Python Program to add two integer values
a = 20
b = 30
print("Addition of two integer values:", a + b)

# 2. Python Program to subtract two integer values.
c = 30
d = 40
print("Subtraction of two integer values:", d - c)

# 3. Python program to multiply two numbers.
e = 5
f = 6
print("Multiplication of two integer values are:", 5 * 6)

# 4. Python program to repeat a given string 5 times.
str1 = "SQATools"
print("Displaying the string 5 times:", str1 * 5)

# 5. Python program to get the Average of given numbers
g = 5
h = 10
i = 15
j = (g + h + i) / 3
print("Average of all 3 numbers is:", j)

# 6. Python program to get the median of given number
nums = [45, 60, 61, 66, 70, 77, 80, 85]
nums.sort()  # this will sort in ascending order
a = (len(nums)) / 2
print(nums[int(a)])  # incase, if 'a' is in float number, so we are converting into int.

# 7. Python program to print the square and cube of a given number.
k = 9
print("Square & Cube of k value is:", k ** 2, k ** 3)

# 8. Python program to interchange values between variables.
a = 10
b = 20
a, b = b, a
print("After interchange of A & B values are:", a, b)

# 9. Python program to solve this Pythagoras theorem (a2 + b2 = c2)
"""
In this Python basic program, we will solve the Pythagoras theorem, which states, 
the square of the hypotenuse is equal to the sum of squares of other sides 
of the right triangle.

a2 + b2 = c2
a = side of a right triangle
b = side of a right triangle
c = hypotenuse
"""
a = 5
b = 4
c = (a ** 2) + (b ** 2)
print(c)

# 10. Python program to solve the given math formula. (a + b)2 = a^2 + b^2 + 2ab
a = 2
b = 3
print(((a + b) ** 2) == (a ** 2) + (b ** 2) + 2 * a * b)

# 11. Python program to solve the given math formula. (a - b)2 = a^2 + b^2 - 2ab
a = 4
b = 5
print(((a - b) ** 2) == (a ** 2) + (b ** 2) - 2 * a * b)

# 12. Python program to solve the given math formula.a2 – b2 = (a-b)(a+b)
a = 9
b = 2
print((a ** 2) - (b ** 2) == (a - b) * (a + b))

# 13. Python program to solve the given math formula. (c + d)3 = c3 + 3cd(c+d) + d3
c = 10
d = 9
print(((c + d) ** 3) == (c ** 3) + (3 * c * d * (c + d)) + (d ** 3))

# 14. Python program to solve the given math formula.(a – b)3 = a3 – 3a2b + 3ab2 – b3
a = 7
b = 6
print(((a - b) ** 3) == (a ** 3) - (3 * (a ** 2) * b) + (3 * a * (b ** 2)) - (b ** 3))

# 15. Python program to calculate the area of square. area = a * a
a = 9
print("Area of square:", a ** 2)

# 16. Python program to calculate the area of a circle. Formula = PI*r*r
radius = 5
Pi = 3.14
print("Area of circle:", Pi * (radius * radius))

# 17. Python program to calculate the area of a cube. Formula = 6*a*a
a = 5
print("Area of cube:", 6 * a * a)

# 18. Python program to calculate the area of the cylinder. Formula = 2*PI*r*h + 2*PI*r*r
radius = 5
height = 6
Pi = 3.14
print("Area of cylinder:", 2 * Pi * radius * height + 2 * Pi * radius * height)

# 19. Python program to check whether the given number is an Armstrong number or not.
# Example: 153 = 1*1*1 + 5*5*5 + 3*3*3
num = 153
rev = 0
temp = num
while temp > 0:
    rem = temp % 10
    rev = rev + rem ** 3
    temp = temp // 10

if rev == num:
    print("It is a armstrong number")
else:
    print("It is not an armstrong number")

# 20. Python program to calculate simple interest. Formula = P+(P/r)*t
P = 1000
r = 1200
t = 12
print("Simple interest:", P + (P / r) * t)

# 21. Python program to print the current date in the given format Output: 2023 Jan 05
import datetime

date = datetime.datetime.now()
print(date.strftime("%Y %b %d"))



