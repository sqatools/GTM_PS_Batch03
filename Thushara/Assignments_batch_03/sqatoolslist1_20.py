#1)program to calculate the square of each number from the given list.
list1 =[2,3,6,8]
for ele in list1:
    print(ele,":",ele**2)
print("#"*50)
#2)Python program to combine two lists.
list1 = [3 , 5, 6, 8]
list2 =[ 34,56,78]
result = list1 +list2
print(result)#[3, 5, 6, 8, 34, 56, 78]

list1.extend(list2)
print(list1)#[3, 5, 6, 8, 34, 56, 78]

#3)program to calculate the sum of all elements from a list.

list1 = [2,5,9,6]
total =0
for num in list1:
    total+= num
print("Sum :",total)#Sum : 22
#while loop

list1 =[2,5,9,6]
total = 0
count =0
while count<len(list1):
    total +=list1[count]
    count+=1
print("Sum :",total)#Sum : 22
#sum()

print("Sum :",sum(list1))
#4)program to find a product of all elements from a given list

list1 =[4,6,7,8]
pdt=1
for ele in list1:
    pdt*=ele
print("The product of all the elements :",pdt) #The product of all the elements : 1344

#while loop
list1 =[4,6,7,8]
pdt=1
count=0
while count<len(list1):
    pdt*=list1[count]
    count+=1
print("The product of all the elements :",pdt)#The product of all the elements : 1344

#5)program to find the minimum and maximum elements from the list.

list1 =[34,76,45,12,56]
list1.sort()
print(list1)
print("Max value :",list1[-1])#Max value : 76
print("Min value :",list1[0])#Min value : 12

#6)program to differentiate even and odd elements from the given list
lst1 = [23,54,76,38,24,22,12,33]
lst_even =[]
lst_odd= []
for val in lst1:
    if val%2==0:
        lst_even.append(val)
    else:
        lst_odd.append(val)

print("List of even numbers :",lst_even)#List of even numbers : [54, 76, 38, 24, 22, 12]
print("List of odd numbers :",lst_odd)# List of odd numbers : [23,33]

#7)program to remove all duplicate elements from the list.

lst_a = [ 3,4,5,4,3,2,5,7]
lst_b =[]
for val in lst_a:
    if val not in lst_b:
        lst_b.append(val)
print("List without duplicates :", lst_b)#List without duplicates : [3, 4, 5, 2, 7]

#8)program to print a combination of 2 elements from the list whose sum is 10.
list1=[3,7,6,4,5,5,8,2,12]
list2=[3,7,6,4,5,5,8,2,12]
sum = 10
for i in list1:
    for j in list2:
        if i+j ==10:
            print(i,"+", j,"= 10")

print("$"*50)
#9)program to print squares of all even numbers in a list.
lst1= [3,2,5,6,7,4,8]
for val in lst1:
    if val%2==0:
        print(val,":",val**2)
#10)program to split the list into two-part, the left side all odd values and the right side all even values.

ls=[23,65,66,78,33,11,51,24]
even=[]
odd=[]
for val in ls:
    if val%2==0:
        even.append(val)
    else:
        odd.append(val)
print(odd+even)
odd.extend(even)
print(odd)#[23, 65, 33, 11, 51, 66, 78, 24]

#11)program to get common elements from two lists.
lst1=[23,45,65,34]
lst_2=[45,23,69,30]
lst_c=[]
for val in lst1:
    if val in lst_2:
        lst_c.append(val)
print("List of common values ",lst_c)#List of common values  [23, 45]

#12) program to reverse a list with for loop.
lst = [10,20,30,40,50]
for i in range(len(lst)-1,-1,-1):
    print(lst[i],end=" ")#50 40 30 20 10
print()
#13)program to reverse a list with a while loop.
l = [10,20,30,40,50]
count =len(l)-1
while count>=0:
    print(l[count],end=" ")#50 40 30 20 10
    count-=1
print()
#14)program to reverse a list using index slicing
l1= [10,20,30,40,50]
print(l[::-1])

#15)program to reverse a list with reversed and reverse methods.
lst1=[10,20,30,40,50]
print("Reversed():",list(reversed(lst1)))#Reversed(): [50, 40, 30, 20, 10]
lst2=[10,20,30,40,50]
lst2.reverse()
print("Reverse():",lst2)#Reverse(): [50, 40, 30, 20, 10]

#16)program to copy or clone one list to another list

lst1 = [34,56,78]
lst2=[]
for i in lst1:
    lst2.append(i)
print(lst2)#[34, 56, 78]

#17)program to return True if two lists have any common member.
ls1 = [3,4,6,7,8]
ls2= [3]

for val in ls1:
    if val in ls2:
        print("True")#True

#18)print a specific list after removing the 1st, 3rd, and 6th elements from the list.
lst1=[34,45,34,23,34,34,56]
lst2 = []
for i in range (len(lst1)):
    if i in (1,3,6):
        continue
    else:
        lst2.append(lst1[i])
print(lst2)#[34, 34, 34, 34]

#19)program to remove negative values from the list.
ls =[23,-56,-78]
ls1=[]
for val in ls:
    if val>=0:
        ls1.append(val)
print(ls1)#[23]

#20)program to get a list of all elements which are divided by 3 and 7.
ls =[21,34,42,54,84,49]
ls1=[]
for val in ls:
    if val%3==3 or val%7==0:
        ls1.append(val)
print(ls1)#[21, 42, 84, 49]