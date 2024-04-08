# 11). Python tuple program to check whether an element exists in a tuple or not.
tup1 = (34, 56, 78, 34, 89)
print(34 in tup1) # True
print(100 in tup1)  # False
tup2 = ('p', 'y', 't', 'h', 'o', 'n')
print('p' in tup2) # True

# 12). Python tuple program to add a list in the tuple.
l = [56, 78, 89]
t = (45, 12, 90)
# l.append(list(t))
# print(tuple(l)) # (56, 78, 89, [45, 12, 90])
'''
l1 = list(t)
for val in l1:
    l.append(val)
print(tuple(l)) # (56, 78, 89, 45, 12, 90)
'''
print(tuple(list(t)+l)) # (45, 12, 90, 56, 78, 89)

# 13). Python tuple program to find sum of elements in a tuple.

tup3 = [34, 56, 89]
print("Sum :", sum(tup3)) # Sum : 179

# 14). Python tuple program to add row-wise elements in Tuple Matrix

# A = [[(‘sqa’, 4)], [(‘tools’, 8)]]
# B = (3,6)
# Output:[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]

# 15). Python tuple program to create a tuple having squares of the elements from the list.
# Input = [(1,5,7), (3,6)]
# Output = (1, 81, 25, 49, 36)

# 16). Python tuple program to multiply adjacent elements of a tuple.
# Input = (1,2,3,4)
# Output =  (2,6,12)
tup_p = (1, 2, 3, 4)
list1 = list(tup_p)
list2= []

for i in range(len(list1)-1):
     p = list1[i]*list1[i+1]
     list2.append(p)
print(tuple(list2)) # (2, 6, 12)

# 17). Python tuple program to join tuples if the initial elements of the sub-tuple are the same.
t1 = [(3,6,7),(7,8,4),(7,3),(3,0,5)]
#Output:[(3,6,7,0,5),(7,8,4,3)]

# 18). Python tuple program to convert a list into a tuple and multiply each element by 2.
l2 = [12,65,34,77]
print(l2) # [12, 65, 34, 77]
for i in range(len(l2)):
    l2[i] = l2[i]*2
print(tuple(l2)) # (24, 130, 68, 154)

# 19). Python tuple program to remove an item from a tuple.
t9 =('p', 'y', 't', 'h', 'o', 'n')
print(t9) # ('p', 'y', 't', 'h', 'o', 'n')
l9 = list(t9)
l9.pop(3)
print(tuple(l9)) # ('p', 'y', 't', 'o', 'n')

# 20). Python tuple program to slice a tuple.
tup5 =(5,7,3,4,9,0,2)
print(tup5[::-1]) # (2, 0, 9, 4, 3, 7, 5)
print(tup5[::2]) # (5, 3, 9, 2)
print(tup5[2::]) # (3, 4, 9, 0, 2)
print(tup5[:3]) # (5, 7, 3)
print(tup5[2:5]) #(3, 4, 9)



