""" Python os Module:
Python has a built-in os module with methods for interacting with the operating system, like creating
files and directories, management of files and directories, input, output, environment variables,
process management, etc.
The os module has the following set of methods and constants
"""

import os
import random
import shutil
import time

# OS Path #
# os.path is the sub module of the main module i.e, os module
# Functions are available in os

# os.path.exists() - check if path is exist or not
print(os.path.exists(r"C:\PythonAutomation\PyAuto"))

# os.path.isfile() - check if path belongs to file
print(os.path.exists(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))

# os.path.isdir() - given path is file or dir
print(os.path.isdir(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))
print(os.path.isdir(r"C:\PythonAutomation\PyAuto\Child1"))

# os.path.split() - split address and file name
print(os.path.split(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))
# o/p: ('C:\\PythonAutomation\\PyAuto\\Child1', 'newfile.txt')

# os.path.join() - join path and filename together to give single path
print(os.path.join(r"C:\PythonAutomation\PyAuto\Child1", "newfile.txt"))
# o/p: C:\PythonAutomation\PyAuto\Child1\newfile.txt

# os.path.basename()
print(os.path.basename(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))
# o/p: newfile.txt

# os.path.dirname()
print(os.path.dirname(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))
# o/p: C:\PythonAutomation\PyAuto\Child1

# os.path.getmtime() - Last Modified time
print(time.ctime(os.path.getmtime(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt")))

# os.path.getatime()  - Last Access time
print(time.ctime(os.path.getatime(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt")))

# os.path.getctime()  - Created time
print(time.ctime(os.path.getctime(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt")))

# os.path.relpath() - access something from another folder
print(os.getcwd())  # To get the current working directory.
print(os.path.relpath(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))
# o/p: ..\..\..\PyAuto\Child1\newfile.txt

# os.path.abspath()  - access something in absolute way
print(os.path.abspath(r"..\..\..\PyAuto\Child1\newfile.txt"))
# o/p: C:\PythonAutomation\PyAuto\Child1\newfile.txt

# os.path.getsize() - This will provide the file size
print(os.path.getsize(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt"))

# OS Module #

# os.getlogin() - Provides the current user
print(os.getlogin())

# os.getcwd() - get the current working directory
print(os.getcwd())

# os.chdir() - change directory
# print(os.chdir(r"C:\PythonAutomation\PyAuto\Child1"))
print(os.getcwd())

# os.listdir() - give list of file in current directory
print(os.listdir(r"C:\PythonAutomation\GTM_PS_Batch03\Ashok"))

# os.mkdir() - create a folder
# os.mkdir(r"C:\PythonAutomation1")

# os.makedirs() - create a multiple folders
# os.makedirs(r"C:\PythonAutomation1\Folder1\Folder2")

# os.remove()  -
# os.remove(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt")

# os.rmdir() -
# os.rmdir(r"C:\PythonAutomation1")

# os.removedirs() -
# os.rmdir(r"C:\PythonAutomation\PyAuto\Child2")

"""
The Shutil module allows you to do high-level operations on a file, such as copy, create, and remote
operations. It falls within the umbrella of Python's basic utility modules1. This module aids in the
automation of the copying and deleting of files and folders.
"""

# Remove non-empty directory #
# shutil.rmtree(r"C:\PythonAutomation\PyAuto1\Folder1")

# copy files from one location to another location
src_location = r"C:\PythonAutomation\PyAuto2\Folder2\file1.txt"
tar_location = r"C:\PythonAutomation\PyAuto2\Folder3"
shutil.copy(src_location, tar_location)
# note: It will not copy the empty files.

# get values from environment variable #
print(os.getenv("NUMBER_OF_PROCESSORS"))
print(os.getenv("PROCESSOR_ARCHITECTURE"))

# get CPU count #
print(os.cpu_count())

# Run windows command #
print(os.system("control"))  # open control panel of windows

print(os.system("appwiz.cpl"))  # open program feature

print(os.system("dir C:\\PythonAutomation"))  # get all file folder data

# Check file permission #
permission = os.access(r"C:\PythonAutomation\PyAuto\Child1\newfile.txt", os.X_OK)
print("File permission :", permission)

"""
mode	Required.
os.F_OK: Checks if the path exists.
os.R_OK: Checks if the path is readable.
os.W_OK: Checks if the path is writable.
os.X_OK: Checks if the path is executable.
"""

# Generate random string in python #
output = os.urandom(100)
print("random string :", output)

# Generate random integer #
# return any random in given values
result = random.randint(1000, 1200)   # 1013
print(result)

# return any random value in given range along with difference value as like range method.
val = random.randrange(2, 10, 2)
print("val  :", val, type(val))

# it will provide random floating number 0 to 1
val2 = random.random()
print(val2)          # 0.35347856816623346

# generate random binary numbers #
bin = ''
for i in range(10):
    val = random.randint(0, 1)
    bin = bin + str(val)

print(bin)

###############################
number = random.getrandbits(10)
print(number, format(number, "0b"))