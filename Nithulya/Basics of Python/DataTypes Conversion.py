########## Integer ########

# int -> float
a1 = 5
print("Number : ",a1,type(a1)) # <class 'int'> 5
f1 = float(a1)
print("Number : ",f1,type(f1)) # <class 'float'> 5.0
print("_"*50)

# int -> string
n2 = 65
s2 = str(n2)
print("Number : ",s2,type(s2),s2*3,s2[0])

# int -> list # conversion is not possible

"""print("_"*50)
a3 = 40
l1 = list(a3)
print(l1)"""

# int ->  tuple # conversion is not possible
# int -> dict # conversion is not possible
# int -> set # conversion is not possible


# int -> boolean

n1 = 10
b1 = bool(n1)
print("Number : ",n1,b1) # True

n2 = 0
b2 = bool(n2)
print("Number : ",n2,b2) # False

n3 = -33
b3 = bool(n3)
print("Number : ",n3,b3) # True

########################## Float ################
print("_"*50)

# float -> int
var1 = 11.02
n1 = int(var1)
print("Number : ",var1,type(n1),n1) # 11 <class 'int'>

#### float -> string ###
print("_"*50)
var2 = 11.02
s1 = str(var2)
print("Number : ",var2,type(s1),s1,":", s1*2, ":", s1[1])
# 11.02 <class 'str'> : 11.0211.02 : 1

# float -> list # conversion is not possible
# float -> dict # conversion is not possible
# float -> tuple # conversion is not possible
# float -> set # conversion is not possible
# float -> boolean
print("_"*50)
f1 = 23.89
b1 = bool(f1)
print(b1) # True

f2 = 0.0
b2 = bool(f2)
print(b2) # False

f3 = -23.89
b3 = bool(f3)
print(b3) # True

########### string ############

# string -> int

# if string contains character then conversion is not possible
"""
s1 = "WELCOME"
n1 = int(s1)
# invalid literal for int() with base 10: 'WELCOME'
print(n1)
"""
# if the string contains only number, then str to int conversion is possible
print("_"*50)
s1 = "4576"
n1 = int(s1)
print("Char : ",s1,type(n1),n1,n1*2)
# Char :  4576 <class 'int'> 4576 9152
#### string - float ####

# if string contains character then str to float conversion is not possible
# if string contains only number or pointer values then conversion is possible
print("-"*50)
s3 = "45.789"
f3 = float(s3)
print("Char : ",s3,type(f3),f3,f3*2)
#Char :  45.789 <class 'float'> 45.789 91.

### string ->  list ####
print("_"*50)
str_a = "HELLO"
l1 = list(str_a)
print("String :",str_a,", List : ",l1, type(l1))
#String : HELLO , List :  ['H', 'E', 'L', 'L', 'O'] <class 'list'>

### string -> tuple #####
print("_"*50)
str_b = "Good Morning!"
t1 = tuple(str_b)
print("String :",str_b,", Tuple : ",t1, type(t1))
# String : Good Morning! , Tuple :  ('G', 'o', 'o', 'd', ' ', 'M', 'o', 'r', 'n', 'i', 'n', 'g', '!') <class 'tuple'>

### string -> dict ####
print("_"*50)
"""
# If string contains any plain word, then str to dict conversion is not possible
str_c = "Hello"
d1 = dict(str_c)
print(d1, type(d1))
# dictionary update sequence element #0 has length 1; 2 is required
"""
import json
str_g = '{"Name" : "Keerthi", "Phone" : 772345645, "email" : "keerthi@gmail.com"}'
dict_output = json.loads(str_g)
print(dict_output, type(dict_output))
#{'Name': 'Keerthi', 'Phone': 772345645, 'email': 'keerthi@gmail.com'} <class 'dict'>
print(dict_output['Name'])
# Keerthi

############################ List ######################

### list  -> int #### conversion is not possible
### list -> float ### conversion is not possible

### list -> string ###
l1 = [3,2,1,4,6]
s1 = str(l1)
print("List : ",l1,type(s1),"String : ",s1)  # List :  [3, 2, 1, 4, 6] <class 'str'> String :  [3, 2, 1, 4, 6]
print(s1[0], s1[1], s1[2], s1[-1])  # [ 3 , ]

#### list -> tuple ###
print("_" * 50)
l2 = [2,4,5,6,7]
t2 = tuple(l2)
print('List : ',l2,type(t2), "Tuple : ",t2,':',t2[0])
# List :  [2, 4, 5, 6, 7] <class 'tuple'> Tuple :  (2, 4, 5, 6, 7) : 2


### list -> dict ####
print("_" * 50)
"""
l3 = [5, 8, 2, 6]
d1= dict(l3)
print(d1,type(d1))
 # TypeError: cannot convert dictionary update sequence element #0 to a sequence
"""
lista = ['a','b','c','d','e']
listb = [11,35,28,12,14]
result1 = dict(zip(lista,listb))
print("Result1 :", result1)
# Result : {'a': 11, 'b': 35, 'c': 28, 'd': 12, 'e': 11}

listc= ['A','B','C','D']
listd = [11,35,28,12,13,34,23]
result2 = dict(zip(listc,listd))
print("Result2 :", result2)
# Result2 : {'A': 11, 'B': 35, 'C': 28, 'D': 12}
####### list -> set ##########
print("_" * 50)
list1 = [2,3,1,4,5,4]
s1 = set(list1)
print("List : ",list1,type(s1),"SET : ",s1)
# List :  [2, 3, 1, 4, 5, 4] <class 'set'> SET :  {1, 2, 3, 4, 5}
print("List : ",list(s1))  # [8, 2, 4, 6]

##### list -> Boolean #######
lis1 = [1,3,2,4]
lis2 = bool(lis1)
print("List : ",lis1,type(lis2),lis2)
#List :  [1, 3, 2, 4] <class 'bool'> True
list2 = []
b2 = bool(list2)
print("List : ",list2,type(b2),b2)
#List :  [] <class 'bool'> False

################### Tuple ###################

print("_"*50)
# tuple -> int  # conversion is not possible
# tuple -> float # conversion is not possible
# tuple -> string
tup1 = (2,4,5,6)
str1 = str(tup1)
print("Tuple : ",tup1,type(str1),'String : ',str1,':',str1[0], str1[1])
# Tuple :  (2, 4, 5, 6) <class 'str'> String :  (2, 4, 5, 6) : ( 2

# tuple -> list
tup2= (1,3,2,4,5)
list1 = list(tup2)
print("Tuple : ",tup2,type(list1),'List : ',list1,':',list1[0])
# Tuple :  (1, 3, 2, 4, 5) <class 'list'> List :  [1, 3, 2, 4, 5] : 1

### tuple -> dict ### conversion is not possible

### tuple -> set ###
print("_"*40)
tup3 = (1,3,4,5,2,6,7)
set1 = set(tup3)
print('Tuple : ',tup3,type(set1),'SET : ',set1)
#Tuple :  (1, 3, 4, 5, 2, 6, 7) <class 'set'> SET :  {1, 2, 3, 4, 5, 6, 7}

### tuple -> boolean ####
tup4 = (1,3,6,7)
b1 = bool(tup4)
print("Tuple : ",tup4, type(b1),b1)
# Tuple :  (1, 3, 6, 7) <class 'bool'> True

tup5= ()
b2 = bool(tup5)
print("Tuple : ",tup5, type(b2),b2)
# Tuple :  () <class 'bool'> False

################ Dictionary ###########

# dict -> int : conversion is not possible
# dict -> float : conversion is not possible

### dict -> string ###
dict1 = {'c' : 111, 'd' : 112}
s1 = str(dict1)
print("Dict : ",dict1,type(s1), 'String : ',s1,':', s1[0], s1[-2])
# Dict :  {'c': 111, 'd': 112} <class 'str'> String :  {'c': 111, 'd': 112} : { 2

### dict -> list ###
print("_"*50)
dict2 = {'Name' : 'Keerthi', 'email' : 'keerthi@gmail.com', 'phone' : 1234563}
l1 = list(dict2)
print('Dict:',dict2,type(l1),'List:',l1)
# Dict: {'Name': 'Keerthi', 'email': 'keerthi@gmail.com', 'phone': 1234563} <class 'list'> List: ['Name', 'email', 'phone']

##### dict -> tuple ###
print("_"*50)
dict4 = {'Name' : 'Keerthi', 'email' : 'keerthi@gmail.com', 'phone' : 1234563}
t1 = tuple(dict2)
print('Dict:',dict4,type(t1),'Tuple:',t1)
# Dict: {'Name': 'Keerthi', 'email': 'keerthi@gmail.com', 'phone': 1234563} <class 'tuple'> Tuple: ('Name', 'email', 'phone')

### dict -> set ####
print("_"*50)
dict2 = {'Name' : 'Keerthi', 'email' : 'keerthi@gmail.com', 'phone' : 1234563}
s1 = set(dict2)
print('Dict:',dict2,type(s1),'SET:',s1)
# Dict: {'Name': 'Keerthi', 'email': 'keerthi@gmail.com', 'phone': 1234563} <class 'set'> SET: {'phone', 'email', 'Name'}

#### dict -> boolean ###
print("_"*50)
dict1= {}
b1= bool(dict1)
print('Dict:',dict1,type(b1),b1) # Dict: {} <class 'bool'> False

dict2 = {'a' : 456}
b2 = bool(dict2)
print('Dict:',dict2,type(b2),b2) # Dict: {'a': 456} <class 'bool'> True

######################## Set #############

# set -> int : conversion is not possible
# set -> float : conversion is not possible

### set -> string ####
print("-"*50)
set1 = {1,3,4,5,2}
str1 = str(set1)
print("SET:",set1,type(str1),'String:',str1,':',str1[0], str1[1])
# SET: {1, 2, 3, 4, 5} <class 'str'> String: {1, 2, 3, 4, 5} : { 1

### set1 -> list ####
seta = {1,3,2,5,6,9}
lista = list(seta)
print("SET:",seta,type(lista),'List:',lista,':',lista[0], lista[1])
# SET: {1, 2, 3, 5, 6, 9} <class 'list'> List: [1, 2, 3, 5, 6, 9] : 1 2

#### set -> tuple ####
setb = {112,113,213,134,312,500}
tup1 = tuple(setb)
print("SET:",setb,type(tup1),'Tuple:',tup1,':',tup1[0], tup1[1])
# SET: {112, 113, 500, 213, 134, 312} <class 'tuple'> Tuple: (112, 113, 500, 213, 134, 312) : 112 113

#### set -> dictionary ### conversion is not possible
#### set -> boolean ####

set1 = {1,2,3}
b1 = bool(set1)
print('SET:',set1,type(b1),b1)
# SET: {1, 2, 3} <class 'bool'> True

set2 = set()
b2 = bool(set2)
print('SET:',set2,type(b2),b2)
# SET: set() <class 'bool'> False