set1 = {4, 4.7, 'Python', (2, 5, 7), True, 4, 'Python'}
print(set1, type(set1))

"""
properties :
- set contains only unique data, duplicate data is not allowed.
- set is mutable data type, we can modify at any point of time
- set only contains immutable data type as member e.g int, float, string, tuple, boolean.
- set store the data in random order, does not follow any sequencing.
"""

for val in set1:
    print(val)

# set2 = {4, 6, 8, 2, [11, 22, 33]}
# print(set2)
# unhashable type: 'list'

############## set methods ##############
print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update',
# 'discard', 'intersection', 'intersection_update', 'isdisjoint',
# 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference',
# 'symmetric_difference_update', 'union', 'update']


########
# add() method : This method add data to the set
set_a = {4, 7, 2, 8}
set_a.add(100)
print("set_a:", set_a)

print("-"*50)
#########
# update() method : This method update the data from set1 to set2
set_b= {5, 7, 8, 9}
set_c = {'a', 'b', 'c'}

set_c.update(set_b)
print("set_c :", set_c) # {5, 7, 'b', 8, 'a', 'c', 9}
print("set_b :", set_b)
# print(set_b[2]) # TypeError: 'set' object is not subscriptable

##########
# union method : this method combine two sets and create new set of values

set_d = {5, 8, 2, 9}
set_e = {11, 12, 13}
output = set_d.union(set_e)
print("output :", output) # {2, 5, 8, 9, 11, 12, 13}

print("_"*50)
######### remove data #####
# pop() method: This method remove any random value from set and return it.

set_f = {'a', 'b', 'c', 'd', 'e'}
val = set_f.pop()
print("removed value :", val) # d
print("updated set :", set_f) # {'b', 'e', 'c', 'a'}

print("_"*50)
#########
# remove method : this method remove specific data from and does not return anything

set_h = {5, 7, 3, 88, 22}
val = set_h.remove(88)
print("removed value :", val)  # None
print("update set :", set_h)   # {3, 5, 22, 7}

# If we try to remove unavailable data from set, it will through the error.
# set_h.remove(99) # KeyError: 99

print("_"*50)
############
# discard method: this method will remove the data from set and does not return it.
set_g = {5, 7, 3, 88, 22}
set_g.discard(22)
print("set_g :", set_g)

# If we try to remove any available data, then it does not through any error.
set_g.discard(100)
print("set_g :", set_g)

#########################
# clear method :  This will clear all the data from set.
set_j = {5, 7, 3, 88, 22}
set_j.clear()
print("set_j :", set_j)
set_g = set()










