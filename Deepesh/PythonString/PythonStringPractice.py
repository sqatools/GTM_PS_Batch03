str1= 'Hello'
str2 = "Python Programming"
str3 = '''
In common usage, data is a collection 
of discrete or continuous values that 
convey information, 654353 describing the 
quantity, quality, ###*#&*^* fact, statistics, 
other basic units of meaning, or 
'''

str4 = """
In common usage, data is a collection 
of discrete or continuous values that 
convey information, describing the 
"""

str5 = "Hello we are learning 'Python' Programing"
str6 = 'Hope you are "enjoying" the learning Process'

print(str1, type(str1))
print("_"*50)

print(str2, type(str2))
print("_"*50)

print(str3, type(str3))
print("_"*50)

print(str4, type(str4))
print("_"*50)

print(str5, type(str5))
print("_"*50)

print(str6, type(str6))
print("_"*50)

# Ways to do the string formatting
Name = 'Rohan'
Age = 30
City = "Bangalore"
# My name is john and age is 25 and I am living in Mumbai


# 1. String concatenation
result = "My name is " +Name+ " and age is " +str(Age)+ " and I am living in " +City
print(result)

# 2. Format method
result2 = "My name is {} and age is {} and I am living in {}".format(Name, Age, City)
print(result2)

# F string formation
result3 = f"My name is {Name} and age is {Age} and I am living in {City}"
print(result3)

str1 = "Python"
# 0  1  2  3  4  5   +ve indexing
# P  y  t  h  o  n
#-6 -5 -4 -3 -2 -1   -ve indexing

print(str1[1])  # y
print(str1[-5]) # y

print(str1[-2]) # o

# Get length of the given string

print("length of the string :", len(str1))  # 6

# Apply loop on the string

# without indexing
stra = "Python Learning"
for char in stra:
    print(char, end=" ")


print()
# with indexing
for i in range(len(stra)):
    #print(i, stra[i])
    print(stra[i], end=" ")

print()
print("_"*40)
######################### String Slicing #######################
# Rule1 : str1[initial index : last index]
# It will return the substring, which includes the initials index value and exclude last index value

str_b = "Good Morning"
print("str_b[1:6] =",str_b[1:6]) # ood M

print("str_b[0:4] =",str_b[0:4]) # Good

print(str_b[2:-2])  # od Morni

print(str_b[-5:-1]) # rnin

print(str_b[-7: 10]) # Morni

print(str_b[-7:2]) # blank output

print(str_b[2:-7]) # od
