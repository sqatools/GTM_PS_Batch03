# 31) Program to merge all elements of the list in a single entity using a special character.
lst1 = [ "a","b","c","d"]

print("$".join(lst1))#a$b$c$d
# 32)program to get the difference between two lists

lst2 = [45,67,45,23,89,90]
lst3 = [45,67]

for val in lst2:
        if val not in lst3:
            print(val,end=" ")#23 89 90

print()
#Input list
list1 = [34,55,12,89,44,67]
list2 = [55,89,34]

for value in list1:
    if value not in list2:
        print(value, end=" ")#12 44 67
print()
# 33)program to reverse each element of the list.
lst4 = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
lst5 = []
for val in lst4:
    val = val[::-1]
    lst5.append(val)
    print(val,end="")

print()
print(lst5)
# 34) program to combine two list elements as a sublist in a list.
list4 = [56,34,23,12,67]
list5 = [40,60,30,10,20]

fin = []
fin1 = []
for(x,y) in zip(list4,list5):
    fin.append([x,y])
    fin1.append(list((x,y)))
print(fin)
print(fin1)
# 35)program to get keys and values from the list of dictionaries.
list8 = [{'a':12},{'b': 34},{'c': 23},{'d': 11},{'e': 15}]
print(list8)
key=[]
value =[]

for element in list8:
    for val in element:
        key.append(val)
        value.append(element[val])
print(key)
print(value)



# 36)program to get all the unique numbers in the list.
list_a = [56,34,34,12,23,12,67]
uni =[]
for val in list_a:
    if val not in uni:
        uni.append(val)
print(uni)#[56, 34, 12, 23, 67]
# using set
#Input list
list1 = [56,34,34,12,23,12,67]

#Printing output
print(list(set(list1)))#[34, 67, 12, 23, 56]

# 37)program to convert a string into a list.
str = " It's a good day to have a good day!"
print(str.split())#["It's", 'a', 'good', 'day', 'to', 'have', 'a', 'good', 'day!']

# 38)program to replace the last and the first number of the list with the word.
list1 = [56,34,34,12,23,12,67]
list1[0] = "SQA"
list1[-1] = "Tools"
print(list1)#['SQA', 34, 34, 12, 23, 12, 'Tools']

# 39)program to check whether the given element is exist in the list or not.

list9 = [22,45,67,11,90,67]

print("Is 67 exist in list1? ", 67 in list9)
print("Is 10 exist in list1? ", 10 in list9)
# 40) program to remove all odd index elements.
lst9 = [22,45,67,11,90,67]
lst10 = []
for i in range(len(list9)):
    if i%2 == 0:
        lst10.append(lst9[i])
print(lst9)#[22, 45, 67, 11, 90, 67]
print(lst10)#[22, 67, 90]


