"""
properties :
- set contains only unique data, duplicate data is not allowed.
- set is mutable data type, we can modify at any point of time
- set only contains immutable data type as member e.g int, float, string, tuple, boolean.
- set store the data in random order, does not follow any sequencing.
"""
#1.
# set1 = {5,5.6, 'Python', (5,6,7), True,5, 'Python','Hello'}
# print('Set1:',set1, type(set1))        # Set1: {(5, 6, 7), True, 5.6, 5, 'Hello', 'Python'} <class 'set'>
# for element1 in set1:
#     print(element1,end=', ')           # (5, 6, 7), True, 5.6, 5, Hello, Python,

#2.
# set1={2,3,4,1,[1,2,3,4],2}
# print(set1)                       # TypeError: unhashable type: 'list'

#3
# set1={1,2,3,4}
# print(set1[0])               # TypeError: 'set' object is not subscriptable


############## set methods ##############################################################
#print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']

####1. add() method : This method add data to the set
# set1 = {1,2,3,4,'Hello'}
# set1.add(50)
# print("set1:", set1)           # set1: {1, 2, 3, 4, 50, 'Hello'}
# set1.add('Hi')
# print("set1:", set1)           # set1: {1, 2, 3, 4, 50, 'Hi', 'Hello'}
# set1.add((1,2,3))
# print("set1:", set1)           # set1: {1, 2, 3, 4, 50, 'Hi', (1, 2, 3), 'Hello'}


####2. update() method : This method update the data from set1 to set2
# set1= {1,2,3,4}
# set2= {'a', 'b', 'c'}
# set1.update(set2)
# print("set1 :", set1)          # set1 : {1, 2, 3, 4, 'c', 'a', 'b'}
# print("set2 :", set2)          # set2 : {'a', 'c', 'b'}


####3. union method : this method combine two sets and create new set of values
# set1 = {1,2,3,4}
# set2 = {11, 12, 13,14}
# result = set1.union(set2)
# print("Result:", result)         # Result: {1, 2, 3, 4, 11, 12, 13, 14}


####4.  pop() method: This method remove any random value from set and return it.
#1.
# set1 = {'a', 'b', 'c', 'd', 'e'}
# val = set1.pop()
# print("Removed value :", val)            # Removed value : a
# print("Updated set :", set1)             # Updated set : {'e', 'c', 'd', 'b'}

#2.
# set1 = {'a', 'b', 'c', 'd', 'e'}
# val2 = set1.pop('a')
# print('Set1:',set1)                     # TypeError: set.pop() takes no arguments (1 given)


####5.  remove method : this method remove specific data from and does not return anything
# set1= {1,2,3,4,5,'hello'}
# val = set1.remove('hello')
# print("Removed value :", val)              # Removed value : None
# print("Update set :", set1)                # Update set : {1, 2, 3, 4, 5}
# If we try to remove unavailable data from set, it will through the error.
# set_h.remove(99) # KeyError: 99


####6. discard method: this method will remove the data from set and does not return it.
#1.
# set1 = {1,2,3,4,5}
# set2 = set1.discard(5)
# print("set1 :", set1)         # set1 : {1, 2, 3, 4}
# print('set2:',set2)           # set2: None

#2 If we try to remove any available data, then it does not through any error.
# set1 = {1,2,3,4,5}
# set1.discard(6)
# print("set1 :", set1)          # set1 : {1, 2, 3, 4, 5}


####7. clear method :  This will clear all the data from set.
set1 = {11,22,33,44,(1,2,3)}
set1.clear()
print("set1 :", set1)            # set1 : set()






