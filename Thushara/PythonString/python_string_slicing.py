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
# My name is john and age is 25 ,and I am living in Mumbai.


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

#######################
print("_"*50)
### Rule2 str1[:last index]
# in this rule default initial index is zero and last index will be the position we have defined.

str1 = "IPL 2024 Mumbai Indian"
print(str1[: 5])   #IPL 2
print(str1[: -7])  # IPL 2024 Mumbai

#################
# Rule3 : str[initial index : ]
# in this rule the default last index will be end of the string
str2= "India is great country"
print(str2[2:]) # dia is great country
print(str2[-5:]) # untry

###########
# Rule4 : str1[initial index : last index : difference of index]
# In this rule initial index value will be included and last index value will excluded.

strc = "Good MorningH"

print(strc[2:8:1])  # od Mor

print(strc[2: 13: 2]) # o onnH

print(strc[-1:-6:-1]) # Hgnin

print(strc[-1:2:-1])  # HgninroM d

###################
print("_"*50)
# Rule5 str1[:last index:different index value]
# by default initial index is zero if the difference is positive
# by default initial index is -1 if the difference is negative


str_d = "Learning Python"

# default initial index is zero
print(str_d[:8:1])  # Learning

# default initial index is -1
print(str_d[:8:-1])  # nohtyP

print(str_d[:2:-2])  # nhy nn

##################
# Rule6 : str[::difference value]
# the default initial index will be zero and last index will end of the string if difference is positive
# The default initial index will be -1 and last index will be begining of string if difference is negative

str_e = "Very Good Evening"

# the default initial index will be zero and last index will end of the string if difference is positive
print(str_e[::1]) # Very Good Evening
print(str_e[::2]) # Vr odEeig


# The default initial index will be -1 and last index will be begining of string if difference is negative
print(str_e[::-1])  # gninevE dooG yreV
# str_e[-1:-len(str)-1: -1]

print(str_e[::-2]) # gieEdo rV

########################################################

# Practice Assingment

# replace first char with last char
str1 = "IPL 2024 Cricket Trophy"
fist_char = str1[0]
last_char = str1[-1]
remaining_part = str1[1:-1]
#result = f"{last_char}{remaining_part}{fist_char}"
result = f"{str1[-1]}{str1[1:-1]}{str1[0]}"
print("Result :", result)  # yPL 2024 Cricket TrophI


# question2:  Repeat every second character 2 times in the given string
str1 = "Python"
# output = "pyythhonn"
result = f"{str1[0]}{str1[1]*2}{str1[2]}{str1[3]*2}{str1[4]}{str1[-1]*2}"
print(result) #Pyythhonn

# question3 :
str2 = "Good Morning"
# output = "ggninroM dooGG"
result = f"{str2[-1]*2}{str2[-2:0:-1]}{str2[0]*2}"
print(result)
