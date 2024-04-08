"""
Properties:
-  dict store the data in form of key value pair
-  dict is mutable data type, we can modify at any point of time
-  dict only store unique keys, duplicate keys are not allowed.
-  Only immutable data type can be key in the dict, int, float, string, tuple, boolean
-  All type of data can be value in the dict.
"""
# dict1 = {'a' : 5, 'b' : 32}
# print(dict1, type(dict1))       # {'a': 5, 'b': 32} <class 'dict'>
# dict1['n'] = 36
# print(dict1)                    # {'a': 5, 'b': 32, 'n': 36}

### Duplicate keys are not allowed, if user set the duplicate keys then will overwrite the previous value.
# dict1={'a':5,'b':32,'c':36,'b':33}
# print("Dict1 :", dict1)            # Dict1 : {'a': 5, 'b': 33, 'c': 36}


####### Add all possible keys ##########
# dict1 = {}
# dict1['a']=5
# dict1['b']=32
# dict1['n']=36
# dict1['h']='Welcome'
# dict1['Hi']=6
# dict1[(1,2,3)]  = [4,5,6]
# dict1[True] = (2,4,6)
# print(dict1)           # {'a': 5, 'b': 32, 'n': 36, 'h': 'Welcome', 'Hi': 6, (1, 2, 3): [4, 5, 6], True: (2, 4, 6)}

# dict1[[1,2,3]] = 111
# print(dict1)              # TypeError: unhashable type: 'list'

#### Get any value with the help of keys :
# dict1={'a': 5, 'b': 32, 'n': 36, 'h': 'Welcome', 'Hi': 6, (1, 2, 3): [4, 5, 6], True: (2, 4, 6)}
# print(dict1[True])         # (2, 4, 6)

# dict1={'a': 5, 'b': 32, 'n': 36, 'h': 'Welcome', 'Hi': 6, (1, 2, 3): [4, 5, 6], True: (2, 4, 6)}
# for i in dict1.items():
#     print(i,end=' ')   # ('a', 5) ('b', 32) ('n', 36) ('h', 'Welcome') ('Hi', 6) ((1, 2, 3), [4, 5, 6]) (True, (2, 4, 6))

# (OR)
# dict1 = {'a': 5, 'b': 32, 'n': 36, 'h': 'Welcome', 'Hi': 6, (1, 2, 3): [4, 5, 6], True: (2, 4, 6)}
# for i, j in dict1.items():
#     print("Key :", i)
#     print("Value :", j)

############################ Dictionary Methods #########################################

# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'

#1. get() method : This method return the values on the basis of key provided.
# dict1 = {'a' : 1, 'b' : 2, 'c' : 3}
# value1 = dict1.get('c')
# print("Value of c :", value1)           # Value of c : 3
# #(OR)
# print("Value of c :", dict1['c'])       # Value of c : 3


#2. update() method : This method update the data from dict1 to dict2.
# dict2 = {'Name' : 'Nihith', 'Age' : 7, 'Address' : 'Kerala'}
# dict2['Experience'] = '3 years'
# print("dict2:", dict2)
#update
# dict2 = {'Name' : 'Nihith', 'Age' : 7, 'Address' : 'Kerala'}
# dict3 = {'email' : 'riya@gmail.com', 'phone' : 9995612023}
# dict2.update(dict3)
# print("dict2 :", dict2)  # dict2 : {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com', 'phone': 9995612023}


#3. Keys() and value() method:
# keys() and values() method provide the list of keys and list of values from given dict.

# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com', 'phone': 9995612023}
# print(dict1.keys())       # dict_keys(['Name', 'Age', 'Address', 'email', 'phone'])
# print(dict1.values())     # dict_values(['Nihith', 7, 'Kerala', 'riya@gmail.com', 9995612023])

###############
#4. items() method : This method provides list of key value combination in tuple
# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com'}
# print(dict1.items())        # dict_items([('Name', 'Nihith'), ('Age', 7), ('Address', 'Kerala'), ('email', 'riya@gmail.com')])


#5. pop method : This method will remove data from dict with the help of keys.
# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com'}
# value1= dict1.pop('email')
# print(value1)               # riya@gmail.com
# print("dict1:", dict1)      # dict1: {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala'}


#6. popitems method : This method remove key value combination from the dictionary
# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com'}
# value1 = dict1.popitem()
# print(value1)               # ('email', 'riya@gmail.com')
# print("dict1:", dict1)      # dict1: {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala'}


#7. clear method:
# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com'}
# dict1.clear()
# print("dict1:", dict1)        # dict1: {}


#8. del method:
# dict1 = {'Name': 'Nihith', 'Age': 7, 'Address': 'Kerala', 'email': 'riya@gmail.com'}
# del dict1['Address']
# print(dict1)               # {'Name': 'Nihith', 'Age': 7, 'email': 'riya@gmail.com'}


#9. copy method : this method copy data from dict1 to dict2 :
#1. shallow copy
# dict1 =  {'a' : 23, 'b' : 82, 'c' : 12}
# dict2 = dict1
# dict2['d'] = 36
# print("dict1 :", dict1)        # dict1 : {'a': 23, 'b': 82, 'c': 12, 'd': 36}
# print("dict2 :", dict2)        # dict2 : {'a': 23, 'b': 82, 'c': 12, 'd': 36}

#2. Deep copy
# dict1 =  {'a' : 23, 'b' : 82, 'c' : 12}
# dict2 = dict1.copy()
# dict1['d'] = 26
# print("dict1 :", dict1)         # dict1 : {'a': 23, 'b': 82, 'c': 12, 'd': 26}
# print("dict2 :", dict2)         # dict2 : {'a': 23, 'b': 82, 'c': 12}


#10. setdefault() method :The setdefault() method returns the value of the item with the specified key.
# If the key does not exist, insert the key, with the specified value,

#GET vs setdefault():If k isn't a key in the dictionary, get doesn't modify the dictionary,
# but setdefault adds key k with value v to the dictionary.


##############################################################################################

# Program:
#1 Get out put - Result : {'a': 23, 'b': 24, 'c': 44}
# list1=['a','b','c']
# list2=[23,24,44]
# result={}
# for i in range(len(list1)):
#     result[list1[i]]=list2[i]
# print("Result :",result)

#2
# str1='Python'
# dict1={}
# #output={'p':1,'y':2,'t':3,'h':4,'o':5,'n':6}
# for i in range(len(str1)):
#     dict1[str1[i]]=i+1
# print(dict1)

#8
str1='ProGraM'
str2=str1.lower()
dict1={}
for i in range(len(str2)):
    dict1[(str2[i])*(i+1)] =i+1
print(dict1)             # {'p': 1, 'rr': 2, 'ooo': 3, 'gggg': 4, 'rrrrr': 5, 'aaaaaa': 6, 'mmmmmmm': 7}







