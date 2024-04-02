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
print("#"*50)
st = "Python is dynamically typed and garbage-collected."
word_list= st.split()
print(word_list)
sml_wd = word_list[0]
count=len(word_list[0])
for word in word_list:
    if len(word) < count:

        count=len(word)
        sml_wd=word


print("Smallest word in the list:",sml_wd)
print("Number of characters in the word:",count)
lrg_word = word_list[0]
count=len(word_list[0])
for word in word_list:
    if len(word) > count:
        count = len(word)
        lrg_wd = word


print("longest word in the list:",lrg_wd)
print("Number of characters in the word:",count)
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
"""
11). Write a python program to get to swap the last character of a given string.
Input = “SqaTool”
Output = “IqaTooS”
"""
st = "SqaTool"
print(st[-1]+st[1:-1]+st[0])
print("#"*50)
"""
12). Write a python program to exchange the first and last character of each word from the given string.
Input = “Its Online Learning”
Output = “stI enlino gearninL”
"""
st ="It's online Learning"
lst=[]
for word in st.split():
    result = word[::-1]
    lst.append(result)

print(" ".join(lst)) #s'tI enilno gninraeL

print("#"*50)
"""
13). Write a python to count vowels from each word in the given string show as dictionary output.
Input = “We are Learning Python Codding”
output = {“We” : 1, “are” : 2, “Learning” : 3, “Python”:1, “Codding”}
"""
st= "We are Learning Python Coding"
lst =st.split()
vowels="aeiou"
dictionary=dict()
print(lst)
for word in lst:
    count=0
    for char in word:
        if char in vowels:
            count=count+1
    dictionary[word]=count
print(dictionary)

"""
14). Write a python to repeat vowels 3 times and consonants 2 times.
Input = “Sqa Tools Learning”
Ouput = “SSqqaaa TToooooollss LLeeeaaarrnniiinngg”

"""
print("#"*50)
st= "Sqa Tools Learning"
v="aeiou"
st1=""
for char in st:
    if char in v:
        char=char*3
        st1= st1+char
    else:
        char = char*2
        st1=st1+char

print(st1) #SSqqaaa  TToooooollss  LLeeeaaarrnniiinngg
"""
15). Write a python program to re-arrange the string.
Input = “Cricket Plays Virat”
Output = “Virat Plays Cricket”
"""
print("#"*50)
st="Cricket Plays Virat"
lst=st.split(" ")
print(" ".join(lst[::-1])) #Virat Plays Cricket

"""
16). Write a python program to get all the digits from the given string.
Input = “””
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen
“””
Output = [1112, 5324, 1773, 5324, 555]
"""
st ="""
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen"""
for num in st.split():
    if num.isnumeric():
        print(num,end=" ") #1112 1773 444 5324 555
print()
print("#"*50)

"""
17). Write a python program to replace the words “Java” with “Python” in the given string.
Input = “JAVA is the Best Programming Language in the Market”
Output = “Python is the Best Programming Language in the Market”
"""
st = "JAVA is the Best Programming Language in the Market"
st1= st.replace("JAVA","Python")
print(st1) #Python is the Best Programming Language in the Market

"""
18). Write a Python program to get all the palindrome words from the string.
Input = “Python efe language aakaa hellolleh”
output = [“efe”, “aakaa”, “hellolleh”]
"""
st=Input = "Python efe language aakaa hellolleh"
lst=st.split()
for word in lst:
    if word==word[::-1]:
        print(word +" is palindrome")
    else:
        print(word +" is not palindrome")
"""
output ___________Python is not palindrome
efe is palindrome
language is not palindrome
aakaa is palindrome
hellolleh is palindrome
"""
lst1=[]
for word in st.split():
    if word == word[::-1]:
        lst1.append(word)
print(lst1) #['efe', 'aakaa', 'hellolleh']
"""
19). Write a Python program to create a string with a given list of words.
Input = [“There”, “are”, “Many”, “Programming”, “Language”]
Output = There are many programming languages.
"""
lst = ["There","are","many","programming","languages"]
print(" ".join(lst)) #There are many programming languages
print("#"*50)

"""
20). Write a Python program to remove duplicate words from the string.
Input = “John jany sabi row john sabi”
output = “John jany sabi row”
"""

st = "John jany sabi row john sabi"
lst=st.split()
lst1=[]
for word in lst:
    if word  not in lst1:
        lst1.append(word)
print(" ".join(lst1)) #John jany sabi row john

