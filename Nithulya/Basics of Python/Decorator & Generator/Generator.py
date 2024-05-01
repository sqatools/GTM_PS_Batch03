
"""
A generator is a function or expression that will process a given iterable one object at a time, on demand.
"""

#1).
# def greeting():
#     yield 'Good Morning'
#     yield 'Good Afternoon'
#     yield 'Good Evening'
#     yield 'Good Night'
# obj1 = greeting()
# print(next(obj1))            # Good Morning         # Loading each message line by line when executing.
# print(next(obj1))            # Good Afternoon
# print(next(obj1))            # Good Evening
# print(next(obj1))            # Good Night
# print(next(obj1))            # Error : StopIteration

#(OR)
# def greeting():
#     yield 'Good Morning'
#     yield 'Good Afternoon'
#     yield 'Good Evening'
#     yield 'Good Night'
#
# obj1 = greeting()
# for val in obj1:
#     print(val)         # Good Morning, Good Afternoon, Good Evening, Good Night,(Do not show any error)


#2).
# import time
# import psutil as psutil
# def listValue():
#     list1 = [2,4,5,3]*5000
#     t1 = time.time()
#     for val1 in list1:
#         print(val1)
#     t2 = time.time()
#     print("Total Time Taken :", t2-t1)                    # Total Time Taken : 0.09769225120544434
#     print("CPU Usage :", psutil.cpu_percent(8))           # CPU Usage : 0.8
#     print("CPU Usage :", psutil.virtual_memory())         # CPU Usage : svmem(total=8345964544, available=1275781120, percent=84.7,
                                                                        # used=7070183424, free=1275781120)
# listValue()

#(OR) Checking the executing time without generator and with generator
import time
import psutil as psutil
def listValueGen():
    list1 = [2, 4, 5, 3] * 5000
    for val in list1:
        yield val

obj1 = listValueGen()
ta = time.time()
for val2 in obj1:
    print(val2)
tb = time.time()

print("Total Time Taken :", tb-ta)                 # Total Time Taken : 0.10456728935241699
print("CPU Usage :", psutil.cpu_percent(8))        # CPU Usage : 2.3
print("CPU Usage :", psutil.virtual_memory())      # CPU Usage : svmem(total=8345964544, available=1302716416, percent=84.4,
                                                                # used=7043248128, free=1302716416)
