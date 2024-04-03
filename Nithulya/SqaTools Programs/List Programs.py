#1). Python program to calculate the square of each number from the given list.
# list1=[2,4,3,4,5,]
# for i in list1:
#     print('Number :',i,'Square value :',i**2)

#2). Python program to combine two lists.
# list1=[2,4,3,4,5]
# list2=['a','b','c','d']
# list3=list1+list2
# print('List3 :',list3)    # List3 : [2, 4, 3, 4, 5, 'a', 'b', 'c', 'd']

#3). Python program to calculate the sum of all elements from a list.
# list1=[2,4,3,4,5,]
# Total=0
# for i in list1:
#     Total += i
# print('Total :',Total)       # Total : 18

#4). Python program to find a product of all elements from a given list.
# list1=[2,4,3,4,5,]
# product1=1
# for i in list1:
#     product1 *= i
# print('Total :',product1)        # Total : 480

#5). Python program to find the minimum and maximum elements from the list.
# list1=[2,4,3,4,5]
# list1.sort()
# print(list1)              # [2, 3, 4, 4, 5]
# print('Minimum Number :',list1[0],'Maximum Number :',list1[4])    # Minimum Number : 2 Maximum Number : 5

#6). Python program to differentiate even and odd elements from the given list.
# list1=[2,4,3,8,5]
# listeven=[]
# listodd=[]
# for i in list1:
#     if i%2==0:
#         listeven.append(i)
#     else:
#         listodd.append(i)
# print('Even Number :',listeven)      # Even Number : [2, 4, 8]
# print('Odd Number :', listodd)       # Odd Number : [3, 5]

#7). Python program to remove all duplicate elements from the list.
# list1=[2,4,4,3,8,5,8,2,16]
# list2=[]
# for i in list1:
#     if i not in list2:
#         list2.append(i)
# print('List2 :',list2)        # List2 : [2, 4, 3, 8, 5, 16]

#8). Python program to print squares of all even numbers in a list.
# list1=[2,4,6,3,8,5,10]
# list2=[]
# for i in list1:
#     if i%2==0:
#         print('Even Number :',i,'Square of Number :',i**2)

#9). Python program to split the list into two-part, the left side all odd values and the right side all even values.
#Input = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# list1 = [5, 7, 2, 8, 11, 12, 17, 19, 22]
# listeven=[]
# listodd=[]
# for i in list1:
#     if i%2==0:
#         listeven.append(i)
#     else:
#         listodd.append(i)
# print('Even Number :',listeven)      # Even Number : [2, 8, 12, 22]
# print('Odd Number :', listodd)       # Odd Number : [5, 7, 11, 17, 19]
# listodd.extend(listeven)
# print(listodd)                       # [5, 7, 11, 17, 19, 2, 8, 12, 22]

#10).  Python program to get common elements from two lists.
# list1 = [4, 5, 7, 9, 2, 1]
# list2 = [2, 5, 8, 3, 4, 7]
# list3=[]
# for i in list1:
#     if i in list2:
#         list3.append(i)
# print('Common elements from List1 & List2 : ',list3)

#11). Python program to reverse a list with for loop.
# list1=[2,3,1,5,7,11,16]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i], end=" ")

