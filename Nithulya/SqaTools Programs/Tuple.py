#1). Python tuple program to create a tuple with 2 lists of data.
#Input lists: list1 = [4, 6, 8] list2 = [7, 1, 4] , Output= ((4, 7), (6, 1), (8, 4))
# list1 = [4, 6, 8]
# list2 = [7, 1, 4]
# tup1=zip(list1,list2)
# print(tuple(tup1))           # ((4, 7), (6, 1), (8, 4))


#2). Python tuple program to find the maximum value from a tuple.Input = (41, 15, 69, 55),Output = 69
# tup1=(41, 15, 69, 55)
# print('Maximum Value:',max(tup1))         # Maximum Value: 69

#3). Python tuple program to find the minimum value from a tuple.Input = (36,5,79,25),Output = 5
# tup1=(36,5,79,25)
# print('Minimum Value:',min(tup1))          # Minimum Value: 5

#4). Python tuple program to create a list of tuples from a list having a number and its square in each tuple.
#Input = [4,6,3,8],Output = [ (4, 16), (6, 36), (3, 27), (8, 64) ]
# list1=[4,6,3,8]
# list2=[]
# for i in list1:
#     list2.append(i**2)
# print(list(zip(list1,list2)))        # [(4, 16), (6, 36), (3, 9), (8, 64)]

#5). Python tuple program to create a tuple with different datatypes.
# Output= ( 2.6, 1, ‘Python’, True, [5, 6, 7], (5, 1, 4), {‘a’: 123, ‘b’: 456})
# tup1=( 2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})
# print('Tuple:',tup1)      # Tuple: (2.6, 1, 'Python', True, [5, 6, 7], (5, 1, 4), {'a': 123, 'b': 456})

#6). Python tuple program to create a tuple and find an element from it by its index no.,Input = (4, 8, 9, 1)
#Index = 2,Output = 9
# tup1=(4, 8, 9, 1)
# print(tup1[2])            # 9

#7). Python tuple program to assign values of tuples to several variables and print them.
#Input = (6,7,3),Variables = a,b,c,
# Output:
# a, 6
# b, 7
# c, 3
# tup1= (6,7,3)
# (a,b,c)=tup1
# print('a,',a)
# print('b,',b)
# print('c,',c)

#8). Python tuple program to add an item to a tuple.Input= ( 18, 65, 3, 45),Output=(18, 65, 3, 45, 15)
# tup1=( 18, 65, 3, 45)
# print('Tuple1:',tup1)
# list1=list(tup1)
# list1.append(15)
# print('Result:',tuple(list1))         # Result: (18, 65, 3, 45, 15)

#9). Python tuple program to convert a tuple into a string.Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’, ‘l’, ‘s’)
#Output = Sqatools
# tup1=('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
# word=''
# for i in tup1:
#     word+=i
# print('Result:',word)             # Result: sqatools

#10). Python tuple program to get the 2nd element from the front and the 3rd element from the back of the tuple.
#Input = (‘s’, ‘q’, ‘a’, ‘t’, ‘o’, ‘o’ ,’l’, ‘s’),Output=q,o
# tup1=('s','q','a','t','o','o','l','s')
# print(tup1[1])       # q
# print(tup1[-3])      # o

#11). Python tuple program to check whether an element exists in a tuple or not.Input = ( ‘p’ ,’y’, ‘t’, ‘h’, ‘o’, ‘n’)
#P in A,Output=True
# tup1=('p','y','t','h','o','n')
# if 'p' in tup1:
#     print(True)             # True
# else:
#     print(False)


#12). Python tuple program to add a list in the tuple.Input:L=[12,67],A=(6,8,4),Output:A=(6,8,4,12,67)
# list1=[12,67]
# tup1=(6,8,4)
# total=tuple(list(tup1)+list1)
# print('Total:',total)             # Total: (6, 8, 4, 12, 67)

#13). Python tuple program to find sum of elements in a tuple.Input:A=(4,6,2),Output:12
# tup1=(4,6,2)
# print('Sum:',sum(tup1))          # Sum: 12


#14)....... Python tuple program to add row-wise elements in Tuple Matrix.Input:A = [[(‘sqa’, 4)], [(‘tools’, 8)]],B = (3,6)
#Output:[[(‘sqa’, 4,3)], [(‘tools’, 8,6)]]
A=[[('sqa', 4)], [('tools', 8)]]
B= (3, 6)
c=[]
d=()

items=[()]
i=0
while(i<len(A)):
    d=A[i].__getitem__(0)
    print(d)
    c.append(d.__add__(B[i]))
    i=i+1

print(c)


#15). Python tuple program to create a tuple having squares of the elements from the list.
#Input = [(1,5,7), (3,6)],Output = (1, 25, 49, 9, 36)
# list1=[(1,5,7), (3,6)]
# list2=[]
# for i in list1:
#     for j in i:
#         list2.append(j**2)
# print('Result:',tuple(list2))             # Result: (1, 25, 49, 9, 36)


#16). Python tuple program to convert a list into a tuple and multiply each element by 2.
#Input = [12,65,34,77],Output = (24, 130, 68, 154)
# list1=[12,65,34,77]
# list2=[]
# for i in list1:
#     list2.append((i*2))
# print('Result:',tuple(list2))           # Result: (24, 130, 68, 154)


#17). Python tuple program to remove an item from a tuple.Input:A=(p,y,t,h,o,n),Output: (p,y,t,o,n)
# tup1=('p','y','t','h','o','n')
# list1=list(tup1)
# list1.remove('h')
# print('Result:',tuple(list1))            # Result: ('p', 'y', 't', 'o', 'n')


#18). Python tuple program to slice a tuple.Input:A=(5,7,3,4,9,0,2),Output:(5,7,3)\n(3,4,9)
# tup1=(5,7,3,4,9,0,2)
# print(tup1[:3])          # (5, 7, 3)
# print(tup1[2:-2])        # (3, 4, 9)

#19). Python tuple program to find an index of an element in a tuple.Input:A=(s,q,a,t,o,o,l,s),Index of a?,Output = 2
# tup1=('s','q','a','t','o','o','l','s')
# print("Index of 'a':",tup1.index('a'))      # Index of 'a': 2

#20). Python tuple program to find the length of a tuple.Input:A=(v,i,r,a,t),Output=5
# tup1=('v','i','r','a','t')
# print('Length of tuple:',len(tup1))           # Length of tuple: 5

#21). Python tuple program to convert a tuple into a dictionary.Input:A=((5,s),(6,l)),Output ={5: 's', 6: 'l'}
# tup1=((5,'s'),(6,'l'))
# dict1=dict(tup1)
# print(dict1)           # {5: 's', 6: 'l'}

#22). Python tuple program to reverse a tuple.Input = ( 4, 6, 8, 3, 1),Output= (1, 3, 8, 6, 4)
# tup1=( 4, 6, 8, 3, 1)
# tup2=reversed(tup1)
# list1=[]
# for i in tup2:
#     list1.append(i)
# print(tuple(list1))         # (1, 3, 8, 6, 4)


#23). Python tuple program to convert a list of tuples in a dictionary.Input=[(s,2),(q,1),(a,1),(s,3),(q,2),(a,4)]
#Output ={ s: [ 2, 3 ], q: [ 1, 2 ], a: [ 1 ,4 ] }
# list1=[('s',2),('q',1),('a',1),('s',3),('q',2),('a',4)]
# dict1={}
# for key,value in list1:
#     dict1.setdefault(key,[]).append(value)
# print(dict1)                # {'s': [2, 3], 'q': [1, 2], 'a': [1, 4]}

