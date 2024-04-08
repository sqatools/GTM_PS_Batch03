# tup1 = (6, 3, 'Happy',8, {'a': 123, 'b' : 456}, 111,[1,3,4],234, (3, 6, 7))
# print(tup1[2])          # Happy
# print(tup1[4]['b'])     # 456

######### Slicing in tuple :
# tup1 = (6, 3, 'Happy',8, {'a': 123, 'b' : 456}, 111,[1,3,4],234, (3, 6, 7))
# print(tup1[1:5])        # (3, 'Happy', 8, {'a': 123, 'b': 456})
# print(tup1[-4:])        # (111, [1, 3, 4], 234, (3, 6, 7))
# print(tup1[-1:-4:-1])   # ((3, 6, 7), 234, [1, 3, 4])
# print(tup1[::2])        # (6, 'Happy', {'a': 123, 'b': 456}, [1, 3, 4], (3, 6, 7))
# print(tup1[1::2])       # (3, 8, 111, 234)
# print(tup1[::-1])       # ((3, 6, 7), 234, [1, 3, 4], 111, {'a': 123, 'b': 456}, 8, 'Happy', 3, 6)


#1. Apply loop on the tuple
# tup3 = (5,[2,1,3], 112, 12, 343, 535)
# for i in tup3:
#     print(i,end=' ')           # 5 [2, 1, 3] 112 12 343 535

#(OR)
# tup4=list(i for i in tup3)
# print(tup4)                     # [5, [2, 1, 3], 112, 12, 343, 535]

#(OR)
# for i in range(len(tup3)):
#     print(tup3[i],end=' ')        # 5 [2, 1, 3] 112 12 343 535


############## Tuple Methods #####

# print(dir(tuple))
# 'count', 'index'
#### Count :
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# print(tup1.count(12))             # 3

#### Index :
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# print(tup1.index(12))             # 3
# print(tup1.index(66))             # 1

#### Delete tup variable
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# del tup1
# print(tup1)             # name 'tup1' is not defined.

#### Sorted function :
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# sorted1 = tuple(sorted(tup1))
# print("Sorted1 :", sorted1)         # Sorted1 : (5, 12, 12, 12, 17, 18, 28, 66)

#### Reversed function :
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# reversed1= reversed(tup1)
# for i in reversed1:
#     print(i,end=' ')               # 12 18 17 12 12 28 66 5
#(OR)
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# reversed1= reversed(tup1)
# tup2=tuple(i for i in reversed1)
# print(tup2)                          # (12, 18, 17, 12, 12, 28, 66, 5)


#### Get Max, Min and Sum from tuple values :
# tup1 = (5, 66, 28, 12, 12, 17, 18, 12)
# print("Max value:", max(tup1))      # Max value: 66
# print("Min value:", min(tup1))      # Min value: 5
# print("Sum of values:", sum(tup1))  # Sum of values: 170


tup1 = ('a','b','c')
print(tup1*3)         # ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

list1 = [1, 2, 3]
print(list1*3)        # [1, 2, 3, 1, 2, 3, 1, 2, 3]






