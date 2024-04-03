list1 = [4, 18, 'Hello', 3.5, [5, 7, 8], (1, 2, 3), {'a': 123, 'b': 456}, True, {4, 7, 8, 9}]
# get values from list with the help of index
print(list1[5])  # (1, 2, 3)
print(list1[5][2])  # 3
print(list1[6]['a'])  # 123
print(list1[-3]['b'])  # 456
print(list1[-5][1])  # 7
print(list1[2][1])  # e

# List Slicing
listb = [4, 6, 8, 2, 'Hello', [3, 1, 5], 'Python', 'Programming']
print(listb[4:6])  # ['Hello', [3, 1, 5]]

print(listb[1:7])  # [ 6, 8, 2, 'Hello', [3, 1, 5], 'Python',]
print(listb[1:-1])  # # [ 6, 8, 2, 'Hello', [3, 1, 5], 'Python',]
print(listb[1::2])  # [6, 2, [3, 1, 5], 'Programming']
print(listb[-2:1:-1])  # ['Python', [3, 1, 5], 'Hello', 2, 8]

# Rule : list[initial index : last index: difference]
# print list in reverse order
print(listb[::-1])
# ['Programming', 'Python', [3, 1, 5], 'Hello', 2, 8, 6, 4]

# Apply loop on list values #
listc = [4, 7, 2, 8, 9, 12, 11]

# loop without index #
for val in listc:
    print(val)

# get all the even values from list
for val in listc:
    if val % 2 == 0:
        print(val)

# loop with indexing #
listd = [4, 7, 22, 11, 33]
for i in range(len(listd)):
    print(i, listd[i])

# List Methods #
print(dir(list))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# Add data to the list #
# append() method : This method add data to the list at the end of all values.

lista = [5, 7, 2, 8]
lista.append(40)
lista.append("Hello")
lista.append(['a', 'b', 'c'])
print("lista :", lista)  # [5, 7, 2, 8, 40, 'Hello', ['a', 'b', 'c']]

# insert() method : This method insert data at specific index location
list_b = [5, 7, 1, 66]
list_b.insert(1, 100)
print("list_b:", list_b)  # [5, 100, 7, 1, 66]

# extend() method: This method update the data from list1 to list2
list1 = ['a', 'b', 'c', 'd']
list2 = [4, 7, 9, 2]

list2.extend(list1)
print("list2 :", list2)  # [4, 7, 9, 2, 'a', 'b', 'c', 'd']
list1.extend(list2)
print("list2 :", list1)
list2.extend(list2)
print("list2 :", list2)

# list concatenation : combine two list with plus operator and create new list
listp = [4, 6, 8, 2]
listq = ['p', 'q', 'r', 's']
listr = listp + listq
print("listr :", listr)  # [4, 6, 8, 2, 'p', 'q', 'r', 's']

# Remove data from the list #
# remove() method : This method remove specific data from list

listy = [4, 6, 8, 22, 12, (3, 6, 8)]
listy.remove(22)
print("listy :", listy)  # [4, 6, 8, 12]
# listy.remove(100) # ValueError: list.remove(x): x not in list
listy.remove((3, 6, 8))
print("listy :", listy)  # [4, 6, 8, 12]

# pop() method: This method remove data from list using index position and return it
# the default index position is -1

listz = [4, 6, 8, 22, 12, 22, 8, 24]

val = listz.pop()  # default index will be -1
print("val :", val, listz)  # val : 24 [4, 6, 8, 22, 12, 22, 8]

val2 = listz.pop(-2)
print("val :", val2, listz)  # 22 [4, 6, 8, 22, 12, 8]

# clear method: This method remove all the data from the list
listh = [5, 7, 22, 44, 55]
listh.clear()
print("listh :", listh)  # []

# delete complete list variable from the memory
listj = [4, 8, 22, 99, 12]
del listj
# print("listj :", listj) # NameError: name 'listj' is not defined. Did you mean: 'list1'?

# delete partials values from list
listk = [4, 7, 11, 88, 23, 25]
del listk[2:5]
print("listk :", listk)  # [4, 7, 25]

# replace data in the list
list_x = [4, 7, 9, 2, 11]
list_x[2] = 900
print(list_x)

list_x[2:5] = [1, 2, 3]
print(list_x)

# count() method: This method return of number of occurrence of specific element
list_v = [3, 6, 8, 2, 6, 8, 3, 2, [8, 1, 2]]
print(list_v.count(8))

# index method : This return index position of specific element
list_z = [4, 77, 22, 66, 33]
print(list_z.index(66))  # 3

# sort() method: this method sort list data and modify the original list
list_n = [4, 1, 5, 2, 8, 11, 7]
list_n.sort()  # sort the list increasing order
print("list_n :", list_n)  # [1, 2, 4, 5, 7, 8, 11]

list_n.sort(reverse=True)  # sort the list in decreasing order
print("list_n :", list_n)  # [11, 8, 7, 5, 4, 2, 1]

# sorted() function : this function will provide the sorted result of the list without modifying the original list
list_m = [4, 6, 77, 11, 34, 2, 5, 6]
result1 = sorted(list_m)
print("result1 :", result1)  # result1 : [2, 4, 5, 6, 6, 11, 34, 77]
print(list_m)

result2 = sorted(list_m, reverse=True)
print("result 2:", result2)  # [77, 34, 11, 6, 6, 5, 4, 2]

# reverse() method : This method reverse the list values and modify the original list
list_l = [5, 7, 2, 1, 66, 88]
list_l.reverse()
print("list_l :", list_l)  # [88, 66, 1, 2, 7, 5]

# reversed function : reversed function provide the reverse list value and does not modify the original list
list_h = [4, 7, 22, 33, 55, 11]
data = reversed(list_h)
print(data)
for val in data:
    print(val, end=" ")
print()

# copy method:
# shallow copy: when we modify the reference list value, then original list will also be affected.
list_p = [4, 7, 2, 8, 1, 33]
list_q = list_p
list_r = list_q

list_r.append(100)
list_q.append(200)
print("list_p :", list_p)
print("list_q :", list_q)
print("list_r :", list_r)

# Deep copy : In deep copy we use copy method or pass the data from list1 to list2, if any modification done on list2,
# it won't affect list1

list_a = [44, 66, 22, 77, 12]
list_b = list_a.copy()
list_c = list_b.copy()

list_b.append(30)
list_c.append(40)

print("list a :", list_a)
print("list b :", list_b)
print("list c :", list_c)

# in built functions
list_w = [5, 7, 33, 44, 112, 6, 3]
print("max value :", max(list_w))
print("Min value :", min(list_w))
print("sum of the list :", sum(list_w))

# Write a python program to values which are divisible by 3 or 7
listr = [3, 7, 21, 55, 33, 42, 50, 11]
output = []

for i in listr:
    if i % 3 == 0 or i % 7 == 0:
        output.append(i)
    else:
        continue
print(output)

# Writing the above program in list comprehension to solve the problem
result = [x for x in listr if x % 3 == 0 or x % 7 == 0]
print("result :", result)

# Program to print the list result in given manner
list_o = [3, 6, 8, 11, 33, 9]
# result = [(3, 'odd'), (6, 'even'), (8, 'even'), (11, 'odd'), (33, 'odd'), (9, 'odd')]
result = []
for val in list_o:
    if val % 2 == 0:
        result.append((val, 'even'))
    else:
        result.append((val, 'odd'))
print("result :", result)

# solve with list of comprehension
result2 = [(val, 'even') if val % 2 == 0 else (val, 'odd') for val in list_o]
print("result 2 :", result2)


# apply nested loop in the list comprehension
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
result3 = [(x, y) for x in list1 for y in list2]
print("result3 :", result3)
# result3 : [(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

# PROGRAMS #

# write a python program to find the duplicate values from the list,
# and remove the duplicate value also.

list1 = [5, 7, 9, 22, 7, 5, 9, 11, 12]
duplicate = []
result = []

for val in list1:
    if val not in result:
        result.append(val)
    else:
        duplicate.append(val)

print("result :", result)
print("duplicate value :", duplicate)

# write a python move all positive value in right side and negative values in left side.
lista = [2, -4, -6, 7, 8, -22, 11, -16]
# positive = right side
# negative = left side
result = []

for val in lista:
    if val > 0:
        result.append(val)
    else:
        result.insert(0, val)

print("Result :", result)