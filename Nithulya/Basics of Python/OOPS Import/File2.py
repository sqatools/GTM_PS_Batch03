#1).  Importing all functions from File1 :
# import File1
# File1.Addition(6,4)                   # Addition :  10
# File1.Multiplication(3,5)             # Multiplication :  15
# File1.Division(50,10)                 # Division :  5

#2).  Importing perticular function from File1:
# from File1 import Division
# Division(100,5)              # Division :  20
# File1.Addition(6,4)                      # Error : Did not import this function here.
# File1.Multiplication(3,5)                # Error : Did not import this function here.

#3). Importing all functions from File1 and give name to file :
# import File1 as f1           # File1 as f1 : It is for easy to call.
# f1.Addition(6,4)                   # Addition :  10
# f1.Multiplication(3,5)             # Multiplication :  15
# f1.Division(50,10)                 # Division :  5

#4).Importing perticular function from File1 and give name to that function:
# from File1 import Division as D1      # Division as D1 : It is for easy to call.
# D1(100,5)              # Division :  20
# File1.Addition(6,4)              # Error : Did not import this function here.
# File1.Multiplication(3,5)        # # Error : Did not import this function here.

#5).  Importing all functions from File1 :
# from File1 import *                        # '*' means importing all functions from file but it is not commonly using keyword because
#                                            # if we imported all functions from file, it will leads to name clashes.
# Addition(6,4)                   # Addition :  10
# Multiplication(3,5)             # Multiplication :  15
# Division(50,10)                 # Division :  5




