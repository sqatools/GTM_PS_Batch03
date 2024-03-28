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

str1 = "Python"
str2= ''
for i in range(len(str1)):
    if i%2==0:
        str2=str2+str1[i]
    else:
        str2=str2+str1[i]*2
    i=i+1
print(str2)                            # Pyythhonn

#4. Question3 ? str2 = "Good Morning" , Output = "ggninroM dooGG"
str3='Good Morning'
word1=str3[-1:-13:-1]
str4=f"{word1[0]}{word1}{word1[-1]}"
print(str4)                             # ggninroM dooGG

