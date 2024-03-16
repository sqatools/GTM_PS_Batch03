## Integer
x = 20
y = 10
z=x+y
print(z, type(x))

## Float
x = 20.0
y = 10.0
z=x+y
print(z, type(x))

## Complex
x = 20+10j
y= 10+5j
z=x+y
print("Value : ",z, type(z))

##String
str1 = "WELCOME"
print(str1[2],type(str1))   # +ve indexing
print(str1[-2],type(str1))  # -ve indexing

##List
list1 = [1,2,3,4,'Hello',[3,4]]
print("List1 ",list1,type(list1))
list1.append(100)
print("List1 ",list1)
list1[1]=400
print("List1 ",list1)
print("List1 string  : ",list1[4])
print("List1 string first letter : ",list1[4][0])