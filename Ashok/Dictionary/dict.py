""" Properties:
-> dict store the data in form of key value pair
-> dict is mutable data type, we can modify any point of time.
-> All the keys in the dict should be unique, duplicate keys are not allowed.
-> Only immutable data type can be in dict -> int, float, string, tuple, boolean.
-> All type of data can value in the dict e.g. int, float, string, tuple, boolean, list, set, dict.
"""

dict1 = {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 5: 'hi', 2.2: "hello", True: 'World',
         (1, 2, 3): 45}
print(dict1, type(dict1))
# modifying the data in dict using key.
dict1['age'] = 30
print(dict1)

# duplicate keys are not allowed, if user set the duplicate keys then will overwrite the latest value.
dict2 = {'Name': 'Rahul', 'age': 25, 'email': 'rahul@gmail.com', 'Name': 'Ashok', 'age': 40}
print(dict2)

# Adding all possible keys #
dict3 = {}
dict3[1] = "hi"
dict3[3.5] = "world"
dict3['Name'] = 'Ashok'
dict3["Age"] = 20
dict3[True] = 5
dict3[(1, 2, 3)] = [4, 5, 6]
print(dict3)

# Dictionary Methods #

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

# get() method : This method return the values on the basis of key provided.
dict1 = {'a': 123, 'b': 345, 'c': 789}
print(dict1.get('b'))
# There will be difference between normal and get method, Using get method if there is no value for key then it will
# not display any error.
print(dict1['b'])  # Normal way of calling the key.
print(dict1.get('c'))

# update method: This method updates the data from dict1 to dict2.
dict2 = {"Name": 'Rahul', 'Age': 30, 'Address': 'Mumbai'}
dict2['Country'] = 'India'  # updating single key with value
print(dict2)
dict3 = {'Email': "ashok.pusarla@test.com", 'Phone': '123456789'}
dict2.update(dict3)  # We can add multiple values at a time
print(dict2)

# The keys() method will return a list of all the keys in the dictionary.
# The values() method will return a list of all the values in the dictionary.
# The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())  # dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

thisdict["color"] = "white"
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

# using for loop to above methods:
for val in thisdict.keys():
    print(val, end=' ')
print()

for val in thisdict.values():
    print(val, end=' ')
print()

for k, v in thisdict.items():
    print(k, v)

# items() method : This method provides list of key value combination in tuple
dict_b = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com',
          'phone': 765765756}
print(dict_b.items())
# dict_items([('Name', 'Rahul'), ('Age', 30), ('Address', 'Mumbai'), ('Country', 'India'),
# ('email', 'rahul@gmail.com'), ('phone', 765765756)])

# pop method : This method will remove data from dict with the help of keys.
dict_b = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com',
          'phone': 765765756}
val = dict_b.pop('Name')  # Atleast one key is mandatory in pop
print(val)
print(dict_b)  # {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'phone': 765765756}

# popitem method : This method remove key value combination from the dictionary
dict_c = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com',
          'phone': 765765756}
data = dict_c.popitem()
print(data)  # ('phone', 765765756)
print(dict_c)  # {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com'}

# clear method:
dict_d = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai', 'Country': 'India', 'email': 'rahul@gmail.com',
          'phone': 765765756}
dict_d.clear()
print("dict_d:", dict_d)  # {}

# delete method:
dict_e = {'Name': 'Rahul', 'Age': 30, 'Address': 'Mumbai'}
# del dict_e
# print("dict_e :", dict_e) # name 'dict_e' is not defined

del dict_e['Address']
print("dict_e :", dict_e)  # {'Name': 'Rahul', 'Age': 30}

# copy method:
# shallow copy: when we modify the reference list value, then original list will also be affected.
dict1 = {'a': 345, 'b': 678, 'c': 999}
dict2 = dict1
dict2['d'] = 1000
print("dict1 :", dict1)
print("dict2 :", dict2)

# Deep copy : In deep copy we use copy method or pass the data from list1 to list2, if any modification done on list2,
# it won't affect list1
dictp = {'a': 345, 'b': 678, 'c': 999}
dictq = dictp.copy()
dictq['d'] = 300
print("dictp :", dictp)  # dictp : {'a': 345, 'b': 678, 'c': 999}
print("dictq :", dictq)  # dictq : {'a': 345, 'b': 678, 'c': 999, 'd': 300}

# Sample programs #
# program1:
list1 = ['A', 'B', 'C']
list2 = [22, 33, 44]
list3 = zip(list1, list2)
print(dict(list3))

s = {}
for i in range(len(list1)):
    s[list1[i]] = list2[i]
print("s:", s)

# program2:
str1 = "Python"
# output= {'P': 1, 'y': 2, 't': 3, 'h': 4, 'o': 5, 'n' : 6}
s = {}
for i in range(len(str1)):
    s[str1[i]] = i + 1
print("s:", s)

# program3:
str2 = "ProGraM"
list1 = [1, 2, 3, 4, 5, 6, 7]
# output = {'p': 1, 'rr': 2, 'ooo': 3, 'gggg': 4, 'aaaaaa' : 6, 'mmmmmmm': 7}

output = {}
for i in range(len(str2)):
    output[(str2[i].lower() * list1[i])] = list1[i]
print(output)
