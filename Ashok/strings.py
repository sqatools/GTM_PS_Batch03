"""
1 . string is a collection of characters.
2. length is a function to give the character of string.
3. operators on string - 1. Concatenation 2. Repetition 3. Indexing 4. Slicing 5. in 6. not in
4. string can be written in Single quotes(' '), Double quotes (" "), Single three quotes (''' '''),
    Double three quotes("""  """).
5. string is a immutable object. We can't modify.
"""

# Class work #
str1 = 'Hello'
str2 = "Python Programming"

str3 = '''In common usage, data is a collection of discrete or continuous values that convey information,
654353 describing the quantity, quality, ###*#&*^* fact, statistics, other basic units of meaning, or . '''

str4 = """In common usage, data is a collection of discrete or continuous values that
convey information, describing the. """

str5 = "Hello we are learning 'Python' Programing."
str6 = 'Hope you are "enjoying" the learning Process.'

print(str1, type(str1), "\n")
print(str2, type(str2), "\n")
print(str3, type(str3), "\n")
print(str4, type(str4), "\n")
print(str5, type(str5), "\n")
print(str6, type(str6), "\n")

# Ways to do string formatting.
Name = 'Sachin'
Age = 48
City = "Mumbai"

# String concatenation
result1 = "My name is " + Name + " and age is " + str(Age) + " and city is " + City
print(result1)

# Using format method
result2 = "My name is {} and age is {} and city is {}".format(Name, Age, City)
print(result2)

# f string formation
result3 = f"My name is {Name} and age is {Age} and city is {City}"
print(result3)

# stra = "Python"
#  0  1  2  3  4  5   +ve indexing
#  P  y  t  h  o  n
# -6 -5 -4 -3 -2 -1   -ve indexing

# Indexing
str7 = "Hello World"
print(str7[0], str7[1], str7[2], str7[3], str7[4], str7[5], str7[6], str7[7], str7[8], str7[9], str7[10])
# print(str7[11])  # IndexError: string index out of range
print(str7[-1], str7[-2], str7[-3], str7[-4], str7[-5], str7[-6], str7[-7], str7[-8], str7[-9], str7[-10], str7[-11])

# length of string
print(len(str7))  # 11

# applying loop on string - without indexing
for char in str7:
    print(char, end="")
print()

# applying loop on string - with indexing
for i in range(len(str7)):
    print(str7[i], end=" ")
print()

for i in range(len(str7)-1, -1, -1):
    print(str7[i], end=" ")
print()

# Slicing - Access a range of character in a string by using slice operator 'colon(:)'
# Rule1: str[initial index: last index], It will return the initial index value and exclude the last index value.
#   0   1   2   3   4    5    6    7     8   9    10    11  12  13  14  15
#   W   e   l   c   o    m    e          t   o          I   n   d  i   a
# -16 -15 -14 -13  -12  -11  -10   -9    -8  -7   -6   -5  -4  -3  -2  -1

str8 = "Welcome to India"
print(len(str8))
print(str8[0:16])
print(str8[-1:-len(str8)-1:-1])
print(str8[1:6])
print(str8[0:4])
print(str8[2: -2])
print(str8[-5: -1])  # Need to check with trainer
print(str8[-7: 12])
print(str8[-7: 2])   # Blank output
print(str8[2: -7])  # Need to check with trainer

# Rule2: str[:last index], In this rule default initial index is zero and last index will be the position
# which we defined.
print(str8[:5])
print(str8[:-7])

# Rule3: str[initial index:], In this rule default last index is will be end of string.
print(str8[5:])
print(str8[-7:])

# Rule 4: str[initial index: last index: difference of index],
# In this rule initial index value will be included and last index value will be excluded.
print(str8[2:8:1])
print(str8[2:13:2])
print(str8[-1: -6: -1])
print(str8[-1: 2: -1])

# Rule 5:str[:last index :difference index value]
# by default initial index value is zero if the difference is positive
# by default initial index value is -1  if the difference value is negative
print(str8[: -6: -1])
print(str8[: 2: -1])
print(str8[: 2: -2])

# Rule 6: [: : difference value]
# The default initial index will be zero and last index will end of the string if difference is positive
# The default initial index will be -1 and last index will be begining of string if difference is negative
print(str8[::1])
print(str8[::2])
print(str8[::-1])
print(str8[-1:-len(str8)-1:-1])  # Another way
print(str8[::-2])

# Practice - Summary with +ve indexing#
str11 = "Hi Hyderabad"
print(len(str11))
print(str11[0:12:1])                      # [Start: Stop: Step]
print(str11[0:len(str11):1])              # [Start: Stop: Step]
print(str11[:len(str11):1])               # [     : Stop: Step]
print(str11[::1])                         # [     :     : Step]
print(str11[::])                          # [     :     :     ]
print(str11[0::1])                        # [Start:     : Step]
print(str11[0:len(str11):])               # [Start: Stop:     ]
print(str11[0::])                         # [Start:     :     ]

# Practice - Summary with -ve indexing#
print(str11[-1:-13:-1])                      # [Start: Stop: Step]
print(str11[-1:-len(str11)-1:-1])            # [Start: Stop: Step]
print(str11[:-len(str11)-1:-1])              # [     : Stop: Step]
print(str11[::-1])                           # [     :     : Step]
print(str11[::])                             # [     :     :     ]  # Hi Hyderabad
print(str11[-1:-len(str11)-1:])              # [Start: Stop:     ]  # blank o/p
print(str11[-1::])                           # [Start:     :     ]  # o/p: d
print(str11[-1::-1])                         # [Start:     : Step]  # dabaredyH iH

# Practice #
# 1.  replace first char with last char
str1 = "IPL 2024 Cricket Trophy"
fist_char = str1[0]
last_char = str1[-1]
remaining_part = str1[1:-1]
result = f"{last_char}{remaining_part}{fist_char}"
# result = f"{str1[-1]}{str1[1:-1]}{str1[0]}"
print("Result :", result)  # yPL 2024 Cricket TrophI

# question2:  Repeat every second character 2 times in the given string
str12 = "Python"   # output = "pyythhonn"

# Question3:
str9 = "Good Morning"
fist_char = str9[0] * 2
last_char = str9[-1] * 2
remaining_part = str9[-2:-len(str9):-1]
result = f"{last_char}{remaining_part}{fist_char}"
print("Result :", result)

str10 = "Hello"
fist_char = str10[0] * 2
last_char = str10[-1] * 2
remaining_part = str10[-2:-len(str10):-1]
result = f"{last_char}{remaining_part}{fist_char}"
print(result)

