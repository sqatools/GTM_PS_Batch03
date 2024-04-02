list1 = [4, 18, 'Hello', 3.5, [5, 7, 8],
         (1, 2, 3), {'a': 123, 'b' : 456}, True,
         {4, 7, 8, 9}]

# get values from list with the help of index

print(list1[5])  # (1, 2, 3)
print(list1[5][2])  # 3
print(list1[6]['a']) # 123
print(list1[-3]['b']) # 456
print(list1[-5][1]) # 7
print(list1[2][1]) # e

# List Slicing

listb = [4, 6, 8, 2, 'Hello', [3, 1, 5], 'Python', 'Programming']
print(listb[4:6])  # ['Hello', [3, 1, 5]]

print(listb[1:7]) # [ 6, 8, 2, 'Hello', [3, 1, 5], 'Python',]
print(listb[1:-1]) # # [ 6, 8, 2, 'Hello', [3, 1, 5], 'Python',]
print(listb[1::2])  # [6, 2, [3, 1, 5], 'Programming']
print(listb[-2:1:-1]) # ['Python', [3, 1, 5], 'Hello', 2, 8]

# Rule : list[initial index : last index: difference]

# print list in reverse order
print(listb[::-1])
# ['Programming', 'Python', [3, 1, 5], 'Hello', 2, 8, 6, 4]

##### Apply loop on list values ####

listc = [4, 7, 2, 8, 9, 12, 11]

# loop without index

for val in listc:
    print(val)

print("_"*50)
# get all the even values from list
for val in listc:
    if val%2 == 0:
        print(val)

print("_"*50)
#### loop with indexing ####
listd = [4, 7, 22, 11, 33]

for i in range(len(listd)):
    print(i, listd[i])

############### List Methods ################

print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

######## add data to the list #########

# append() method : This method add data to the list at the end of all values.
print("_"*50)
lista = [5, 7, 2, 8]
lista.append(40)
lista.append("Hello")
lista.append(['a', 'b', 'c'])
print("lista :", lista) #  [5, 7, 2, 8, 40, 'Hello', ['a', 'b', 'c']]

###########
# insert() method : This method insert data at specific index location
print("_"*40)
list_b = [5, 7, 1, 66]
list_b.insert(1, 100)
print("list_b:", list_b) # [5, 100, 7, 1, 66]

##########
# extend() method: This method update the data from list1 to list2
print("_"*50)
list1 = ['a', 'b', 'c', 'd']
list2 = [4, 7, 9, 2]

#list2.extend(list1)
print("list2 :", list2) # [4, 7, 9, 2, 'a', 'b', 'c', 'd']

list2.extend(list2)
print("list2 :", list2)

#########
# list concatenation : combine two list with plus operator and create new list
print("_"*50)
listp = [4, 6, 8, 2]
listq = ['p', 'q', 'r', 's']

listr = listp + listq
print("listr :", listr) # [4, 6, 8, 2, 'p', 'q', 'r', 's']


######### Remove data from the list #########
# remove() method : This method remove specific data from list
print("_"*50)

listy = [4, 6, 8, 22, 12, (3, 6, 8)]
listy.remove(22)
print("listy :", listy)  # [4, 6, 8, 12]
# listy.remove(100) # ValueError: list.remove(x): x not in list
listy.remove((3, 6, 8))
print("listy :", listy)# [4, 6, 8, 12]


##########
# pop() method: This method remove data from list using index position and return it
# the default index position is -1
print("_"*50)
listz = [4, 6, 8, 22, 12, 22, 8, 24]

val = listz.pop() # default index will be -1
print("val :", val, listz) # val : 24 [4, 6, 8, 22, 12, 22, 8]

val2 = listz.pop(-2)
print("val :", val2, listz) # 22 [4, 6, 8, 22, 12, 8]


#########
# clear method: This method remove all the data from the list
print("_"*50)
listh = [5, 7, 22, 44, 55]
listh.clear()

print("listh :", listh) # []

###########
# delete complete list variable from the memory

listj = [4, 8, 22, 99, 12]
del listj
#print("listj :", listj) # NameError: name 'listj' is not defined. Did you mean: 'list1'?


# delete partials values from list
listk = [4, 7, 11, 88, 23, 25]

del listk[2:5]
print("listk :", listk) # [4, 7, 25]
