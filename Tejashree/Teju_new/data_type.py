"""
#data type
# if 2 variables are holding same value then memory address will be same. if different values means hold different address.
var1 = 10
print(id(var1))
var2 = 20
print(id(var2))
var3 =10
print(id(var3))

#rules to define variable name
# 1.variable name doesnot contain space
#var 1 = 40 # invalid variable
var1 -= 40
# 2. variable name cannot start by numbers
#1var = 50 # invalid variable
#3.special characters are not allowed in variable name
#var@12% = 50 # invalid variable

#4 variabale python is case sensitive
name = 'Rahul'
Name = 'Ravi'
NAME = 'Raju'
print(name,Name,NAME)
#############################################
# assign single value to multiple variable
a = b = c = 500
print(a,b,c)

# assign different value to different valur
P, Q, R = 20, 40, 60
print(P,Q,R)
##############################################

#mathematical operators (+ add,- sub,* mul,/ or //div , % reminder,** power)
"""
var1 = 12
var2 =5
print("value of A+B:", var1+var2)
print("value of A/B and A//B :", var1/var2 , var1//var2) # o/p 2.4 and 2

var3= 500
var4 = 600
var5 = 500
var6=7
print(var3 == var5) # True
print(var4 == var5) # false
print("power of 7:",var6**2 ) # 49 power operator



