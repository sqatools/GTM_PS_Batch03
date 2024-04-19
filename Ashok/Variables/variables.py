"""
1. Python determines the type of a variable during runtime, rather than during compilation.The interpreter
automatically determines the type of the variable.
2. In python, the values will have data type. Variables will just hold the value belonging to any type of data.
3. Variable name contains alphanumeric, characters. It cannot contain special characters except underscore(_).
4. Variable name should start with alphabet or underscore(_). It cannot start with numeric like '1Age' it
   can be 'Age1'
5. Python is case-sensitive
6. In python, we don't have range for values.
7. price = 250. If we assign the value directly to variable then it is a literal/constant.
8. Type casting - using these func int(), float(), complex(), bool(), str() we can convert one data type to another
   data type.
9. .__sizeof__() is a function to get the size of variable. ex: variable.__sizeof__()
10. Type function will be used to display the type of data
11. id function/method is used to find the memory location of variable. Syntax : id(variable name)
"""

""" 
1. If two variable are holding same value, then their memory address is same.Each variable 
with different value will have their different memory address.
2. id function/method is used to find the memory location of variable. Syntax : id(variable name)
9. .__sizeof__() is a function to get the size of variable. ex: variable.__sizeof__()
10. Type function will be used to display the type of data """
var1 = 10
print(id(var1))
var2 = 10
print(id(var2))

var3 = 200
print(id(var3))
print(type(var3))
print(var3.__sizeof__())

var4 = 25.5
print(id(var4))
print(type(var4))
print(var4.__sizeof__())

var5 = "Ashok"
print(id(var5))
print(type(var5))
print(var5.__sizeof__())

"""
3. Variable name contains alphanumeric, characters. It cannot contain special characters except underscore(_).
   It cannot contain spaces
4. Variable name should start with alphabet or underscore(_). It cannot start with numeric like '1Age' it
   can be 'Age1'
"""

age = 15
print(age)

# 1Age = 20     --> Syntax error
# age2num = 30  -->  Valid
# @Age = 30     --> Syntax error
# Age$#1 = 30   --> Syntax error
# var 1 = 40    --> Syntax error
# _age = 20     --> Valid
# var_age = 15  --> valid

_age = 20
print(_age)
var_age = 30
print(var_age)
age2num = 40
print(age2num)

""" There is no limit to defined variable name """
mathematic_var_value_holder = 700
print(mathematic_var_value_holder)

""" Python is case sensitive language, os variable with different will be considered individually."""
Name = 'Ashok'
NAME = 'Rahul'
name = 'Mohit'
print(Name, name, NAME)

""" assign single value to multiple variable """
a = b = c = 700
print("value a :", a)
print("value b :", b)
print("value c :", c)

"""assign different values to different variables """
p, q, r = 50, 60, 70
print("value of p:", p)
print("value of q:", q)
print("value of r:", r)









