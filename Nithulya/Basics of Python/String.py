# Ways to do the string formatting
#1.
# input_Name = input("Enter your name : ")
# st1='Hello '+ input_Name + ' How are you?'
# print(st1)

#2.
# input_Name = input("Enter your name : ")
# st1='Hello {} How are you?'.format(input_Name)
# print(st1)

#3.
# input_Name = input("Enter your name : ")
# st1=f'Hello {input_Name} How are you?'
# print(st1)

##### Get length of the given string ####
#1.
# str1= 'Hello'
# for i in str1:
#     print(i,end=' ')

#2.
# str1 = 'Hello'
# for i in range(len(str1)):
#     print(str1[i],end=' ')


##### String Slicing #####
#1.
str1 = 'How are you?'
print('str1[4:10] : ',str1[4:12])      # are you?

#2.
str1 = 'How are you?'
print('str1[0:7] : ',str1[0:7])        # How are

#3.
str1 = 'How are you?'
print('str1[1:-1] : ',str1[1:-1])      # ow are you

#4.
str1 = 'How are you?'
print('str1[-8:-1] : ',str1[-8:-1])    # are you

#5.
str1 = 'How are you?'
print('str1[-8:7] : ',str1[-8:7])       # are

#6.
str1 = 'How are you?'
print('str1[-3:1] : ',str1[-3:1])      # blank output

#7.
str1 = 'How are you?'
print('str1[1:-3] : ',str1[1:-3])      #ow are y





