"""
Data types can be classified into
1. Numeric -> i). Integer ii). Float iii). Complex Number iv) bool v) complex
   --> All numeric data types are immutable. Once it is defined we cannot modify
2. Sequential -> i). String ii). List  iii). Tuple iv) byte v) byte array
   --> List is mutable. We can change it.
   --> String, Tuple is immutable, we cannot change it.
3. Dictionary -> i). dict
   --> It is a key value based pair.
   --> key should be immutable & unique and value should be mutable & allows different types of data
4. Set - i). set ii). frozenset
   --> set is mutable data type, we can modify at any point of time.

Summary:
--------
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

# Integer Data Type #
""" Properties:
 - Integer is immutable data type, once it is defined we can not change it.
 - There is no as such limit for integer data type. any long number we can defined as integer.
"""
var1 = 50
var2 = 5456456456546546
var3 = 0
print(type(var1))
print(type(var2))
print(type(var3))
var4 = int()
print(type(var4), var4)

a = 100
b = 200
c = 100 + 1
print(c)

# Float Data Type #
""" Properties:
 - Float is immutable data type, once it is defined we can not change it.
 - There is no as such limit for float data type. any long number we can defined as float.
"""
print("_" * 50)
vara = 56.55
varb = 0.0
varc = 43534534.34543534534534543
print(vara, type(vara))  # 56.55 <class 'float'>
print(varb, type(varb))  # 0.0 <class 'float'>
print(varc, type(varc))  # 43534534.34543534 <class 'float'>

# Complex data type #
""" Properties:
 - complex number is the combination of real and imaginary number that's represent with x+yj
 - complex is the immutable data type, once it is defined we can not change it.
 - There is no as such limit for complex data type. any long number we can defined as complex values.
"""

# Sequential data type #
# String Data Type #
str1 = "H"
str2 = 'Python'
str3 = """
All Python releases are Open Source. 
Historically, most, but not all, 
Python releases have also been 
GPL-compatible. 
The Licenses page details 
GPL-compatibility and Terms and Conditions. 
"""
str4 = '''
This site hosts the "traditional" 
implementation of Python (nicknamed CPython). 
A number of alternative implementations are
'''
print(str1, type(str1))
print("_" * 50)
print(str2, type(str2))
print("_" * 50)
print(str3, type(str3))
print("_" * 50)
print(str4, type(str4))

str5 = "Hello"
#  0  1   2  3  4   +ve indexing
#  H  E   L  L  O
# -5 -4  -3 -2 -1   -ve indexing

print(str5[1])  # e
print(str5[-4])  # e

stra = "Python Programming"
strb = "Good Morning"
strc = stra + strb
print("strc :", strc)

# re-assignment of value in same variable
stra = "Python is Programming"
print(stra)
print(dir(str))

# List #
""" Properties
1. List is a mutable data type. 
2. List is a heterogeneous, it means can hold any type of data in variable.
3. Allow duplicates.
4. Allow indexing. Forward indexing(starts with 0). Negative/Backward indexing (Starts with -1 from right side)
5. Allow slicing [Start: Stop: Skip] 6. Lists have multiple methods.

List can be created in two ways.
1. mylist1 = ['A', 'B', 'C', 'D', 'E', 'F'] or mylist2 = ['john', 'Ravi', '123', '45.67', '5+7J', 'F']
2. mylist3 = list((1,2,3,4,5)) here list is a function name.
3. Length function (len) cane be used in list.
4. List can contain any type of data, int, float, string, list, dict, tuple, set, boolean
"""
list1 = [2, 3.5, 'Hello', True, [4, 6], (6, 8, 9), {1, "hi"}, {'a': 123, 'b': 444}]
print(list1, type(list1))
# [2, 3.5, 'Hello', True, [4, 6], (6, 8, 9), {1, "hi"}, {'a': 123, 'b': 444}] <class 'list'>

list2 = []
print("list2 :", list2, type(list2))
# list2 : [] <class 'list'>

#        0   1   2   3   4    +ve indexing
list3 = [55, 77, 88, 22, 33]
#       -5  -4   -3  -2  -1   -ve indexing

print(list3[2])  # 88
print(list3[-1])  # 33

#        0  1          2          3
list4 = [5, [5, 7, 8], (2, 7, 9), 'Python']
#       -4  -3          -2         -1

print(list4[1])  # [5, 7, 8]
print(list4[1][1])  # 7

list5 = [5, 7, 9, 20]
print("list5 :", list5)  # [5, 7, 9, 20]

# List can allow duplicate members
list6 = [2, 3.5, 'Hello', True, [4, 6], (6, 8, 9), {1, "hi"}, {'a': 123, 'b': 444}, 2, 3.5, 'Hello', True, [4, 6],
         (6, 8, 9), {1, "hi"}, {'a': 123, 'b': 444}]
print(list6)

# Tuple #
"""properties :
 - tuple is immutable data type, cannot changes once it is defined
 - tuple follows positive and negative indexing as like string and list
 - tuple can contains any type of data, int, float, string, list, tuple, dict, set, boolean
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
print("*" * 40)

# Dictionary #
""" Properties :
-> dict is mutable data type, we can modify any point of time.
-> All the keys in the dict should be unique, duplicate keys are not allowed.
-> Only immutable data type can be in dict -> int, float, string, tuple, boolean.
-> All type of data can value in the dict e.g. int, float, string, tuple, boolean, list, set, dict.
"""
dict1 = {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 5: 'hi', 2.2: "hello", True: 'World',
         (1, 2, 3): 45}
print(dict1, type(dict1))
# {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 5: 'hi', 2.2: "hello", True: 'World',
# (1, 2, 3): 45} <class 'dict'>

print(dict1['age'])  # 25
print(dict1['email'])  # 'rahul@gmail.com'
print(dict1[(1, 2, 3)])
dict1['age'] = 30

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

dict2 = {50: 100, 5.5: 55.55, 'Hello': "Good Morning", 'a': [4, 6, 8], (4, 7, 7, 2): ('a', 'b', 'c'), True: False}
print(dict2)

# list as key is not allowed
# dict2[[66, 7, 8]] = [55, 66, 77]
# print(dict2)
# int, float, string, tuple, boolean.

# dictionary as key is not allowed
# dict2[{'a' : 123}] = 7000
# print(dict2)
# TypeError: unhashable type: 'dict'

# set as key is not allowed
# dict2[{5, 7, 8}] = {5, 8, 23, 33}
# print(dict2)
# TypeError: unhashable type: 'set'
print("*" * 50)

# set #
"""properties :
- set only store unique data, duplicate data is not allowed.
- set is mutable data type, we can modify at any point of time.
- All the immutable data type can be member of set, like int, float, string, tuple, boolean
- Mutable data types are not allowed as member in the set, list, dict and set it self.
- Set store the data in random order.
- Set does not follow any indexing.
"""
set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello'}
print(set1)
set1.add(100)
print(set1)

# dictionary is not allowed
# set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello', {'a': 5}}
# unhashable type: 'dict'

# list is not allowed
# set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello', [5]}
# unhashable type: 'list'

# set is not allowed
# set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello', {5}}
# unhashable type: 'set'

# Boolean #
# boolean data type has only two values True and False
var1 = 60
var2 = 70
var3 = 60
print(var1 == var2)  # False
print(var1 == var3)  # True
