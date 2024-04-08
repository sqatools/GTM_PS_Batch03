# 1) tuple program to create a tuple with 2 lists of data.
ls1 = [34, 45, 67, 23]
ls2 = [45, 23, 89, 14]
result = zip(ls1,ls2)
print(tuple(result)) # ((34, 45), (45, 23), (67, 89), (23, 14))
# 2)Python tuple program to find the maximum value from a tuple
ls1 = [34, 45, 67, 23]
print("Max value :",max(ls1))
print("Min value :",min(ls1))
# 4)tuple program to create a list of tuples from a list having a number and its square in each tuple.
Input = [4, 6, 3, 8]
Output = [(4, 16), (6, 36), (3, 27), (8, 64) ]
lis1 = [4,6,3,8]
result = [(val,val**2) for val in lis1]
print(list(result))
print("#"*50)

# 5). Python tuple program to create a tuple with different datatypes.
tup = (2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
print("Tuple :", tup)
print("#"*50)

# 6). Python tuple program to create a tuple and find an element from it by its index no.

tup2 = (5,67,90,32)
print(tup2[2])#90

# 7). Python tuple program to assign values of tuples to several variables and print them.

tup4 = (45,67,89,23)
(a, b, c, d) = tup4
print(a, b, c, d)
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)

# 8). Python tuple program to add an item to a tuple.

tup2 = (18, 65, 3, 45)
ls = list(tup2)
ls.append(15)
print(tup2) # (18, 65, 3, 45)
print(tuple(ls)) # (18, 65, 3, 45, 15)
print("#"*50)
# 9). Python tuple program to convert a tuple into a string.
tup5 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
str1 = ""
for char in tup5:
    print(str1+char,end="")
print()
# 10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
tu = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
print("2nd element from the front:", tu[1])
print("3rd element from the back:", tu[-3])