""" Python os Module:
Python has a built-in os module with methods for interacting with the operating system, like creating
files and directories, management of files and directories, input, output, environment variables,
process management, etc.
The os module has the following set of methods and constants
"""

import os
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
operations. It falls within the umbrella of Python's basic utility modules. This module aids in the
automation of the copying and deleting of files and folders
"""

# Remove non-empty directory #
# shutil.rmtree(r"C:\PythonAutomation\PyAuto1\Folder1")

# copy files from one location to another location
src_location = r"C:\PythonAutomation\PyAuto2\Folder2\file1.txt"
tar_location = r"C:\PythonAutomation\PyAuto2\Folder3"
shutil.copy(src_location, tar_location)
# note: It will not copy the empty files.


