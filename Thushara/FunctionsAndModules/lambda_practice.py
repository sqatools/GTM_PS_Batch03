str1= 'hello how are you'
fun = lambda string: string.upper()
print(fun(str1)) #HELLO HOW ARE YOU

lst1 = [2, 4, 6,1]
fun1 =list(map(lambda x: x**3 , lst1))
print(fun1) #[8, 64, 216, 1]


list2 = [45, 78, 32, 21, 24]
fun2 = list(filter(lambda x:x%3==0, list2))
print(fun2) #[45, 78, 21, 24]

from functools import reduce

lst3 = [1, 2, 3, 4]
result = reduce(lambda x,y : x*y , lst3)
print(result) #24

function1 = lambda a: a+10
print (function1(45)) #55

lf = lambda  x,y,z :x*y*z
print(lf(4,6,7)) #168

