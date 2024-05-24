#21)program to check whether the given list is palindrome or not.
lst = [3,4,5,6,7,6,5,4,3]
lst1=lst[::-1]

result= ("palindrome" if (lst == lst1) else "not a palindrome list")

print(result)

#22)Program to get a list of words which has vowels in the given string.
st1 = "www Student ppp are qqqq learning Python vvv"
lst2 = st1.split()
print(lst2)
vow = ['a','e','i','o','u']
vow1 =[]

for val in lst2:
    for chr in val:
        if chr in vow:
            vow1.append(val)
        else:
            continue
print(vow1)

#23)program to add 2 lists with extend method.

lst3 = [1,2,3]
lst4 = [4,5,6]
lst3.extend(lst4)
print(lst3)#[1, 2, 3, 4, 5, 6]
#24)program to sort list data, with the sort and sorted method.

lst5 = [23,45,21,25,43,20]
lst5.sort()
print("using sort :",lst5)
lst6 = [23,45,21,25,43,20]
print("using sorted ():",sorted(lst6))
#25) Remove data from the list from a specific index using the pop method.

lst7 = [23,45,21,25,43,20]
print(lst7)
lst7.pop(3)
print(lst7)#[23, 45, 21, 43, 20]

# 26)program to get the max, min, and sum of the list using in-built functions.
lst8 = [23,45,21,25,43,20]

print("Min :",min(lst8))#Min : 20
print("Max :",max(lst8))#Max : 45
print("Sum :",sum(lst8))#Sum : 177

#27)program to check whether a list contains a sublist.

lst8 = [23,45,21,25,43,20]
lst9 = [45,21,25]
count = 0
for val in lst8:
    for ele in lst9:
        if val == ele :
            count += 1

if count == len(lst9):
    print("Sublist")
else:
    print("Not a sublist")

# 28)program to generate all sublist with 5 or more elements in it from the given list.

# 29)program to find the second large number from the list.

list1 = [23,45,21,25,43,20]
list1.sort()
print("The second large number :",list1[-2])
# 30) program to find the second small number from the list.

print("The second small number :",list1[1])








