# 1. Importing all functions from file1 :

import file1  # importing the file and calling all methods individually from file1

file1.Addition(2, 3)
file1.Multiplication(3, 4)
file1.Division(4, 2)

# 2. Importing particular functions form file1
from file1 import Addition, Multiplication

Addition(2, 3)  # We can call the functions directly.
Multiplication(9, 3)
# Division(9, 3)                  # It will throw error, didn't import the function

# 3. Importing all functions from file1 using *
# '*' means importing all functions from file, but it is not commonly using keyword because if we imported
# all functions from file, it will lead to name clashes.

from file1 import *

Addition(3, 2)  # We can call the functions directly.
Multiplication(9, 3)  # We can call the functions directly.
Division(9, 3)  # We can call the functions directly.

# 4. Importing all functions from file1 and given alias name to file1 then it is easy to call the methods from file

import file1 as f

f.Addition(5, 6)
f.Multiplication(6, 7)
f.Division(12, 4)

# 5. Importing particular function from file1 and given alias name to that function:
from file1 import Addition as a

a(5, 6)   # This is Addition method from file1
# File1.Addition(6,4)              # Error : Did not import this function here.
# File1.Multiplication(3,5)        # # Error : Did not import this function here.
