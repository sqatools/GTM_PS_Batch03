### Get values from list with the help of index
# list1 = [4, 18, 'Hello', 3.5, [5, 7, 8],(1, 2), {'a': 123, 'b' : 456}, True,{4, 7, 8, 9}]
# print(list1[5])            # (1, 2)
# print(list1[5][1])         # 2
# print(list1[6]['a'])       # 123
# print(list1[-3]['b'])      # 456
# print(list1[-5][1])        # 7
# print(list1[2][1])         # e


### List Slicing
# lista = [2, 3, 4, 2, 'Python', [4, 1, 6], 'Hi', 'Java']
# print(lista[3:6])        # [2, 'Python', [4, 1, 6]]
# print(lista[1:7])        # [3, 4, 2, 'Python', [4, 1, 6], 'Hi']
# print(lista[1:-1])       # [3, 4, 2, 'Python', [4, 1, 6], 'Hi']
# print(lista[1::2])       # [3, 2, [4, 1, 6], 'Java']
# print(lista[-2:1:-1])    # ['Hi', [4, 1, 6], 'Python', 2, 4]
# print(lista[::-1])       # ['Java', 'Hi', [4, 1, 6], 'Python', 2, 4, 3, 2]


###  Apply loop on list values :
# lista = [1, 3, 2, 8, 10, 12, 14]
# # loop without index
# for i in lista:
#     print(i,end=' ')       # 1 3 2 8 10 12 14

# Get all the even values from list
# lista = [1, 3, 2, 8, 10, 12, 14]
# for i in lista:
#     if i%2 == 0:
#         print(i,end=' ')     # 2 8 10 12 14



### loop with indexing :
# lista = [4, 7, 22, 11, 33]
# for i in range(len(lista)):
#     print(i, lista[i])

############### List Methods ################


### add data to the list :

#1. append() method : This method add data to the list at the end of all values.
# list1 = [7, 7, 3, 8]
# list1.append(23)
# list1.append("Hi")
# list1.append([1,2,'a'])
# print("list1 :", list1)     # list1 : [7, 7, 3, 8, 23, 'Hi', [1, 2, 'a']]


#2. insert() method : This method insert data at specific index location
# list1 = ['a','b','c','d',1,33]
# list1.insert(2,140)
# print("list1:", list1)               # list1: ['a', 'b', 140, 'c', 'd', 1, 33]


#3. extend() method: This method update the data from list1 to list2
# list1 = ['hi', 'hello', 'happy', 'good']
# list2 = [41, 17, 19, 22]
# list1.extend(list2)
# print("list1 :",list1)       # list1 : ['hi', 'hello', 'happy', 'good', 41, 17, 19, 22]
#
# list2.extend(list1)
# print("list2 :",list2)      # list2 : [41, 17, 19, 22, 'hi', 'hello', 'happy', 'good', 41, 17, 19, 22]


#4. List concatenation : Combine two list with plus operator and create new list
# list1 = ['hi', 'hello', 'happy', 'good']
# list2 = [41, 17, 19, 22]
# listTotal= list1 + list2
# print("List Total :", listTotal)        # List Total : ['hi', 'hello', 'happy', 'good', 41, 17, 19, 22]


#5. remove() method : This method remove specific data from list
# list1 = ['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
# list1.remove('hello')
# print("list1 :", list1)             # list1 : ['hi', 'happy', [41, 17, 19, 22], 'good']
# list1.remove('Good Morning')        # ValueError: list.remove(x): x not in list
# list1.remove([41,17,19,22])
# print("list1 :", list1)               #list1 : ['hi', 'hello', 'happy', 'good']


#6. pop() method: This method remove data from list using index position and return it
# the default index position is -1
# list1=['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
# pop_val1 = list1.pop()
# print("pop_val1 :", pop_val1,',','list1','=', list1) # pop_val1 : good , list1 = ['hi', 'hello', 'happy', [41, 17, 19, 22]]
# pop_val2 = list1.pop(-2)
# print("pop_val2 :", pop_val2,',','list1','=', list1) # pop_val2 : happy , list1 = ['hi', 'hello', [41, 17, 19, 22]]


#7. clear method: This method remove all the data from the list
# list1=['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
# list1.clear()
# print("list1 :", list1)     # list1 : []


#7. delete complete list variable from the memory
#1.
# list1=['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
# del list1
# print('List1 : ',list1)       # # NameError: name 'list1' is not defined. Did you mean: 'list1'?

#2.
# list1=['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
# del list1[1:4]
# print('List1 : ',list1)       # List1 :  ['hi', 'good']

#3. Write a python move all positive value in right side and negative value in left side
# list1=[2,-4,-6,7,8,-22,11,-16]
# list2=[]
# list3=[]
# for i in list1:
#     if i<0:
#         list2.append(i)
#     else:
#         list3.append(i)
# list2.extend(list3)
# print('list2 : ',list2)   # list2 :  [-4, -6, -22, -16, 2, 7, 8, 11]


########## Replace data in the list
#1.
# list1 = [14, 79, 91, 322, 211, 515]
# list1[3]=150
# print('List1 :',list1)           # List1 : [14, 79, 91, 150, 211, 515]

#2.
# list1 = [14, 79, 91, 322, 211, 515]
# list1[1:3]=['a','b']
# print('List1 :',list1)          # List1 : [14, 'a', 'b', 322, 211, 515]

######### count() method: This method return of number of occurence of specific element
# list1 = ['a','b','a','c',['a','e','f'],'a']
# print('Count "a" in list1 :',list1.count('a'))        # Count "a" in list1 : 3


########## index method : This return index position of specific element
# list1=['a','b','a','c',['a','e','f'],'a']
# print(list1.index(['a','e','f']))             # 4

######### sort() method: this method sort list data and modify the original list
#1.
# list1 = [22,11,1,4,21,12,45,5]
# list1.sort()
# print('List1 :',list1)         # List1 : [1, 4, 5, 11, 12, 21, 22, 45]

#2.
# list1 = [22,11,1,4,21,12,45,5]
# list1.sort(reverse=True)
# print('List1 :',list1)           # List1 : [45, 22, 21, 12, 11, 5, 4, 1]


######### sorted() function : this function will provide the sorted result of the list without
#1.
# modifying the original list
# list1 = [22,11,1,4,21,12,45,5]
# list2=sorted(list1)
# print('List1 :',list1)         # List1 : [22, 11, 1, 4, 21, 12, 45, 5]
# print('List2 :',list2)         # List2 : [1, 4, 5, 11, 12, 21, 22, 45]


#2.
# list1 = [22,11,1,4,21,12,45,5]
# list2=sorted(list1,reverse=True)
# print('List1 :',list1)           # List1 : [22, 11, 1, 4, 21, 12, 45, 5]
# print('List2 :',list2)           # List2 : [45, 22, 21, 12, 11, 5, 4, 1]


######## reverse() method : This method reverse the list values and modify the original list
# list1 = [22,11,1,4,21,12,45,5]
# list1.reverse()
# print('List1:',list1)           # List1: [5, 45, 12, 21, 4, 1, 11, 22]


###### reversed function : reversed function provide the reverse list value and does not modify the original list
# list1 = [22,11,1,4,21,12,45,5]
# list2 = reversed(list1)
# for i in list2:
#     print(i,end=' ')           # 5 45 12 21 4 1 11 22


######## copy  method:
### Shallow copy: when we modify the reference list value, then original list will also be affected.
# list1 = [22,11,1,4,21,12,45,5]
# list2=list1
# list3=list2
# list2.append('a')
# list3.append('b')
# print('List1:',list1)       # List1: [22, 11, 1, 4, 21, 12, 45, 5, 'a', 'b']
# print('List2:',list2)       # List2: [22, 11, 1, 4, 21, 12, 45, 5, 'a', 'b']
# print('List3:',list3)       # List3: [22, 11, 1, 4, 21, 12, 45, 5, 'a', 'b']


### Deep copy : In deep copy we use copy method or pass the data from list1 to list2,
#               if any modification done on list2, it won't affect list1
# list1 = [22,11,1,4,21,12,45,5]
# list2=list1.copy()
# list3=list2.copy()
# list2.append('a')
# list3.append('b')
# print('List1:',list1)              # List1: [22, 11, 1, 4, 21, 12, 45, 5]
# print('List2:',list2)              # List2: [22, 11, 1, 4, 21, 12, 45, 5, 'a']
# print('List3:',list3)              # List3: [22, 11, 1, 4, 21, 12, 45, 5, 'b']


######### Max,Min, Sum :
# list1 = [22,11,1,4,21,12,45,5]
# print("Max value :", max(list1))        # Max value : 45
# print("Min value :", min(list1))        # Min value : 1
# print("Sum of the list :", sum(list1))  # Sum of the list : 121



#1. Write a python program to values which are divisible by 4 or 5
# list1=[4,3,5,16,10,8,12,21,25]
# list2=[]
# for i in list1:
#     if i%4== 0 or i%5 == 0:
#         list2.append(i)
#     else:
#         continue
# print('List2: ',list2)       # List2:  [4, 5, 16, 10, 8, 12, 25]

####   List comprehension to solve the problem
#1. Write a python program to values which are divisible by 4 or 5
# list1=[4,3,5,16,10,8,12,21,25]
# result = [i for i in list1 if i%4 == 0 or i%5 ==0]
# print("Result:", result)      # Result: [4, 5, 16, 10, 8, 12, 25]

#2. Program to print the list result in given manner
#   List2: [(4, 'even'), (3, 'odd'), (16, 'even'), (10, 'even'), (21, 'odd')]
# list1=[4,3,16,10,21]
# list2=[]
# for i in list1:
#     if i%2==0:
#         list2.append((i,'even'))
#     else:
#         list2.append((i,'odd'))
# print("List2:",list2)           # List2: [(4, 'even'), (3, 'odd'), (16, 'even'), (10, 'even'), (21, 'odd')]

#3. Program to print the list result in given manner
#   List2: [(4, 'even'), (3, 'odd'), (16, 'even'), (10, 'even'), (21, 'odd')]
#   Solve with list of comprehension
# list1=[4,3,16,10,21]
# list2 = [(i, 'even') if i%2==0 else (i, 'odd') for i in list1]
# print("List2:",list2)             # List2: [(4, 'even'), (3, 'odd'), (16, 'even'), (10, 'even'), (21, 'odd')]

#4.# Apply nested loop in the list comprehension
# Result: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]
# list1 = [1, 2]
# list2 = ['a', 'b', 'c']
# list3=[]
# for i in list1:
#     for j in list2:
#         list3.append((i,j))
# print('Result:',list3)         # Result: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

#5. Apply nested loop in the list comprehension
# list1 = [1, 2]
# list2 = ['a', 'b', 'c']
# result = [(i, j) for i in list1 for j in list2]
# print("Result:", result)       # Result: [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c')]

