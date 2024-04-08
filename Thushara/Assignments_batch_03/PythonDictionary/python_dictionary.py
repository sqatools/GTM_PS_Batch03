"""
Properties:
-> dict store the data in form of key value pair
-  dict is mutable data type, we can modify at any point of time
-  dict only store unique keys, duplicate keys are not allowed.
-  Only immutable data type can be key in the dict, int, float, string, tuple, boolean
-  All type of data can be value in the dict.
"""

dict1 = {'a' : 3456, 'b' : 167}
print(dict1, type(dict1))
# {'a': 3456, 'b': 167} <class 'dict'>

dict1['c'] = 500
print(dict1)  # {'a': 3456, 'b': 167, 'c': 500}

# duplicate keys are not allowed, if user set the duplicate keys then will overwrite the previous value.
dict2 = {'a' : 111, 'b': 222, 'c' : 333, 'a' : 666}
print("dict2 :", dict2) # {'a': 666, 'b': 222, 'c': 333}


####### add all possible keys ##########

dict3 = {}
dict3[5] = 500
dict3[4.5] = "Hello"
dict3['Python'] = "Programming"
dict3[(3, 5, 7)]  = [4, 6, 8, 22, 33]
dict3[True] = (82, 33, 44)

print(dict3)
# {5: 500, 4.5: 'Hello', 'Python': 'Programming', (3, 5, 7): [4, 6, 8, 22, 33], True: (82, 33, 44)}

#dict3[[5, 6, 8]] = 654654
#print(dict3)
# TypeError: unhashable type: 'list'

# Get any value with the help of keys.
print(dict3['Python'])  #Programming



print("_"*50)
dict4 = {5: 500, 4.5: 'Hello', 'Python': 'Programming', (3, 5, 7): [4, 6, 8, 22, 33], True: (82, 33, 44)}

for val in dict4.items():
    print(val)

print("_"*50)
for k1, v1 in dict4.items():
    print("key :", k1)
    print("value :", v1)
    print("_"*5)

################################## Dictionary Methods #################

print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
