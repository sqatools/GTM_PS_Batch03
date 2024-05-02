# 21). Python Dictionary program to insert a key at the beginning of the dictionary.

d1 ={"course":"python", "Institute": "sqatools"}
d2 ={"Name ":" Rahul"}


d2.update(d1)
print(d2) #{'Name ': ' Rahul', 'course': 'python', 'Institute': 'sqatools'}


#22). Python Dictionary  program to create a dictionary where keys are between 1 to 5
# and values are squares of the keys.

num = 5
d1 ={}
for i in range (1, 5):
    d1[i] = i**2

print(d1) #{1: 1, 2: 4, 3: 9, 4: 16}

#23). Python Dictionary program to find the product of all items in the dictionary.

D2 = { 'a' : 2, 'b' : 4, 'c' : 5}
pdt = 1
for v in D2.values():
    pdt *= v
print("The product of all values :", pdt) #The product of all values : 40

#24). Python Dictionary program to remove a key from the dictionary.

D3 = {'a':5, 'b':6,'c':8}
D4={}

for k,v in D3.items():
    if k !='c':
        D4[k] = v
print(D4) #{'a': 5, 'b': 6}

#25). Python Dictionary program to map two lists into a dictionary.
D1 ={}
l1 =["Name","Sports","Rank","Age"]
l2 = ["Sachin","cricket",1,50]

for i in range(0,len(l1)):

        D1[l1[i]] = l2[i]
print(D1)

D2 = dict(zip(l1,l2))
print(D2)

#26). Python Dictionary program to find maximum and minimum values in a dictionary.

d1 = {'a':34,'b':78,'c':100,'d':1}
l =[]
for v in d1.values():
    l.append(v)

print("Max val :",max(l))
print("Min val :",min(l))


#27).  Python Dictionary program to group the same items into a dictionary value.

list = [1,3,4,4,2,5,3,1,5,5,2,]
d={}
for el in list:
    d[el] = list.count(el)

print(d)
"""
from collections import defaultdict

list1 = [1,3,4,4,2,5,3,1,5,5,2]
print("The original list : ",list1)

dict1 = defaultdict(list)
for val in list1:
    dict1[val].append(val)
print("Similar grouped dictionary :" ,dict1)

"""

#28).  Python Dictionary program to replace words in a string using a dictionary.

str1 = "Learning Python at SQATools"
dict1 ={'at':'is','SQATools':'fun'}
print(str1)

for k ,v in dict1.items():
    str1 = str1.replace(k,v)

print(str1)


#28).  Python Dictionary program to replace words in a string using a dictionary.
String = "sqatools is best for learning python"
Dict = { 'best': 2, 'learning': 6}
list = String.split(" ")
print(list)
list1 =[]

for val in list:
    if val not in Dict:
        list1.append(val)
print(" ".join(list1))

# 30). Python Dictionary program to remove duplicate values from dictionary values.
Dict1 = { 'marks1' : [23,28,23,69], 'marks2' : [ 25, 14,25] }
for key, val in Dict1.items():
    for ele in val :
        if ele in val:
            val.remove(ele)

print(Dict1)





