# Ways to do the string formatting
# 1.
# input_Name = input("Enter your name : ")
# st1='Hello '+ input_Name + ' How are you?'
# print(st1)

# 2.
# input_Name = input("Enter your name : ")
# st1='Hello {} How are you?'.format(input_Name)
# print(st1)

# 3.
# input_Name = input("Enter your name : ")
# st1=f'Hello {input_Name} How are you?'
# print(st1)

##### Get length of the given string ####
# 1.
# str1= 'Hello'
# for i in str1:
#     print(i,end=' ')

# 2.
# str1 = 'Hello'
# for i in range(len(str1)):
#     print(str1[i],end=' ')


##### String Slicing #####
# 1.
# str1 = 'How are you?'
# print('str1[4:10] : ', str1[4:12])  # are you?

# 2.
# str1 = 'How are you?'
# print('str1[0:7] : ', str1[0:7])  # How are

# 3.
# str1 = 'How are you?'
# print('str1[1:-1] : ', str1[1:-1])  # ow are you

# 4.
# str1 = 'How are you?'
# print('str1[-8:-1] : ', str1[-8:-1])  # are you

# 5.
# str1 = 'How are you?'
# print('str1[-8:7] : ', str1[-8:7])  # are

# 6.
# str1 = 'How are you?'
# print('str1[-3:1] : ', str1[-3:1])  # blank output

# 7.
# str1 = 'How are you?'
# print('str1[1:-3] : ', str1[1:-3])  # ow are y

### Rule2 str1[:last index]
# print('-' * 50)
# 1.
# str1 = 'How are you?'
# print('str1[:7] : ', str1[:7])  # How are

# str1 = 'How are you?'
# print('str1[:-2] : ', str1[:-2])  # How are yo

### Rule3 : str[initial index : ]
# print('-' * 50)
# str1 = 'How are you?'
# print('str1[4:] : ', str1[4:])  # are you?

# str1 = 'How are you?'
# print('str1[-6:] : ', str1[-6:])  # e you?

### Rule4 : str1[initial index : last index : difference of index]
# print('-' * 50)
# str1 = 'How are you?'
# print('str1[1:9:1] : ', str1[1:9:1])  # ow are y

# str1 = 'How are you?'
# print('str1[1:11:2] : ', str1[1:11:2])  # o r o

# str1 = 'How are you?'
# print('str1[-1:-8:-1] : ', str1[-1:-8:-1])  # ?uoy er

# str1 = 'How are you?'
# print('str1[-1:1:-1] : ', str1[-1:1:-1])  # ?uoy era w

# str1 = 'How are you?'
# print('str1[-1:-8:-1] : ', str1[-1:-8:-2])  # ?o r

### Rule5 str1[:last index:different index value]
# print('-' * 50)
# str1 = 'How are you?'
# print('str1[:7:1] : ', str1[:7:1])  # How are

# str1 = 'How are you?'
# print('str1[:-3:1] : ', str1[:-3:1])  # How are y

# str1 = 'How are you?'
# print('str1[:-3:-1] : ', str1[:-3:-1])  # ?u

### Rule6 : str[::difference value]
# print('-' * 50)
# str1 = 'Testing'
# print('str1[::1] : ', str1[::1])  # Testing

# str1 = 'Testing'
# print('str1[::2] : ', str1[::2])  # Tsig

# str1 = 'Testing'
# print('str1[::-1] : ', str1[::-1])  # gnitseT

# str1 = 'Testing'
# print('str1[::-2] : ', str1[::-2])  # gisT

### Practice Assingment
# print('-' * 50)

#1. Replace first char with last char
# str1 = "Chase Dreams, Not Regrets"
# chr1 = str1[0]
# chrl = str1[-1]
# chrb = str1[1:-1]
# result = f"{chrl}{chrb}{chr1}"
# print("Result :", result)

# 2.
# str1 = "Chase Dreams, Not Regrets "
# chr1 = str1[:13]
# chr2 = str1[-13:27]
# result = f"{chr2}{chr1}"
# print("Result :", result)  # Not Regrets Chase Dreams,
# print('-'*50)

#3. Repeat every second character 2 times in the given string
    #str1='Python', Output = "pyythhonn"

# str1 = "Python"
# str2= ''
# for i in range(len(str1)):
#     if i%2==0:
#         str2=str2+str1[i]
#     else:
#         str2=str2+str1[i]*2
#     i=i+1
# print(str2)                            # Pyythhonn

#4. Question3 ? str2 = "Good Morning" , Output = "ggninroM dooGG"
# str3='Good Morning'
# word1=str3[-1:-13:-1]
# str4=f"{word1[0]}{word1}{word1[-1]}"
# print(str4)                             # ggninroM dooGG

### lower() method: This method convert all the characters in the lower case.
stra= "Be happy for this moment."
print(stra.lower())                    # be happy for this moment.


### upper() method : This method convert all the characters in the upper case.
stra= "Be happy for this moment."
print(stra.upper())                    # BE HAPPY FOR THIS MOMENT.

### islower() method : Check given string is lower or not
# stra='Happy'
# strb='happy'
# strc='HAPPY'
# print(stra.islower())   # False
# print(strb.islower())   # True
# print(strc.islower())   # False

### isupper method : This method check given string in upper or not
# stra='Happy'
# strc='HAPPY'
# print(stra.isupper())      # False
# print(strc.isupper())      # True

### swapcase method : This method convert all upper case to lower and lower case to upper.
# stra= "Be happy for this moment."
# print(stra.swapcase())       # bE HAPPY FOR THIS MOMENT.

### title method : This method convert the given sentence in the title case, it means first
#                  character of each word should be capital
# stra= "Be happy for this moment."
# print(stra.title())          # Be Happy For This Moment.

### istitle() method : This method check given string is title case or not.
# stra= "Be happy for this moment."
# strb= "Be Happy For This Moment."
# print("Is title method : ",stra.istitle())     # False
# print("Is title method : ",strb.istitle())     #

### count method: This method return count any given sub string/char in given string.
# stra= "Be happy for this moment."
# print("Count p : ",stra.count('p'))         # Count p :  2
# print("Count e : ",stra.count('e'))         # Count e :  2
# print("Count B : ",stra.count('B'))         # Count B :  1
#print("Count ent : ",stra.count('ent'))       # Count ent :  1


### index() method : This method return the index of any sub-string/char in the target string
# stra= "Be happy for this moment."
# print("Index of 'h' : ",stra.index('h'))          # Index of 'h' :  3
# print("Index of 'ent' : ",stra.index('ent'))      # Index of 'ent' :  21


### find method:  This method find the sub-string/char in the target and string
#                 if it is available, then it will return index of substring else it will return -1
# stra= "Be happy for this moment."
# print("Find of 'h' : ",stra.find('h'))     # Find of 'h' :  3
# print("Find of 'z' : ",stra.find('z'))     # Find of 'z' :  -1  #it is not available


### split method: This method split the target string from given delimeter and return the list of substrings
# stra= "Be happy for this moment."
# print(stra.split(' '))              # ['Be', 'happy', 'for', 'this', 'moment.']

# stra= "Be , happy , for , this , moment."
# print(stra.split(','))                     # ['Be ', ' happy ', ' for ', ' this ', ' moment.']

# stra= "Be happy for this moment."
# print(stra.split('a'))                       # ['Be h', 'ppy for this moment.']

# stra= "Be.happy.//for this moment."
# strb= stra.split('.')[0]
# print('word1 : ',strb)                   # word1 :  Be

# stra= "Be.happy.//for this moment."
# strb= stra.split('.')[1]
# print('word2 : ',strb)                    # word2 :  happy

# stra= "Be.happy.//for this moment."
# strb= stra.split('.')[2]
# print('word3 : ',strb)                     # word3 :  //for this moment


### replace method: This method replace the one word from another from given string.
stra='Traditional Art Forms of Kerala'
print(stra.replace("Kerala","India"))
