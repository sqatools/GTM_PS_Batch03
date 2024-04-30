########################## Lambda -Anonymous Function,(lambda arguments : expressions) ##############################
#1).
# func1 = lambda x : x+1
# print('Result : ',func1(6))          # Result :  7

#2).
# func = lambda x, y:  x+y
# print('Addition :',func(50, 60))     # Addition : 110

#3).Check even or odd using lambda function:
# func1 = lambda n : 'Even' if n%2==0 else 'Odd'
# print(f'Number {5} is ',func1(5))          # Number 5 is  Odd

#3).Sort value using Lambda function:
# tup1 = [('Nivya',60),('Riya',80),('Abhi',70)]
# tup1.sort(key=lambda x : x[0])
# print('Tup1:',tup1)                  # Tup1: [('Abhi', 70), ('Nivya', 60), ('Riya', 80)]

#b
# tup1 = [('Nivya',60),('Riya',80),('Abhi',70)]
# tup1.sort(key=lambda x : x[1])
# print('Tup1:',tup1)                   # Tup1: [('Nivya', 60), ('Abhi', 70), ('Riya', 80)]

#c
# tup1 = [('Nivya',60),('Riya',80),('Abhi',70)]
# tup1.sort(key=lambda x : x[1],reverse=True)
# print('Tup1:',tup1)                     # Tup1: [('Riya', 80), ('Abhi', 70), ('Nivya', 60)]


########################## Map : Map function help to mapping of any function with list of inputs ###################
######################### map(function,iterable) : Creating new list and old list keeps as same ################
#1).
# def square(n):
#     return n*n
# list1 = [5, 7, 2, 8, 22, 3]
# result = list(map(square, list1))
# print('Result : ',result)                    # Result :  [25, 49, 4, 64, 484, 9]


#2).
# list1 = [5, 7, 2, 8, 22, 3]
# result2 = list(map(lambda x:x*x, list1))
# print("Result2 :", result2)                 # Result2 : [25, 49, 4, 64, 484, 9]

#3).
# def cube(n):
#     return n**3
# value1 = list(map(cube,[2,3,4,5]))
# print('Result:',value1)                   # Result: [8, 27, 64, 125]

#4).
# list1 = [1,3,4,-2,-55,-23]
# value1 = list(map(abs,list1))
# print('List2:',value1)                     # List2: [1, 3, 4, 2, 55, 23]

#5).
# list1 = [1,3,4,-2,-55,-23]
# value1 = list(map(lambda x : x+1,list1))
# print('List2:',value1)                      # List2: [2, 4, 5, -1, -54, -22]


################### Filter function : Filter the return the values on favorable condition ############################
################### filter(function,iterable) ########################################################################
#1).
# list1 = [1,3,4,-2,-55,-23]
# def positive(n):
#     return True if n>0 else False
# val1 = list(filter(positive,list1))
# print('List2:',val1)                                     # List2: [1, 3, 4]

#2).
# val1 = list(filter(lambda x:x.isupper(),'AppLe'))
# print('Result:',val1)                                      # Result: ['A', 'L']

#3).
# list2 =  [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
# filter_result = list(filter(lambda x: x%2 ==0, list2))
# print(" Filter Result :", filter_result)                         #  Filter Result : [40, 30, 44, 22, 66, 2]

#4.
# list2 =  [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
# filter_result2 = list(filter(lambda x: x > 25, list2))
# print(" Filter Result 2:", filter_result2)                        #  Filter Result 2: [40, 30, 44, 66, 33]

#5).
# list1 = [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
# filter_result2 = list(filter(lambda x: x%2==0,list1))
# print('List2:',filter_result2)                                     # List2: [40, 30, 44, 22, 66, 2]

############################ Reduce Function : Reduce function  provide a combine result #########################
#1).
# from functools import reduce
# def value1(x,y):
#     return x+y
# val1 = reduce(value1,[1,2,3,4,5])
# print('List2:',val1)                                 # List2: 15

#2).
# from functools import reduce
# list3 = [55, 77, 33, 66, 23]
# reduce_result = reduce(lambda x,y: x+y, list3)
# print("Reduce Result :", reduce_result)                          # Reduce Result : 254

#3).
# from functools import reduce
# list4 = [1, 2, 3, 4]
# reduce_result2 = reduce(lambda x,y: x*y, list4)
# print("Reduce Result2 :", reduce_result2)                          # Reduce Result2 : 24

#4).
from functools import reduce
list1 = [40, 13, 30, 44, 22, 17, 66, 2, 1, 33]
filter_result2 = list(filter(lambda x: x%2==0,list1))
print('List2:',filter_result2)
reduce_result2 = reduce(lambda x,y: x+y, filter_result2)
print("Reduce Result2 :", reduce_result2)


