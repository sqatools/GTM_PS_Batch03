import sys

# 11). Python Dictionary program to sort a dictionary using keys.
dict_a = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}
for val in sorted(dict_a):
    print(val,dict_a[val])

# 12). Python Dictionary program to sort a dictionary in python using values.
dict_b = {'d' : 14, 'b' : 52,  'a': 13, 'c': 1 }



# 13). Python Dictionary program to add a key in a dictionary.
dict_c = {1:'a', 2:'b'}
dict_c[3] = 'c'
print(dict_c) # {1: 'a', 2: 'b', 3: 'c'}
# 14). Python Dictionary program to concatenate two dictionaries.
dict_d = {'name' : 'Yash', 'city' :  'Pune'}
dict_e= {'course' : 'python', 'institute' : 'sqatools'}
dict_d.update(dict_e)
print(dict_d)

# 15). Python Dictionary program to swap the values of the keys in the dictionary.
dict_f = {'name':'yash', 'city': 'Pune'}
dict_g ={}
print(dict_f)
for k,v in dict_f.items():
    dict_g[v] = k
print(dict_g)

#Input = {name:’yash’, city: ‘pune’}
#Output = {name:’pune’, city: ‘yash’}


# 16). Python Dictionary program to get the sum of all the items in a dictionary.
dict_h = {'x' : 23, 'y' : 10 , 'z' : 7}
s = 0
for key, val in dict_h.items():
    s = s+dict_h[key]
print("Sum of value :", s)



# 17). Python program to get the size of a dictionary in python.
dict_i = {'x' : 23, 'y' : 10 , 'z' : 7}
print(sys.getsizeof(dict_i),"bytes")

# 18). Python Dictionary program to check whether a key exists in the dictionary or not.
dict_j = {'x' : 23, 'y' : 10 , 'z' : 7}
# check if x exists
temp = 0
for key in dict_j.keys():
    if key == 'x':
        temp+=1
if temp>0:
    print("Key exists")
else:
    print("key doesn't exist")

# 19). Python program to iterate over a dictionary.
dict_k = {'food':'burger', 'type':'fastfood'}
for key,  val in dict_k.items():
    print(key, ":", dict_k[key])

# 20). Python Dictionary program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
n=4
dict_l ={}
for i in range(1,n+1):
    dict_l[i] = i**3

print(dict_l)
