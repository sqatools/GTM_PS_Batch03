#1). Python Dictionary program to add elements to the dictionary.
# dict1 = {'a' : 5, 'b' : 32}
# dict1['c']=21
# print(dict1)           # {'a': 5, 'b': 32, 'c': 21}

#2). Python Dictionary program to print the square of all values in a dictionary.
#Input : {‘a’: 5, ‘b’:3, ‘c’: 6, ‘d’ : 8}
#Output :
#a : 25
#b : 9
#c : 36
#d : 64
# dict1={'a':5 ,'b':3,'c':6,'d':8}
# for i in dict1:
#     print(i,dict1[i]**2)

#3). Python Dictionary program to move items from dict1 to dict2.
#Input :dict1 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’},dict2 = {}
#Output :dict1 = {},dict2 = {‘name’: ‘john’, ‘city’: ‘Landon’, ‘country’: ‘UK’}
# dict1 = {'name': 'john', 'city': 'Landon', 'country': 'UK’'}
# dict2 = {}
# for i in dict1:
#     dict2[i]=dict1[i]
# print('dict2:',dict2)            # dict2: {'name': 'john', 'city': 'Landon', 'country': 'UK'}
# print('dict1',dict1)

#4). Python Dictionary program to concatenate two dictionaries.
#Input :dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’},dict2 = {‘Age’ : 25, ‘salary’: ‘$25k’}
#Output :dict1 = {‘Name’: ‘Harry’, ‘Rollno’:345, ‘Address’: ‘Jordan’, ‘Age’ : 25, ‘salary’: ‘$25k’}
# dict1 = {'Name': 'Harry', 'Rollno':345, 'Address': 'Jordan'}
# dict2 = {'Age' : 25, 'salary': '$25k'}
# dict1.update((dict2))
# print('dict1:',dict1)    # dict1: {'Name': 'Harry', 'Rollno': 345, 'Address': 'Jordan', 'Age': 25, 'salary': '$25k'}
# print('dict2:',dict2)    # dict2: {'Age': 25, 'salary': '$25k'}


#5). Python Dictionary program to get a list of odd and even keys from the dictionary.
# Input :{1: 25, 5:’abc’, 8:’pqr’, 21:’xyz’, 12:’def’, 2:’utv’},Output :Even Key = [[8, ‘pqr’], [12, ‘def’], [2, ‘utv’]]
#Odd Key = [[1, 25], [5, ‘abc’], [21, ‘xyz’]]
# dict1={1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
# even_key=[]
# odd_key=[]
# for i,j in dict1.items():
#         if i%2==0:
#             even_key.append([i,j])
#         else:
#             odd_key.append([i,j])
# print('Even Key:',even_key)           # Even Key: [[8, 'pqr'], [12, 'def'], [2, 'utv']]
# print('Odd Key:',odd_key)             # Odd Key: [[1, 25], [5, 'abc'], [21, 'xyz']]


#6). Python Dictionary Program to create a dictionary from two lists.Input :list1 = [‘a’, ‘b’, ‘c’, ‘d’, ‘e’]|
#list2 = [12, 23, 24, 25, 15, 16],Output :{‘a’: 12, ‘b’: 23, ‘c’: 24, ‘d’: 25, ‘e’: 15}
# list1 = ['a','b','c','d','e']
# list2 = [12, 23, 24, 25, 15, 16]
# dict1={}
# for i in range(len(list1)):
#     dict1[list1[i]]=list2[i]
# print('Result:',dict1)          # Result: {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15}


#7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
#Input :[4, 5, 6, 2, 1, 7, 11],Output :{4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
# list1=[4, 5, 6, 2, 1, 7, 11]
# dict1={}
# dict1=dict((i,i**2) for i in list1)
# print('Result:',dict1)               # Result: {4: 16, 5: 25, 6: 36, 2: 4, 1: 1, 7: 49, 11: 121}


#8). Python Dictionary program to clear all items from the dictionary.
# dict1={4: 16, 5: 25, 6: 36, 2: 4, 1: 1, 7: 49, 11: 121}
# dict1.clear()
# print('dict1:',dict1)            # dict1: {}


#9). Python Dictionary program to remove duplicate values from Dictionary.Input :{‘a’: 12, ‘b’: 2, ‘c’: 12, ‘d’: 5, ‘e’: 35, ‘f’: 5}
#Output :{‘a’: 12, ‘b’: 2, ‘d’: 5, ‘e’: 35}
# dict1={'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
# dict2={}
# for i,j in dict1.items():
#     if j not in dict2.values():
#         dict2[i]=j
# print(dict2)              # {'a': 12, 'b': 2, 'd': 5, 'e': 35}

#10). Python Dictionary program to create a dictionary from the string.Input  = ‘SQATools’
#Output = {‘S’: 1, ‘Q’: 1, ‘A’: 1, ‘T’: 1, ‘o’: 2, ‘l’: 1, ‘s’: 1}
# str1='SQATools'
# dict1={}
# for i in str1:
#     dict1[i]=str1.count(i)
# print('Result:',dict1)           # Result: {'S': 1, 'Q': 1, 'A': 1, 'T': 1, 'o': 2, 'l': 1, 's': 1}


# 11). Python Dictionary program to sort a dictionary using keys.Input = {‘d’ : 21, ‘b’ : 53,  ‘a’: 13, ‘c’: 41}
# dict1={'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
# dict2={}
# for key in sorted(dict1):
#     dict2[key]=dict1[key]
# print(dict2)                 # {'a': 13, 'b': 53, 'c': 41, 'd': 21}


#12). Python Dictionary program to sort a dictionary in python using values.Input = {‘d’ : 14, ‘b’ : 52,  ‘a’: 13, ‘c’: 1 }
#Output= (c, 1) (a,13) (d, 14) (b, 52)
# dict1={'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }
# dict2={}
# sorted_values=sorted(dict1.values())
# print(sorted_values)            # [1, 13, 14, 52]
# for value in sorted_values:
#     for x,y in dict1.items():
#         if(value==y):
#             dict2[x]=y
# print(dict2)                    # {'c': 1, 'a': 13, 'd': 14, 'b': 52}


#13). Python Dictionary program to add a key in a dictionary.Input= {1:’a’, 2:’b’},Output= (1:’a’, 2:’b’, 3:’c’}
# dict1={1:'a',2:'b'}
# dict1[3]='c'
# print(dict1)           # {1: 'a', 2: 'b', 3: 'c'}


#14). Python Dictionary program to concatenate two dictionaries.Input:D1 = {‘name’ : ’yash’, ‘city’ :  ‘pune’}
#D1={‘course’:’python’,‘institute’:’sqatools’},Output:{‘name’:’yash’,city:‘pune’,‘course’:’python’,‘institute’:’sqatools’ }
# dict1 = {'name' : 'yash', 'city' :  'pune'}
# dict2 ={'course':'python','institute':'sqatools'}   # {'name': 'yash', 'city': 'pune', 'course': 'python', 'institute': 'sqatools'}
# dict1.update(dict2)
# print(dict1)


#15). Python Dictionary program to swap the values of the keys in the dictionary.Input = {name:’yash’, city: ‘pune’}
#Output = {'yash': 'name', 'pune': 'city'}
# dict1={'name':'yash', 'city': 'pune'}
# dict2={}
# for key,value in dict1.items():
#     dict2[value]=key
# print(dict2)              # {'yash': 'name', 'pune': 'city'}


#16). Python Dictionary program to get the sum of all the items in a dictionary.Input = {‘x’ : 23, ‘y’ : 10 , ‘z’ : 7}
#Output = 40
# dict1={'x' : 23, 'y' : 10 , 'z' : 7}
# value1=0
# for value in dict1.values():
#     value1 +=value
# print('Sum:',value1)              # Sum: 40


#17). Python Dictionary program to check whether a key exists in the dictionary or not.
#Input:Dict1 = {city:’pune’, state:’maharashtra’},Dict1[country],Output= ‘key does not exist in dictionary
# dict1 = {'city':'pune', 'state':'maharashtra'}
# for key in dict1.keys():
#     if key=='country':
#         print('Key exist')
#     else:
#         print('key does not exist in dictionary')


#18). Python program to iterate over a dictionary.Input :Dict1 = {food:’burger’, type:’fast food’}
#Output :food : burger
#        type : fast food
# dict1={'food':'burger', 'type':'fast food'}
# for key in dict1:
#     print(key,dict1[key])


#19). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
#Input: n=4,Output ={1 : 1, 2 : 8, 3 : 27, 4 : 64}
# value1=4
# dict1={}
# for i in range(1,5):
#     dict1[i]=i**3
# print('Result:',dict1)   # Result: {1: 1, 2: 8, 3: 27, 4: 64}

#20). Python Dictionary program to insert a key at the beginning of the dictionary.
#Input = { ‘course’ : ’python’,  ‘institute’ : ’sqatools’ },Insert : ( ‘name’ : ’omkar’ )
#Output= { ‘name’ : ’omkar’, ‘course’ : ’python’, ‘institute’ : ’sqatools’}
# dict1={ 'course' : 'python',  'institute' : 'sqatools' }
# dict2={'name' : 'omkar' }
# dict2.update(dict1)
# print(dict2)                  # {'name': 'omkar', 'course': 'python', 'institute': 'sqatools'}

#21). Python Dictionary  program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
#Output ={1 : 1, 2 : 4, 3 : 9, 4 : 16, 5 : 25}
# dict1={}
# for i in range(1,6):
#     dict1[i]=i**2
# print(dict1)         # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


#22). Python Dictionary program to find the product of all items in the dictionary.Input = { ‘a’ : 2, ‘b’ : 4, ‘c’ : 5}
#Output = 40
# dict1={ 'a' : 2, 'b' : 4, 'c' : 5}
# product1=1
# for i in dict1.values():
#     product1 *=i
# print('Product:',product1)              # Product: 40


#23). Python Dictionary program to remove a key from the dictionary.Input = {a:2,b:4,c:5},Output = (a:1,b:4}
# dict1={'a':2,'b':4,'c':5}
# dict2=dict1.popitem()
# print(dict1)               # {'a': 2, 'b': 4}


#24). Python Dictionary program to map two lists into a dictionary.Input : a = [ ‘name’, ‘sport’, ‘rank’, ‘age’]
#b = [‘Virat’, ‘cricket’, 1,  32],Output =  { ‘name’ : ’virat’, ‘sport’ : ’cricket’, ‘rank’: 1, ‘age’ : 32}
# list1=[ 'name', 'sport', 'rank', 'age']
# list2=['Virat', 'cricket', 1,  32]
# dict1={}
# for i in range(len(list1)):
#     dict1[list1[i]]=list2[i]
# print(dict1)                     # {'name': 'Virat', 'sport': 'cricket', 'rank': 1, 'age': 32}


#25). Python Dictionary program to find maximum and minimum values in a dictionary.
#Input : Dict = { ‘a’ : 10, ‘b’ : 44 , ‘c’ : 60, ‘d’ : 25},Output :Maximum value: 60,Minimum value: 10
# dict1 = { 'a' : 10, 'b' : 44 , 'c' : 60, 'd' : 25}
# print('Max value:',max(dict1.values()))         # Max value: 60
# print('Min value:', min(dict1.values()))        # Min value: 10


#26)....... Python Dictionary program to group the same items into a dictionary value.
#Input :list = [1,3,4,4,2,5,3,1,5,5,2,],Output = {1 : [1, 1], 2 :[2, 2], 3 : [3, 3], 4 : [4, 4], 5 : [5, 5, 5]}
# list1 = [1,3,4,4,2,5,3,1,5,5,2,]
# list2=sorted(list1)
# list2=[1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]         #  {1 : [1, 1], 2 :[2, 2], 3 : [3, 3], 4 : [4, 4], 5 : [5, 5, 5]}
# dict1={}
# for key in range(1,6):
#     print(dict1)

#27). Python Dictionary program to replace words in a string using a dictionary.String = ’learning python at sqa-tools’
#Dict ={ ‘at’ : ’is’, ‘sqa-tools’ : ’fun’},output = ‘learning python is fun’
# str1='learning python at sqa-tools'
# dict1={ 'at' : 'is', 'sqa-tools' : 'fun'}
# for key,value in dict1.items():
#     str1=str1.replace(key,value)
# print(str1)                         # learning python is fun

(OR)

# str1='learning python at sqa-tools'
# dict1={ 'at' : 'is', 'sqa-tools' : 'fun'}
# str2=str1.split()
# print(str2)            # ['learning', 'python', 'at', 'sqa-tools']
# str3=''
# for i in str2:
#     findValue = dict1.get(i)
#     if(findValue!=None):
#         str3 = str3 + " " + findValue
#     else:
#         str3 = str3 + " " + i
# print(str3)


#28). Python Dictionary program to remove a word from the string if it is a key in a dictionary.
#String = ’Sqatools is best for learning python’,Dict = { ‘best’ : 2, ‘learning’ : 6},Output = “sqatools is for python”
# str1 ='Sqatools is best for learning python'
# dict1 = { 'best' : 2, 'learning' : 6}
# count1=''
# for i in str1.split():
#     if i not in dict1:
#         count1 += i+' '
# print(count1)             # Sqatools is for python


#29). Python Dictionary program to remove duplicate values from dictionary values.
#Input:Dict1 = { ‘marks1’ : [23,28,23,69], ‘marks2’ : [ 25, 14,25,19] },Output= { ‘marks1’ : [28, 69], ‘marks2’ : [14,19] }
# dict1={'marks1':[23,28,23,69],'marks2' :[ 25, 14,25,19]}
# for key,value in dict1.items():
#     for value1 in value:
#         if value1 in value:
#             value.remove(value1)
# print(dict1)                        # {'marks1': [28, 69], 'marks2': [14, 19]}


#30). Python Dictionary program to check whether a dictionary is empty or not.Input:Dict1 = {},Output: Given dictionary is empty
# dict1 = {}
# if len(dict1)>0:
#     print('Given dictionary is not empty')
# else:
#     print('Given dictionary is empty')          # Given dictionary is empty


