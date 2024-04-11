st1 = {(2, 3, 5, 90), 4.5, 'string', True, False}
print(st1)
for val in st1:
    print(val)

print(dir(set))

"""
'add', 'clear', 'copy', 'difference', 'difference_update', 
'discard', 'intersection', 'intersection_update', 
'isdisjoint', 'issubset', 'issuperset',
 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
  'union', 'update']
"""
# add()
st1.add(100)
print(st1) # {True, 4.5, 'string', 100, (2, 3, 5, 90)}
st2 = st1.copy()
print(st2) # {False, True, 4.5, 100, 'string', (2, 3, 5, 90)}
print(st2.clear()) #None
st2.add(100)
st2.add((2, 3, 4))
st2.add(True)
print(st2) #{True, 100, (2, 3, 4)}
print(st1) #{False, 'string', True, 4.5, 100, (2, 3, 5, 90)}
num = st1.pop()
print(num) #False
print(st1) #{True, 4.5, 100, 'string', (2, 3, 5, 90)}
# union()
print(st1.union(st2)) #{True, 4.5, 100, (2, 3, 4), (2, 3, 5, 90), 'string'}

# intersection()
st1.intersection(st2)
print(st1)

print(st1.update(st2))
st1.remove('string')
print(st1)

# remove() discard()

st3 = {45, 78, 90, 54}
st3.remove(45)
print(st3)
# st3.remove(100) # throws an error if the value doesn't present in the given list
print(st3)
st3.discard(100)
print(st3)
# difference()
set10 = {1, 2, 3, 4}
set11 ={1, 2, 3, 4, 5, 6, 7, 8}

result = set11.difference(set10)
print(result) #{8, 5, 6, 7}

# difference_update()

set10 = {1, 2, 3, 4}
set11 ={1, 2, 3, 4, 5, 6, 7, 8}

set11.difference_update(set10)
print(set11)# {5, 6, 7, 8}
print(set10)# {1, 2, 3, 4}

# intersection()
set10 = {1, 2, 3, 4}
set11 ={1, 2, 3, 4, 5, 6, 7, 8}
result = set10.intersection(set11)
print(result) #{1, 2, 3, 4}

