"""properties :
 - tuple is same as list but tuple will be declared in parentheses (). Ex: t1= (1,2,3,"Ashok")
 - tuple is immutable data type, cannot change once it is defined.
 - tuple is immutable so there are no methods. Only built-in functions will be used(Min, Max, Count etc.)
 - tuple follows positive and negative indexing as like string and list
 - tuple can contain any type of data, int, float, string, list, tuple, dict, set, boolean

 Summary:
 --------
There are four collection data types in the Python programming language:
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#       0  1  2  3
tup1 = (4, 7, 9, 10)
#      -4 -3 -2 -1

print(tup1, type(tup1))
print(tup1[2])  # 9
print(tup1[-3])  # 7

tup2 = (2, 3.5, "Python", False, [2, 8, 3, "Hi"], (4, 5, 6, "hi"), {1, 2, "hi"},
        {'a': 345, 'b': 478, 5: 4})
print(tup2)
print(tup2[3])
print(tup2[2][1])
print(tup2[4][1])
print(tup2[4][3])
print(tup2[7]["a"])
print(tup2[7][5])

# Tuple allows duplicate members
tup3 = (2, 3.5, "Python", False, [2, 8, 3, "Hi"], (4, 5, 6, "hi"), {1, 2, "hi"},
        {'a': 345, 'b': 478, 5: 4}, 2, 3.5, "Python", False, [2, 8, 3, "Hi"], (4, 5, 6, "hi"), {1, 2, "hi"},
        {'a': 345, 'b': 478, 5: 4})
print(tup3)

# slicing in tuple
tup4 = (4, 2.5, 'Hello', [4, 5, 7], {'a': 123, 'b': 456}, 111, 234, (3, 6, 7))
print(tup4[2:5])  # ('Hello', [4, 5, 7], {'a': 123, 'b' : 456})
print(tup4[-3:])  # (111, 234, (3, 6, 7))
print(tup4[-1:-4:-1])  # ((3, 6, 7), 234, 111)
print(tup4[1::2])  # (2.5, [4, 5, 7], 111, (3, 6, 7))
print(tup4[::-1])  # ((3, 6, 7), 234, 111, {'a': 123, 'b': 456}, [4, 5, 7], 'Hello', 2.5, 4)

# apply loop on the tuple
tup3 = (4, 6, 98, 12, 34, 35)
# without indexing
for val in tup3:
    print(val)
# with indexing
for i in range(len(tup3)):
    print(i, tup3[i])

# Tuple Methods #

print(dir(tuple))
# 'count', 'index'

tup5 = (4, 6, 8, 22, 4, 7, 8, 22)
print(tup5.count(22))
print(tup5.index(8))

# delete tup variable
del tup4
# print(tup4)
# name 'tup4' is not defined.

# sorted function - Always display the result in list
tup5 = (3, 7, 2, 8, 12, 67, 1)
result = sorted(tup5)
print(result)
print(tup5)

# reversed function#
result2 = reversed(tup5)
print(result2, [result2])

output = [data for data in result2]
print(output)
# for data in result:
#     print(data)

# Get Max, Min and sum from tuple values
tup6 = (55, 66, 77, 33, 223, 266)
print("Max value:", max(tup6))  # Max value: 266
print("Mix value:", min(tup6))  # Mix value: 33
print("Sum of values:", sum(tup6))  # Sum of values: 720

tup7 = (4, 7, 2, 66, 2)
print(tup7 * 3)  # (4, 7, 2, 66, 2, 4, 7, 2, 66, 2, 4, 7, 2, 66, 2)

list1 = [5, 7, 8]
print(list1 * 3)  # [5, 7, 8, 5, 7, 8, 5, 7, 8]
