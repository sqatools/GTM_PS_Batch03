#1). Python Dictionary program to add elements to the dictionary.
dict1 = {}
dict1["Name"] = "Aadi"
dict1["Age"] = 21
dict1["email"]="aadi21@gmail.com"


print(dict1)#{'Name': 'Aadi', 'Age': 21, 'email': 'aadi21@gmail.com'}
print("Name:",dict1["Name"])

#2). Python Dictionary program to print the square of all values in a dictionary.
dict2 = {'a':4,'b':7,'c':5,'d':2}
for key in dict2:
    print(key,":",dict2[key]**2)
    print(dict2['d'])

# 3). Python Dictionary program to move items from dict1 to dict2.
dict6 ={'Name': 'Aadi', 'Age': 21, 'email': 'aadi21@gmail.com'}
dict7 ={}
for val in dict6:
    dict7[val]=dict6[val]
print(dict7)#{'Name': 'Aadi', 'Age': 21, 'email': 'aadi21@gmail.com'}
for val in dict7:
    print(dict7[val])

#4). Python Dictionary program to concatenate two dictionaries.
dict1 ={'Name': 'Aadi', 'Age': 21, 'email': 'aadi21@gmail.com'}
dict2 ={'Salary':"$250k"}
dict1.update(dict2)
print(dict1)

#5). Python Dictionary program to get a list of odd and even keys from the dictionary.
dict8 = {1:25,5:'abc',8:'pqr',21:'xyz',12:'def',2:'utv'}
print(dict8)
list1 =[]
list2=[]
for val in dict8:
    if val%2==0:
        l=[val,dict8[val]]
        list1.append(l)
    else:
        l1=[val,dict8[val]]
        list2.append(l1)
print("Even keys :",list1)
print("Odd keys:",list2)

l3=[[val,dict8[val]] for val in dict8 if val%2==0]
l4 =[[val,dict[val]] for val in dict8 if val%2!=0]
print(l3) # [[8, 'pqr'], [12, 'def'], [2, 'utv']]
print(l4) # [[1, dict[1]], [5, dict[5]], [21, dict[21]]]
# 6). Python Dictionary Program to create a dictionary from two lists.
dict={}
list1 = ['a','b','c','d','e','f']
list2 = [12, 23, 24, 25, 15, 16]
for x,y in zip(list1,list2):
    dict[x]=y
print(dict)# {'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15, 'f': 16}

# 7). Python Dictionary program to store squares of even and cubes of odd numbers in a dictionary using dictionary comprehension.
list1 =[4, 5, 6, 2, 1, 7, 11]
dict9 ={}
for val in list1:
    if val%2==0:
        dict9[val]=val**2
    else:
        dict9[val]=val**3
print(dict9)# {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331}
# 8). Python Dictionary program to clear all items from the dictionary.
dicta ={'a': 12, 'b': 23, 'c': 24, 'd': 25, 'e': 15, 'f': 16}
dicta.clear()
print(dicta)#{}
# 9). Python Dictionary program to remove duplicate values from Dictionary.
db ={'a': 12, 'b': 12, 'c': 24, 'd': 12, 'e': 15, 'f': 15}
dc = {}

for key,val in db.items():
    if val not in dc.values():
        dc[key] = val

print(dc) # {'a': 12, 'c': 24, 'e': 15}

# 10). Python Dictionary program to create a dictionary from the string.

st1 = 'Verryyy gooodddd moorrnnniniggggg'
d7={}

for char in st1:
    d7[char]=st1.count(char)
print(d7) # {'V': 1, 'e': 1, 'r': 4, 'y': 3, ' ': 2, 'g': 6, 'o': 5, 'd': 4, 'm': 1, 'n': 4, 'i': 2}

