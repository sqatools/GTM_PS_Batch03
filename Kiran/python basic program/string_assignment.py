# question1
s1 = "IPL2024 CRICKET TROPHY"
first_char =s1[0]
last_char = s1[-1]
remaining_part = s1[1 : -1]
result = f"{last_char}{remaining_part}{first_char}"
print("result : ", result)

# question2
i = input("Enter sentence : ")
j = " "
k = 1
for k in range(len(i)):
    if k%2:
        j+=i[k]*2
    else:
        j+=i[k]
print(j)

# question 3
s2 = "GOOD MORNING"
first_char =s2[0]
last_char = s2[-1]
remaining_part = s2[-2: 0 : -1]
result = f"{last_char*2}{remaining_part}{first_char*2}"
print("result : ", result)

# 1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string.
char1 = input("Enter a string : ")
if len(char1)>2:
    char2 = char1[:2]+char1[-2:]
    print(char2)
else:
    print(" ")

# 2). Python string program that takes a list of strings and returns the length of the longest string.
char1 = input("Enter a string : ").split(",")
temp = 0
for char2 in char1:
    char3 = len(char2)
    if temp <char3:
        temp = char3
print(temp)

# 3). Python string program to get a string made of 4 copies of the last two characters
# of a specified string (length must be at least 2).
char1 = input("Enter a string : ")
index = 0
if len(char1) > 2:
    index = char1[-2:]
print(index*4)


# 4). Python string program to reverse a string if it’s length is a multiple of 4
char1 = input("Enter a string : ")
if len(char1)%4 == 0:
    print(char1[::-1])
else:
    print(char1)

# 5). Python string program to count occurrences of a substring in a string.
char1 = input("Enter a string : ")
#print(char1.count(input("enter substring ")))
char2=input("enter a substring: ")
count=0
i=0
while i<=len(char1)-len(char2):
    if char1[i:i+len(char2)]==char2:
        count+=1
    i+=1
print(count)

# 6). Python string program to test whether a passed letter is a vowel or consonant.
char1 = input("Enter a string : ")
#char2 ="0"
for char2 in char1:
    if "a"<=char2<="z" or "A"<=char2<="Z":
        #print("It is alphabet")
        if char2 in "AEIOU" or char2 in "aeiou":
            print("It is vowel",char2)
        else:
            print("It is consonent",char2)
    else:
        print("Invalid string = ",char2)


# 7). Find the longest and smallest word in the input string.
str2 = input("Enter a string : ")
l1 = str2.split(" ")
s_len = len(l1[0])
s_word = l1[0]
l_len=len(l1[0])
l_word=l1[0]
for word in l1:
    word_len = len(word)
    if word_len < s_len:
        s_len = word_len
        s_word = word
        print("smallest length :", s_len)
        print("smallest word :", s_word)
    if word_len > l_len:
        l_len = word_len
        l_word = word
        print("largest length :", l_len)
        print("largest word :", l_word)


# 8). Print most simultaneously repeated characters in the input string.
str_1 = input("Enter a string : ")
str_2 = " "
most_count = 0
most_digit = 0
counter = 1
for word in range(len(str_1)-1):
    if str_1[word] == str_1[word+1]:
        counter = counter+1
        if most_count<counter:
            most_count= counter
            str_2 = str_1[word]
    else:
        counter =1
print(str_2, most_count)


# 9). Write a Python program to calculate the length of a string with loop logic.
char1=input("Enter a string : ")
count = 0
for i in char1:
    count = count+1
print(count)


 # 10). Write a Python program to replace the second occurrence of any char with the special character $.
char1 = input("Enter the string :")
char2 = ""
for i in char1:
    if i in char2:
        char2+="$"
    else:
        #print(str1,end="")
        char2 = char2+i
print(char2)

# 11). Write a python program to get to swap the last character of a given string.
char1=input("Enter a string : ")
firstchar = char1[0]
lastchar = char1[-1]
remainchar = char1[1:-1]
result = f"{lastchar}{remainchar}{firstchar}"
print(result)


# 12). Write a python program to exchange the first and last character of each word from the given string.
char1 = input("Enter your string : ")
list1 = char1.split(" ")
char2 = ""
for i in list1:
    if len(i) > 1:
        list2 = i[-1] + i[1:-1] + i[0]
        char2 = char2 + " " + list2

    else:
        print(i)
print("Updated string : ", char2)


# 13). Write a python to count vowels from each word in the given string show as dictionary output.
char1 = input("Enter your string : ")
l1 = char1.split(" ")
dict11=dict()
for j in l1:
    count = 0
    for i in j:
        if i in "AEIOUaeiou":
            count = count+1
        dict11[j]=count
print(dict11)


# 14). Write a python to repeat vowels 3 times and consonants 2 times.
num = input("Enter a number: ")
result =""
digit = 0
for digit in num:
    if "a"<=digit<="z" or "A"<=digit<="Z":
        if digit in "AEIOUaeiou":
            result = digit*3
        else:
            result = digit*2
    print(result,end="")


# 15). Write a python program to re-arrange the string
s1 = input("Enter a string :")
l1 = s1.split(" ")
l1.reverse()
print(" ".join(l1))


# 16). Write a python program to get all the digits from the given string.
s1 = input("Enter your string : ")
l1 = s1.split(" ")
for i in l1:
    if i.isnumeric():
        print("digit is . ",i)


# 17). Write a python program to replace the words “Java” with “Python” in the given string.
s1 = "JAVA is the Best Programming Language in the Market"
s1 = s1.replace("JAVA", "Python")
print(s1)


# 18). Write a Python program to get all the palindrome words from the string.
s1 = input("Enter a string ")
l1 = s1.split(" ")
print(s1)
for word in l1:
    if word==word[::-1]:
        print("It is palindrome : ",word)

# 19). Write a Python program to create a string with a given list of words.
l1 = input("Enter the string in list formet : ").split(",")
l2 =list(l1)
print("given list is : ",l2)
l3=" ".join(l2)
print("The new stringis : ",l3)


# 20). Write a Python program to remove duplicate words from the string.
s1 = input("Enter a string : ")
l1 = s1.split(" ")
l2 = []
for value in l1:
    if value not in l2:
        l2.append(value)
print(" ".join(l2))


#21 Write a Python to remove unwanted characters from the given string.
s1 = input("Enter your string : ")
for word in s1:
    if word.isalpha():
        i = " ".join(word)
        print(i,end="")


# 22). Write a Python program to find the longest capital letter word from the string.
str_1 = input("Enter a string : ")
str_2 = str_1.split(" ")
str_empty = " "
for word in str_2:
    if word.isupper() and len(str_empty)<len(word):
        str_empty=word
        print("Longest capital letter word: ",str_empty)
        break
    else:
        print("No Capital letter word : ",str_1)
        break


# 23). Write a Python program to get common words from strings.
input1 = input("enter your first string : ").split(" ")
input2 = input("enter your second string : ").split(" ")
same_str = []
for i in input1:
    for j in input2:
        if i == j:
            same_str.append(i)

print(" ".join(same_str))



# 24). Write a Python program to find the smallest and largest word in a given string.
str1=input("Enter a sentance : ").split()
small_str1=str1[0]
large_str1=str1[0]
for i in str1:
    if len(i)<len(small_str1):
        small_str1=i
    elif len(i)>len(large_str1):
        large_str1=i
print("Small : ",small_str1)
print("large : ",large_str1)


# 25). Check whether the given string is a palindrome (similar) or not.
input1 = input("enter your first string : ")

if input1 == input1[::-1]:
    print("It is palindrome : ",input1)
else:
    print("not a palindrome")


# 26). Write a program using python to reverse the words in a string.
l1 = input("Enter your string : ")
for word in l1:
    l2=(l1[::-1])
print(l2)

l1 = input("Enter your string : ")
l2 = l1.split(" ")
print(" ".join(l2[::-1]))


# 27). Write a program to calculate the length of a string.
l1 = input("Enter your string : ")
count = 0
for word in l1:
    count+=1
print(count)


# 28). Write a program to calculate the frequency of each character in a string.
l2 = list(input("Enter your string : ").split())
dict1 ={}
for word in l2:
    for i in word:
        if i in dict1:
            dict1[i]+=1
        else:
            dict1[i] = 1
print(dict1)


# 29). Write a program to combine two strings into one.
str1 =input("enter your first string : ")
str2 = input("Enter your second string : ")
print(str1+str2)


# 30). Write a program to print characters at even places in a string.
str1 ='We are reading python'  #str1 =input("Enter your input : ")
output = ""
for i in range (len(str1)):
    if i%2 != 0:
        output+=str1[i]
print(output)

# 31). Write a program to check if a string has a number or not.
string = "python1"
count = 0
for char in string:
    if char.isnumeric():
        count += 1
if count > 0:
    print(True)
else:
    print(False)


# 32). Write a python program to count the number of vowels in a string.
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char in 'aeiouAEIOU':
        count+=1
print(count)


# 33). Write a python program to count the number of consonants in a string.
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char not in 'aeiouAEIOU' and 'a'<char<'z':
        count+=1
print(count)


# 34). Write a program to print characters at odd places in a string.
s1 = input("Enter your string :")
for char in range(len(s1)):
    if char%2 !=0:
        print(s1[char],end="")


# 35). Write a program to remove all duplicate characters from a given string in python.
s1 = input("Enter your string :")
output = ''
for char in s1:
    if char not in output:
        output+=char
print(output)


# 36). Write a program to check if a string has a special character or not
s1 = input("Enter your string :")
count = 0
for char in s1:
    if char.isalnum():
        count = 0

    else:
        count += 1
if count > 0:
    print("It contain special character")
else:
    print("It has no special character")


# 37). Write a program to exchange the first and last letters of the string
s1 = input("Enter your string :")
f_let = s1[0]
l_let = s1[-1]
output = f'{l_let}{s1[1:-1]}{f_let}'
print(output)


# 38). Write a program to convert all the characters in a string to Upper Case.
s1 = input("Enter your string :").upper()
print(s1)


# 39). Write a program to remove a new line from a string using python.
str1=("enter\n")
print(str1.rstrip())