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

for i in range(len(str7) - 1, -1, -1):
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
print(str8[-1:-len(str8) - 1:-1])
print(str8[1:6])
print(str8[0:4])
print(str8[2: -2])
print(str8[-5: -1])
print(str8[-7: 12])
print(str8[-7: 2])  # Blank output
print(str8[2: -7])

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
# by default initial index value will be zero if the difference is positive
# by default initial index value will be -1  if the difference value is negative
print(str8[: -6: -1])
print(str8[: 2: -1])
print(str8[: 2: -2])

# Rule 6: [: : difference value]
# The default initial index will be zero and last index will end of the string if difference is positive
# The default initial index will be -1 and last index will be begining of string if difference is negative
print(str8[::1])
print(str8[::2])
print(str8[::-1])
print(str8[-1:-len(str8) - 1:-1])  # Another way
print(str8[::-2])

# Practice - Summary with +ve indexing#
str11 = "Hi Hyderabad"
print(len(str11))
print(str11[0:12:1])  # [Start: Stop: Step]
print(str11[0:len(str11):1])  # [Start: Stop: Step]
print(str11[:len(str11):1])  # [     : Stop: Step]
print(str11[::1])  # [     :     : Step]
print(str11[::])  # [     :     :     ]
print(str11[0::1])  # [Start:     : Step]
print(str11[0:len(str11):])  # [Start: Stop:     ]
print(str11[0::])  # [Start:     :     ]

# Practice - Summary with -ve indexing#
print(str11[-1:-13:-1])  # [Start: Stop: Step]
print(str11[-1:-len(str11) - 1:-1])  # [Start: Stop: Step]
print(str11[:-len(str11) - 1:-1])  # [     : Stop: Step]
print(str11[::-1])  # [     :     : Step]
print(str11[::])  # [     :     :     ]  # Hi Hyderabad
print(str11[-1:-len(str11) - 1:])  # [Start: Stop:     ]  # blank o/p
print(str11[-1::])  # [Start:     :     ]  # o/p: d
print(str11[-1::-1])  # [Start:     : Step]  # dabaredyH iH

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
str12 = "Python"  # output = "pyythhonn"
str2 = " "
for i in range(len(str12)):
    if i % 2 == 0:
        str2 = str2 + str12[i]
    else:
        str2 = str2 + str12[i] * 2
print(str2)

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

# String Methods #
print(dir(str))
"""
'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 
'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower',
 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 
 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 
 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 
 'translate', 'upper', 'zfill'   """

# Inquiry methods # - Will display true or false
print("HELLO".isupper())
print("Hello".isupper())
print("hello".isupper())
print("hello".islower())
print("Hello".islower())
print("HELLO".islower())
print("Hello".istitle())
print("Hello World".istitle())
print("hello".istitle())
print("hello World".istitle())
print("Hello123".isalnum())  # It will check whether string contain alphabets and numbers
print("Hello".isalpha())  # It will check whether string contain only alphabets.
print("hello".isascii())  # It will check only for ASCII character
print("hello".isidentifier())  # This method check whether a given string can be a valid variable name.
print("123456789".isnumeric())  # It will check whether string contain alphabets and numbers
print("12345 6789".isnumeric())  # It will check whether string contain alphabets and numbers

# Changing case #
# First letter will be upper case and the remaining letter will be lower case
print('hello dear'.capitalize())  # Hello dear

# Upper to lower case
print('HELLO'.lower())  # hello

# Lower to upper case
print('hello'.upper())  # HELLO

# First letter of every word will be Upper case and the remaining will be lower case
print('hEllo deAr'.title())  # Hello Dear

# Lower to Upper, Upper to lower
print('hEllo deAr'.swapcase())  # HeLLO DEaR

# count method: This method return counts the given sub string/char in given string.
print('We Learning Python Programming'.count("P"))  # 2
print('We Learning Python Programming'.count("ing"))  # 2
print('We Learning Python Programming'.count("p"))  # 0

# index() method : This method returns the index of any sub-string/char in the target string
print('We Learning Python Programming'.index("e"))  # 1
print('We Learning Python Programming'.index("ing"))  # 8
# print('We Learning Python Programming'.index("s"))  # ValueError: substring not found

# find method: This method find the sub-string/char in the target and string if it is available,
# then it will return index of substring else it will return -1
print('We Learning Python Programming'.find("e"))  # 1
print('We Learning Python Programming'.find("s"))  # -1 It means not available.

# split method: This method split the target string from given delimiter and return the list of substrings
str_s = "Today is sunny day"
result = str_s.split(" ")
print("Result :", result)  # ['Today', 'is', 'sunny', 'day']

str_ss = "I,am,working,as,software,engineer"
word_list = str_ss.split(",")
print(word_list)  # ['I', 'am', 'working', 'as', 'software', 'engineer']

str_sss = "I am working as software engineer"
word_list = str_sss.split(",")
print(word_list)
print(str_sss.split("i"))  # ['I am work', 'ng as software eng', 'neer']

url = "https://www.google.com"
protocol1 = url.split(":")[0]
protocol2 = url.split(":")[1]
print("protocol :", protocol1)  # https
print("protocol :", protocol2)  # //www.google.com
print("Web :", url.split(".")[0])  # https://www
print("domain :", url.split(".")[1])  # google
print("server :", url.split(".")[2])  # com
print(url.split("//")[1].split(".")[0])  # www

# replace method: This method replace the one word to another from given string.
print('a-b-c-d-e'.replace('-', ','))
print("Welcome to Hyderabad".replace("Welcome", "Hi"))
print("Welcome to Hyderabad".replace("Hyderabad", "India"))

# strip method: This method remove all the trailing space from given string
str3 = " Python Programming "
print(str3)
print(str3.strip())

# lstrip method: remove left side space, then we can use lstrip method
print(str3.lstrip())

# rstrip method: remove right side space, then we can use rstrip method
print(str3.rstrip())

print(str3.replace(" ", "-"))  # --Python-Programming--

# join method: This method join all the characters of the string with any combination
str_v = "Programming"
result = "-".join(str_v)
print(result)  # P-r-o-g-r-a-m-m-i-n-g

result2 = "&%T&*#$".join(str_v)
print("result2 :", result2)  # P&%T&*#$r&%T&*#$o&%T&*#$g&%T&*#$r&%T&*#$a&%T&*#$m&%T&*#$m&%T&*#$i&%T&*#$n&%T&*#$g

result3 = result2.replace("&%T&*#$", "")
print("result3 :", result3)  # Programming

# apply join method for list of values
list1 = ["Hello", "How", "Are", "you?"]  # Hello How Are you?
result4 = " ".join(list1)
print("result4 :", result4)

# apply join method for tuple
tup1 = ('8', '4', '5', '2', '67', '1', '7', '12')
result5 = "".join(tup1)
print("result5:", result5)

# Write a python program to get mobile numbers and email ids from given string ##########
str15 = """Search safer online 2333 with McAfee® Secure 434 Search powered by Yahoo. Color coded search 
testuser@facebook.com 5465465465 results tell you which sites 9898789789 are safe – and test@gmail.com 
which could be dangerous. McAfee® Secure Search updates your default admin@yahoo.com search provider 8768768756 
in Chrome to help you stay protected. """

word_list = str15.split()
for word in word_list:
    if word.isnumeric() and len(word) == 10:
        print("Mobile Number :", word)
    elif "@" in word:
        print("email :", word)

# Write a python programs to find out the smallest word from string.
str1 = "Hello Very good morning, We are A learning Python"
word_list = str1.split()
print(word_list)

s_len = len(word_list[0])
s_word = word_list[0]

for word in word_list:
    # print(word)
    word_len = len(word)
    if word_len < s_len:  # 5 < 5, 4< 5, 4< 4, 8 < 4, 2< 4, 3< 2, 8< 2, 6< 2
        s_len = word_len  # 5, 4, 2
        s_word = word  # Hello, Very, We

print("smallest length :", s_len)
print("smallest word :", s_word)

# Program: write a python code to find the most simultaneously repeated characters.

str2 = "GGoood Mornnning, Hoppppe you are doiiiiing good"

most_r_char = ''
most_r_count = 0

counter = 1

for i in range(len(str2) - 1):
    if str2[i] == str2[i + 1]:
        counter += 1
        if most_r_count < counter:
            most_r_count = counter
            most_r_char = str2[i]
            print("most repeated char :", most_r_char, ":", most_r_count)
        else:
            pass
    else:
        counter = 1

print("most repeated char :", most_r_char, ":", most_r_count)
