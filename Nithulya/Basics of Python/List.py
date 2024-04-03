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
list1=['hi', 'hello', 'happy',[41, 17, 19, 22], 'good']
del list1[1:4]
print('List1 : ',list1)       # List1 :  ['hi', 'good']
