"""
A generator is a function or expression that will process a given iterable one object at a time, on demand.

If you use yield keyword in function then that function is generator
yield will return in the form of iterator.
finally, generator returns the iterator
"""


# 1.
def greeting():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good Evening'
    yield 'Good Night'


obj1 = greeting()
print(next(obj1))  # Good Morning    # Loading each message line by line when executing.
print(next(obj1))  # Good Afternoon
print(next(obj1))  # Good Evening
print(next(obj1))  # Good Night
# print(next(obj1))  # It will throw Error : StopIteration


# 2.
def greeting1():
    yield 'Good Morning'
    yield 'Good Afternoon'
    yield 'Good Evening'
    yield 'Good Night'


obj1 = greeting1()
for val in obj1:
    print(val)  # Good Morning, Good Afternoon, Good Evening, Good Night,(Do not show any error)
