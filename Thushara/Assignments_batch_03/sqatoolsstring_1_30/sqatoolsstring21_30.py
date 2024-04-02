"""
21). Write a Python to remove unwanted characters from the given string.
Input = “Prog^ra*m#ming”
Output = “Programming”
"""
st="Pro$%^^%gra$^%mming"
st1=""
for char in st:
    if char.isalnum():
        st1=st1+char
print(st1) #Programming

"""
22). Write a Python program to find the longest capital letter word from the string.
Input = “Learning PYTHON programming is FUN”
Output = “PYTHON”
"""
print("#"*50)
st = "Learning PYTHON programming is FUNNNNNNNNNNNNNN"
lst= st.split()
length=0
long=""
for word in lst:
    if word.isupper():
        if len(word)>length:
            length = len(word)
            long=word
print("The longest capital letter word :",long) #The longest capital letter word : FUNNNNNNNNNNNNNN

# print all the words in capital letters
lst=st.split()
lst1 =[]
for word in lst:
    if word.isupper():
        lst1.append(word)
print(" ".join(lst1)) #PYTHON FUNNNNNNNNNNNNNN

"""
23). Write a Python program to get common words from strings.
Input String1 = “Very Good Morning, How are You”
Input String1 = “You are a Good student, keep it up”
Output = “You Good are”
"""
print("#"*50)
st1="Very Good Morning, How are You"
st2="You are a Good student, keep it up"
lst=[]
for word in st1.split():
    if word in st2.split():
        lst.append(word)
print(" ".join(lst)) #Good are You

"""
24). Write a Python program to find the smallest and largest word in a given string.
Input = “Learning is a part of life and we strive”
Output = “a”, “Learning”
"""
print("#"*50)
st ="Learning is a part of life and we strive"
l_word=""
s_word=""
length=0
lst=st.split()
length1=len(lst[0])
for word in lst:
    if len(word)>length:
        length=len(word)
        l_word=word
    elif len(word)<length1:
        length1=len(word)
        s_word=word
print("The longest word in the given string :",l_word)
print("The shortest word in the given string :",s_word)
print("#"*50)
"""
25). Check whether the given string is a palindrome (similar) or not.
Input= qwertytrewq
Output= Given string is not a palindrome
"""
st ="qwertytrewq"
if st == st[::-1]:
    print("The given string is a palindrome :",st) #The given string is a palindrome : qwertytrewq
else:
    print("The given string is not a palindrome :",st)
print("#"*50)

"""
26). Write a program using python to reverse the words in a string.
Input= sqatools python
Output= slootaqs nohtyp
"""
st = "Write a program using python to reverse the words in a string."
lst=st.split()
lst1=[]
for word in lst:
    rev=word[::-1]
    lst1.append(rev)
print(" ".join(lst1)) # etirW a margorp gnisu nohtyp ot esrever eht sdrow ni a .gnirts
print("#"*50)
"""
27). Write a program to calculate the length of a string.
Input= “python”
Output = 6
"""
st= "Write a program to calculate the length of a string."
print("The length of the given string is :",len(st)) #The length of the given string is : 52

"""
28). Write a program to calculate the frequency of each character in a string.
Input = “sqatools”
Output = {‘s’:2, ‘q’:1, ‘a’: 1, ‘t’:1,‘o’:2, ‘l’:1, ‘s’:1}
"""
st="sqatools"
lst=st.split()
print(lst)

"""
29). Write a program to combine two strings into one.
Input: 
A = ’abc’
B = ’def’
Output = abcdef
"""
st1 ="Hello!"
st2="Good Morning"
print(st1+st2) #Hello!Good Morning
print("#"*50)

"""
30). Write a program to print characters at even places in a string.
Input = ‘sqatools’
Output = saol
"""
st="It's a good day to have  good day!"
for i  in range(len(st)):
    if i%2==0:
        print(st[i],end="")
    else:
        continue #I'  oddyt ae oddy
print()
print("#"*50)

