#1). Lamda
# func = lambda x, y:  x+y
# print('Addition :',func(50, 60))     # Addition : 110


#2). Map : Map function help to mapping of any function with list of inputs
# def square(n):
#     return n*n
# list1 = [5, 7, 2, 8, 22, 3]
# result = list(map(square, list1))
# print('Result : ',result)                    # Result :  [25, 49, 4, 64, 484, 9]


#2).
# list1 = [5, 7, 2, 8, 22, 3]
# result2 = list(map(lambda x:x*x, list1))
# print("Result2 :", result2)                 # Result2 : [25, 49, 4, 64, 484, 9]



#3). Filter function : Filter the return the values on favorable condition
# list2 =  [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
# filter_result = list(filter(lambda x: x%2 ==0, list2))
# print(" Filter Result :", filter_result)                         #  Filter Result : [40, 30, 44, 22, 66, 2]

#2.
# list2 =  [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
# filter_result2 = list(filter(lambda x: x > 25, list2))
# print(" Filter Result 2:", filter_result2)                        #  Filter Result 2: [40, 30, 44, 66, 33]



#4). Reduce Function : Reduce function  provide a combine result
# from functools import reduce
# list3 = [55, 77, 33, 66, 23]
# reduce_result = reduce(lambda x,y: x+y, list3)
# print("Reduce Result :", reduce_result)                          # Reduce Result : 254

#2).
from functools import reduce
list4 = [1, 2, 3, 4]
reduce_result2 = reduce(lambda x,y: x*y, list4)
print("Reduce Result2 :", reduce_result2)                          # Reduce Result2 : 24