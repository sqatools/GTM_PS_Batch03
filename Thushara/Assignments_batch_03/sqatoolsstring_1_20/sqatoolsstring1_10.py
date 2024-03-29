"""
1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
If the string length is less than 2, print True  instead of the empty string

"""
str_1 = "String program"
if len(str_1)<2:
    print(True)
else:
    print(str_1[:2]+str_1[-2:])
"""
2). Python string program that takes a list of strings and returns the length of the longest string.

"""
lst_1 = ['a','list','of','strings']
temp = 0
for i in lst_1:
    a = len(i)
    if a > temp:
        temp = a
print(temp)


"""
3). Python string program to get a string made of 4 copies of the last two characters of a
 specified string (length must be at least 2).

"""
str_1 = "Hello world"
print(str_1[-2:]*4)
"""
4). Python string program to reverse a string if it’s length is a multiple of 4.

"""
str_1 = "Good Morning"
a = len(str_1)
if a%4 == 0 :
    print(str_1[::-1])
"""
5). Python string program to count occurrences of a substring in a string.

"""
str_1 = "one two three one four one two one one"
sub = "one"
count = str_1.count(sub)
print(sub,"repeats",count,"times in the string")
"""
6). Python string program to test whether a passed letter is a vowel or consonant.

"""
str_1 = "hydrophobia"
for char in str_1:
    if char=='a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        print(char, "is a vowel")
    else:
        print(char,'is a consonant')

"""
7). Find the longest and smallest word in the input string.

"""
st = "Find the longest and smallest word in the input string."
st_lst= st.split(" ")
print(st_lst)
print("The longest word in the string:",max(st_lst,key=len))
print("The smallest word in the string:",min(st_lst,key=len))
str_1 = "learning Python programming"
str1_lst = str_1.split(" ")
print(str1_lst)
temp=0
for i in range(len(str1_lst)):
    if len(str1_lst[i])>temp:
        temp=len(str1_lst[i])
print(temp)
print("The longest word in the string: ",str1_lst[i])

"""
8). Print most simultaneously repeated characters in the input string.

"""
st = " pythonnnnnnnnn programmmmiiiiiing"
temp=1
count=0
char1=" "
for i in range(len(st)-1):
    if st[i]==st[i+1]:
        temp=temp+1
        if temp>count:
            count=temp
            char1=char1+st[i]
        else:
            temp=1
print("Most repeated character:",char1)
print("Number of repetition :",count)


"""
9). Write a Python program to calculate the length of a string with loop logic.

"""
st = "It's a good day to have a good day"
count=0
for char in st:
    count=count+1
print("length of the given string : ",count)
print(len(st))
"""
10). Write a Python program to replace the second occurrence of any char with the special character $.
Input = “Programming”
Output = “Prog$am$in$”
"""
st ="Good Morning"
result=""
for char in st:
    if char in result:
        result = result+"$"

    else:
        result = result+char
print(result)




