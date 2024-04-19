#1). Python Program How to read a file in reading mode.
# def readFile(filename):
#     with open(filename,'r') as file1:
#         data=file1.read()
#         print(data)
# readFile("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file2.txt")


#2). Python file program to overwrite the existing file content.
# def writeFile(filename):
#     with open(filename,'w') as file1:
#         data= file1.write("This file is updated")
# writeFile("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#3).  Python file program to append data to an existing file.
# def writeFile(filename):
#     with open(filename,'a') as file1:
#         data= file1.write("\nfile1 is updated")
# writeFile("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#4).  Python file program to get the file’s first three and last three lines.
# def getFile(filename):
#     with open(filename,'r') as file1:
#         data= file1.readlines()
#         for i in (data[:3]):
#             print(i)
#         for i in (data[-3:]):
#             print(i)
# getFile("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#5). Python file program to get all the email ids from a text file.
# def getEmail(filename):
#     with open(filename,'r') as file1:
#         data= file1.read().split()
#         str=''
#         for i in data:
#             if '@' in i:
#                 str=str+'\n'+i
#         print('Email : ',str)
# getEmail("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#6). Python file program to get a specific line from the file.
# def getLine(file1):
#     with open(file1,'r') as file1:
#         data= file1.readlines()
#         print("Second Line : ",data[1])
#
# getLine("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#7). Python file program to get odd lines from files and append them to separate files.
# def getOddLine(file1,file2):
#     with open(file1,'r') as file10:
#         data= file10.readlines()
#         str1=''
#         for i in range(len(data)):
#             if (i%2 ==0):
#                 str1 += '\n'+data[i]
#         print(str1)
#     with open(file2,'a') as file20:
#         for i in str1:
#             file20.write(i)
#
# getOddLine("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt",
#            "C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#8). Python file program to find the longest word in a file.
# def getLongWord(file1,file2):
#     with open(file1,'r') as file10:
#         data= file10.read().split()
#         longestWord=''
#         for i in data:
#             if len(i) > len(longestWord):
#                 longestWord = i
#             else:
#                 pass
#
#         print(longestWord)
#     with open(file2,'a') as file20:
#             file20.write(longestWord)
#
# getLongWord("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt",
#            "C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#9). Python file program to get the count of a specific word in a file.
# def getCountWord(file1):
#     with open(file1,'r') as file10:
#         data= file10.read().split()
#         countWord=0
#         for i in data:
#             if i =='can':
#                 countWord += 1
#         print('Total Count:',countWord)
#
# getCountWord("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")


#10).  Python file program to read a random line from a file.
# import random
# def getRandom(file1):
#     with open(file1, 'r') as file10:
#         data = file10.readlines()
#         data1=random.choice(data)
#         print(data1)
# getRandom("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#11).  Python file program to copy the file’s contents to another file after converting it to lowercase.
# def getLower(filename,file2):
#     with open(filename,'r') as file10:
#         data= file10.readline()
#         data1=data.lower()
#     with open(file2,'a') as file20:
#         file20.write(data1)
#
# getLower("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\hello.txt",
#             "C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#12). Python file program to copy the file’s contents to another file after converting it to uppercase.
# def getLower(filename,file2):
#     with open(filename,'r') as file10:
#         data= file10.readline()
#         data1=data.upper()
#     with open(file2,'a') as file20:
#         file20.write(data1)
#
# getLower("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\hello.txt",
#             "C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#13). Python file program to count all the words from a file.
# def getCount(filename):
#     with open(filename,'r') as file10:
#         data= file10.read().split()
#         count=0
#         for i in data:
#             count += 1
#         print("Total Words : ",count)
#
# getCount("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")


#14). Python file program to sort all the lines File as per line length size.
# def getSort(filename,filename2):
#     with open(filename,'r') as file10:
#         data= file10.readlines()
#         for i in range(len(data)):
#             for j in range(i+1,len(data)):
#                 if len(data[i]) > len(data[j]):
#                     temp=(data[i])
#                     data[i] = data[j]
#                     data[j]=temp
#                 else:
#                     pass
#     with open(filename2, 'w') as file20:
#         allLines=' '.join(data)
#         file20.write(allLines)
# getSort("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt",
#         "C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")

#15).  Python file program to get all odd and even length words in two lists.
# def getOddEven(filename):
#     with open(filename,'r') as file10:
#         data= file10.read().split()
#         even=[]
#         odd=[]
#         for i in data:
#             if len(i)%2==0:
#                 even.append(i)
#             else:
#                 odd.append(i)
#         print('Even : ',even)
#         print('Odd : ', odd)
# getOddEven("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")


#16). Python file program to get all mobile numbers from a file. e.g each mobile number size should be 10.
# def getPhone(file1):
#     with open(file1, "r") as file1_obj:
#         data = file1_obj.read().split()
#         str1=''
#         for i in data:
#             if len(i)==10 and i.isnumeric():
#                 str1 += '\n'+i
#         print(str1)
# getPhone("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#17). Python file program to get the file size of a file.
# import os
# def getSize(file1):
#         data1 = os.stat(file1)
#         print("Size of the file: ",data1.st_size)
# getSize("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#18).  Python file program to write a tuple to a file.
# def getTuple(file1):
#     tup = ('1','2','3','4','5')
#     with open(file1, "w") as file1_obj:
#         file1_obj.write(" ".join(tup))
#
# getTuple("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt")


#19). Python file program to check whether a file is closed or not.
# file1=open("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file5.txt",'r')
# data=file1.read()
# print(file1.closed)           # False
# file1.close()
# print(file1.closed)           # True

#20).  Python file program to extract characters from a text file into a list.
# def getChar(file1):
#     with open(file1, "r") as file1_obj:
#         data = file1_obj.read().split()
#         list1=[]
#         for i in data:
#             for j in i:
#                 if j.isalpha():
#                     list1.append(j)
#         print("Char : ",list1)
# getChar("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

#21). Python file program to count the total number of characters in a file.
# def getChar(file1):
#     with open(file1, "r") as file1_obj:
#         data = file1_obj.read().split()
#         countChar=0
#         for i in data:
#             for j in i:
#                 if j.isalpha():
#                     countChar += 1
#         print("Total Char : ",countChar)
# getChar("C:\\PythonAutomation\\GTM_PS_Batch03\\Nithulya\\Basics of Python\\FileHandling\\file1.txt")

