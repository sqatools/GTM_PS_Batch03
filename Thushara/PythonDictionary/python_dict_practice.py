dict1 = {'a' : 3456, 'b' : 167}
print(dict1) # {'a': 3456, 'b': 167}
# creating dictionary
dict2 = {}
dict2[1] = 'hello'
dict2[4] = 'good'
dict2[8] = 'morning'
dict2[6] =(3, 4, 8)
print(dict2) #{1: 'hello', 4: 'good', 8: 'morning', 6: (3, 4, 8)}
dict3 = {}
dict3[1,3,4] = ['e', 'r', 'f']
print(dict3) # {(1, 3, 4): ['e', 'r', 'f']}


dict4 = {5: 500, 4.5: 'Hello', 'Python': 'Programming', (3, 5, 7): [4, 6, 8, 22, 33], True: (82, 33, 44)}
for val in dict4:
    print(val)
"""
5
4.5
Python
(3, 5, 7)
True

"""
for val in dict4.items():
    print(val)
"""
(5, 500)
(4.5, 'Hello')
('Python', 'Programming')
((3, 5, 7), [4, 6, 8, 22, 33])
(True, (82, 33, 44))
"""
for k, v in dict4.items():
    print("key :", k )
    print("Value :", v)
"""
key : 5
Value : 500
key : 4.5
Value : Hello
key : Python
Value : Programming
key : (3, 5, 7)
Value : [4, 6, 8, 22, 33]
key : True
Value : (82, 33, 44)
"""

# Dictionary methods
print(dir(dict))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
# get()

print(dict4.get('Python'))
print(dict2)
print(dict4)
dict2=dict2.update(dict4)
print(dict2)

print(dict4.values())
print(dict4.keys())
print(dict4.items())
print(dict4)
dict4.pop(5)
print(dict4)
print(dict1)
dict1.clear()
print(dict1)
print(dict3)
dict1['t'] = 67
print(dict1)
dict_a = dict1
dict_a[67] = 90
print(dict1)
dict_b = dict1.copy()
dict_b['thu'] = 'Ammi'
print(dict1)
print(dict_b)