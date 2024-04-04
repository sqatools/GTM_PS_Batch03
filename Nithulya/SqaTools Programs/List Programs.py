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
# print('Common elements from List1 & List2 : ',list3)     # Common elements from List1 & List2 :  [4, 5, 7, 2]

#11). Python program to reverse a list with for loop.
# list1=[2,3,1,5,7,11,16]
# for i in range(len(list1)-1,-1,-1):
#     print(list1[i], end=" ")            # 16 11 7 5 1 3 2

#12). Python program to reverse a list with a while loop.
# list1=[1,2,3,4,5,6]
# reverse_value = len(list1)-1
# while reverse_value>=0:
#     print(list1[reverse_value],end=' ')        # 6 5 4 3 2 1
#     reverse_value -= 1

#13). Python program to reverse a list using index slicing.
# list1=[1,2,3,4,5,6]
# print(list1[::-1])       # [6, 5, 4, 3, 2, 1]

#14). Python program to reverse a list with reversed and reverse methods.
#1
# list1=[1,2,3,4,5,6]
# list1.reverse()
# print('Reverse Method List1:',list1)       # Reverse Method List1: [6, 5, 4, 3, 2, 1]

#2.
# list1=[1,2,3,4,5,6]
# print('Reversed Method List1:',list(reversed(list1)))   # Reversed Method List1: [6, 5, 4, 3, 2, 1]


#15. Python program to copy or clone one list to another list.
# list1 = [1, 2, 3, 4, 5, 6]
# list2=[]
# for i in list1:
#     list2.append(i)
# print('List2:',list2)           # List2: [1, 2, 3, 4, 5, 6]


#16). Python program to return True if two lists have any common member.
# list1=[1,2,3,4,5]
# list2=[2,7,8]
# for i in list1:
#     if i in list2:
#         print('True')         # True


#17). Python program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
# list1=[1,2,3,4,5,6,7]
# list1.remove(1)
# list1.remove(3)
# list1.remove(6)
# print('New list1:',list1)         # New list1: [2, 4, 5, 7]


#18). Python program to remove negative values from the list.
# list1=[1,-11,2,3,-7,4,-5,-6]
# for i in list1:
#     if i >=0:
#         print(i,end=' ')         # 1 2 3 4


#19). Python program to get a list of all elements which are divided by 3 and 7.
# list1=[3,7,15,10,24,12,21,25,27]
# list2=[]
# for i in list1:
#     if i%3== 0 or i%7==0:
#         list2.append(i)
# print('List2: ',list2)            # List2:  [3, 7, 15, 24, 12, 21, 27]


#20). Python program to check whether the given list is palindrome or not. (should be equal from both sides).
# list1=[1,2,3,3,2,1]
# list2=list1[::-1]
# if list1==list2:
#     print('List is palindrome')          # List is palindrome
# else:
#     print('List is not palindrome')

#22). Python Program to get a list of words which has vowels in the given string.
#Input: “www Student ppp are qqqq learning Python vvv”
#Output : [‘Student’, ‘are’, ‘learning’, ‘Python’]
str1= 'www Student ppp are qqqq learning Python vvv'
str1=str1.split()
str2=[]
for i in str1:
    for j in i:
        if ((j == 'a' or j == 'A') or (j == 'e' or j == 'E') or (j == 'i' or j == 'I') or (j == 'o' or j == 'O')):
            str2.append(i)
            break
print(str2)                            # ['Student', 'are', 'learning', 'Python']