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

# Add all possible keys #
dict3 = {}
dict3[1] = "hi"
dict3[3.5] = "world"
dict3['Name'] = 'Ashok'
dict3["Age"] = 20
dict3[True] = 5
dict3[(1, 2, 3)] = [4, 5, 6]
print(dict3)

# The keys() method will return a list of all the keys in the dictionary.
# The values() method will return a list of all the values in the dictionary.
# The items() method will return each item in a dictionary, as tuples in a list.

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict.keys())
print(thisdict.values())

thisdict["color"] = "white"
print(thisdict.keys())
print(thisdict.values())
print(thisdict.items())

for val in thisdict.keys():
    print(val)

for val in thisdict.values():
    print(val)

for val in thisdict.values():
    print(val)

# Dictionary Methods #

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'


