#1). Write a Python program to get a string made of the first and the last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
# str1=input("Enter the string value : ")
# if len(str1)<2:
#     print("True")
# else:
#     print(str1[:2]+str1[-2:])   #Enter the string value : Hello  Output: Helo

#2). Python string program that takes a list of strings and returns the length of the longest string.
# str1=['Hello','a','abc','Easter']
# char1=0
# for i in str1:
#     if len(i)>char1:
#         char1 =len(i)
# print('Longest string : ',char1)          # Longest string :  6

#3). Python string program to get a string made of 4 copies of the last two characters of a specified
# string (length must be at least 2).
# str1=input("Enter the string : ")
# if len(str1) > 2:
#     print(str1[-2:]*4)
# else:
#     print("Enter valid string with minimum of 2 Characters")  #Enter the string with 5 characters : Hello
                                                              # Output : lolololo


#4). Python string program to reverse a string if it’s length is a multiple of 4.
# str1=input('Enter the string :')
# if len(str1)%4==0:
#     print(str1[::-1])
# else:
#     print('String length is not multiple of 4')


#5). Python string program to count occurrences of a substring in a string.
# stra= "Be happy for this moment."
# print('Count - for : ',stra.count('for'))    # Count - for :  1

#6). Python string program to test whether a passed letter is a vowel or consonant.
# str1=input('Enter the String : ')
# for i in str1:
#     if ((i == 'a' or i == 'A') or (i == 'e' or i == 'E') or (i == 'i' or i == 'I') or (i == 'o' or i == 'O')
#         or (i == 'u' and i == 'U')):
#         print(f'The string {i} is Vowel')
#     else:
#         print(f'The string {i} is Consonant')

#7). Find the longest and smallest word in the input string.
# str1= "Be happy for this moment."
# str2=str1.split(' ')
# longest=""
# shortest=str1
# for i in str2:
#     if len(i)>len(longest):
#         longest=i
#     if len(i)<len(shortest):
#         shortest=i
# print('Longest String : ',longest)
# print('Shortest String : ',shortest)

#8). Write a Python program to calculate the length of a string with loop logic.
# str1= "Be happy for this moment."
# cout=0
# for i in str1:
#     cout += 1
# print('Length of the String with Loop Logic : ',cout)
# print('Length of the String with len() : ',len(str1))


#9). Write a Python program to replace the second occurrence of any char with the special character $.
# str1 = "Be happy for this moment."
# total = ' '
# for i in str1:
#     if i in total:
#         total = total+ '$'
#     else:
#         total += i
# print(total)


#10. Write a python program to get to swap the last character of a given string.
# str1= 'Be Happy'
# str2=str1[-1]+str1[1:7]+str1[0]
# print(str2)                            # ye HappB


#11). Write a python program to exchange the first and last character of each word from the given string.
# str1 = "Its Online Learning"
# str2 = str1.split(' ')
# total=' '
# for i in str2:
#     str3=i[-1]+i[1:-1]+i[0]
#     total += " " +str3
# print(total)                     #'stI enlinO gearninL'


#12). Write a python to count vowels from each word in the given string show as dictionary output.
# str1= 'We are Learning Python Codding'
# str2=str1.split( )
# str3 =['a','A','e','E','i','I','O','o','u','U']
# dictionary=dict()
# for i in str2:
#     print(i)
#     count = 0
#     for char1 in i:
#         if char1 in str3:
#             count +=1
#     print(count)
#     dictionary[i]=count
# print(dictionary)                 # {'We': 1, 'are': 2, 'Learning': 3, 'Python': 1, 'Codding': 2}


#13).Write a python to repeat vowels 3 times and consonants 2 times.
# str1 = 'Sqa Tools Learning'
# str2='AEIOUaeiou'
# total=''
# for i in str1:
#     if i in str2:
#         total += i*3
#     else:
#         total += i*2
# print(total)                 # SSqqaaa  TToooooollss  LLeeeaaarrnniiinngg


#14).16). Write a python program to get all the digits from the given string.
# str1 = '''Sinak’s 1112 aim is to 1773 create a new generation of people who
# understand 444 that an organization’s 5324 success or failure is
# based on 555 leadership excellence and not managerial
# acumen'''
# str2 = str1.split( )
# str3=[]
# for i in str2:
#     if i.isnumeric():
#         str3.append(i)
# print(str3)                  # ['1112', '1773', '444', '5324', '555']


#15). Write a python program to replace the words “Java” with “Python” in the given string.
# Input = 'JAVA is the Best Programming Language in the Market'
# str1=Input.replace('JAVA','Python')
# print(str1)                          # Python is the Best Programming Language in the Market


#16). Write a Python program to get all the palindrome words from the string.
#output = [“efe”, “aakaa”, “hellolleh”]
# Input = 'Python efe language aakaa hellolleh'
# str1=Input.split( )
# str2=[]
# for i in str1:
#     if i ==i[::-1]:
#         str2.append(i)
# print(str2)                  # ['efe', 'aakaa', 'hellolleh']


#17). Write a Python program to create a string with a given list of words.
# Input = ['There', 'are', 'Many', 'Programming', 'Languages']
# str1=' '.join(Input)
# print(str1)               # There are Many Programming Languages


#18). Write a Python program to remove duplicate words from the string.
# Input = 'John jany sabi row John sabi'
# str1=Input.split(' ')
# str2=[]
# for i in str1:
#     if i not in str2:
#         str2.append(i)
# print(' '.join(str2))               # John jany sabi row

#19). Write a Python to remove unwanted characters from the given string.
#1
# Input = 'Prog^ra*m#ming'
# total=' '
# for i in Input:
#     if i.isalpha():
#         print(i,end='')     # Programming

#2
# Input = 'Py(th)#@&on Pro$*#gram'
# total=' '
# for i in Input:
#     if i.isalpha():
#         print(i,end='')           # PythonProgram


#20). Write a Python program to find the longest capital letter word from the string.
# Input = 'Learning PYTHON programming is FUN'
# str1=Input.split( )
# largest=""
# for i in str1:
#     if i.isupper() and len(i)>len(largest):
#         largest=i
# print(largest)


#21). Write a Python program to get common words from strings.
# str1 = 'Very Good Morning, How are You'
# str2 = 'You are a Good student, keep it up'
# list1=[]
# for i in str1.split( ):
#     if i in str2.split( ):
#         list1.append(i)
# print(' '.join(list1))             # Good are You





