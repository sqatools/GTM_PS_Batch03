# Pending topics: function as parameter, function as object, decorator, generator, lambda functions #
"""
Anonymous/Lambda Function:
--------------------------
1. Sometimes we need to declare a function without any name. The nameless property function is called an
anonymous function or lambda function.
2. The reason behind the using anonymous function is for instant use, that is, one-time usage. Normal function is
declared using the def function. Whereas the anonymous function is declared using the lambda keyword.
3. In opposite to a normal function, a Python lambda function is a single expression.
But, in a lambda body, we can expand with expressions over multiple lines using parentheses or a multiline string.
4. A lambda function can take any number of arguments, but can only have one expression.
Syntax: lambda arguments : expression

5. We are not required to write explicitly return statements in the lambda function because the lambda internally
returns expression value.
6. Lambda functions are more useful when we pass a function as an argument to another function. We can also use
the lambda function with built-in functions such as filter, map, reduce because this function requires
another function as an argument.
"""


def miles2km(miles):
    kms = 1.6 * miles
    return kms


print(miles2km(5))

# using lambda for above function.
# 5. We are not required to write explicitly return statements in the lambda function because the lambda internally
# returns expression value.
kms = lambda x, y: x * y
print(kms(1.6, 5))

""" 

How to use filter, map, reduce functions.
----------------------------------------
In Python, the filter() function is used to return the filtered value. We use this function to filter values
based on some conditions. Syntax:  filter(function, sequence)
where,
function – Function argument is responsible for performing condition checking.
sequence – Sequence argument can be anything like list, tuple, string
------------------------------------------------------------------------------------------------------------------
In Python, the map() function is used to apply some functionality for every element present in the given sequence 
and generate a new series with a required modification. Syntax: map(function,sequence)
where,
function – function argument responsible for applied on each element of the sequence
sequence – Sequence argument can be anything like list, tuple, string

Ex: for every element present in the sequence, perform cube operation and generate a new cube list.
----------------------------------------------------------------------
In Python, the reduce() function is used to *minimize sequence elements* into a *single value* by applying the 
specified condition. The reduce() function is present in the functools module; hence, we need to import it using 
the import statement before using it. 
Syntax: reduce(function, sequence)
----------------------------------------------------------------------------------------------------
"""

# lambda function with Filter:
l = [-10, 5, 12, -78, 6, -1, -7, 9]
positive_nos = list(filter(lambda x: x > 0, l))
print("Positive numbers are:", positive_nos)

# lambda function with map:
list1 = [2, 3, 4, 8, 9]
list2 = list(map(lambda x: x * x * x, list1))
print("Cube values are:", list2)

# lambda function with reduce:
from functools import reduce

list3 = [20, 13, 4, 8, 9]
add = reduce(lambda x, y: x + y, list3)
print("Addition of all list elements is:", add)

# Another example for filter, map, reduce #
nums = [3, 2, 6, 8, 4, 6, 2, 9]
evens = list(filter(lambda n: n % 2 == 0, nums))
print("Even numbers are:", evens)

doubles = list(map(lambda n: n * 2, evens))
print("Doubles are:", doubles)

sum = reduce(lambda x, y: x+y, doubles)
print("Sum of all values:", sum)