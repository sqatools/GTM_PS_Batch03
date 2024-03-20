# Python Data Types
"""
1. Numbers
    i). Integer
    ii). Float
    iii). Complex Number

2. Sequential data type
    i). String
    ii). List
    iii). Tuple

3. Dictionary
4. Set
5. Boolean
"""


## Integer
x = 20
y = 10
z=x+y
print(z, type(x))
print('-'*50)

## Float
x = 20.0
y = 10.0
z=x+y
print(z, type(x))
print('-'*50)

## Complex
x = 20+10j
y= 10+5j
z=x+y
print("Value : ",z, type(z))
print('-'*50)

##String
str1 = "WELCOME"
print(str1[2],type(str1))   # +ve indexing
print(str1[-2],type(str1))  # -ve indexing
print('-'*50)

##List
list1 = [1,2,3,4,'Hello',[3,4]]
print("List1 ",list1,type(list1))
list1.append(100)
print("List1 ",list1)
list1[1]=400
print("List1 ",list1)
print("List1 string  : ",list1[4])
print("List1 string first letter : ",list1[4][0])
print('-'*50)

#Tuple
tup1 = (1,3,4,5,3)
print(tup1,type(tup1))
print('-'*50)

#Dictionary
dict = {'a':2,'b':3,'c':3}
dict['d'] = 7
print(dict,type(dict))
print('-'*50)

#SET
set1 = {3, 55.55, 'Hello', (5, 7, 8), True, False, 3, 'Hello'}
print(set1)
set1.add(100)
print(set1,type(set1))

print('-'*50)

#Boolean
var1 = 30
var2 = 70
var3 = 30
print(var1 == var2) # False
print(var1 == var3) # True

"""
1). Properties of Integer :
 - Integer is immutable data type, once it is defined we can not change it.
 - There is no as such limit for integer data type. any long number we can defined as integer.

2). Properties of Float :
 - Float is immutable data type, once it is defined we can not change it.
 - There is no as such limit for float data type. any long number we can defined as float.
 
3). Properties of Complex :
 - complex number is the combination of real and imaginary number that's represent with x+yj
 - complex is the immutable data type, once it is defined we can not change it.
 - There is no as such limit for complex data type. any long number we can defined as complex values.
 
4). Properties of String :
- String is immutable data type, can not change it once it is defined
- String follow positive and negative indexing to represent the data.
- String can be defined with single quote, double quote, triple quote as well.

5). Properties of List :
- List is mutable data type
- List follows positive and negative indexing as like string
- List can contain any type of data, int, float, string, list, dict, tuple, set, boolean

6). properties of Tuple :
 - tuple is immutable data type, can not changes once it is defined
 - tuple follows positive and negative indexing as like string and list
 - tuple can contains any type of data, int, float, string, list, tuple, dict, set, boolean
 
7). Properties of Dictionary :
-> dict is mutable data type, we can modify any point of time.
-> All the keys in the dict should be unique, duplicate keys are not allowed.
-> Only immutable data type can be in dict, int, float, string, tuple, boolean.
-> All type of data can value in the dict e.g. int, float, string, tuple, boolean, list, set, dict.

8). Properties of SET :
- set only store unique data, duplicate data is not allowed.
- set is mutable data type, we can modify at any point of time.
- All the immutable data type can be member of set, like int, float, string, tuple, boolean
- Mutable data types are not allowed as member in the set, list, dict and set it self.
- Set store the data in random order.
- Set does not follow any indexing.

9). Properties of Boolean :
- boolean data type has only two values True and False
- boolean is immutable data type, can not changes once it is defined
"""

