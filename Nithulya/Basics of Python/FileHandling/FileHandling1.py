"""
read mode(r)
write mode(w)
append mode(a)
"""

#1.
# file=open("python.txt",'r')
# print(file.read())             # Read whole content
# file.close()
#2.
# file=open("python.txt",'r')
# print(file.read(16))           #choose how many charecters we need.
#file.close()

#3.
# file=open("python.txt",'r')
# print(file.readline())           #It will print first line
#file.close()

#4.
# file=open("python.txt",'r')
# print(file.readline())
# print(file.readline())             # It will print two lines.
#file.close()

#5. Loop through the file line by line:
# file=open("python.txt",'r')
# for i in file:
#     print(i)
#file.close()


#6. Read :
# def read_file(filename):
#     file = open(filename, "r")
#     data = file.read()
#     file.close()
#     print(data)


#read_file("python.txt")         # If it is in the same folder we only need to enter the file name.
#read_file("FileHandling2")      # It will show an error because this file in different folder.
#read_file("C:\\PythonAutomation\\Nithulya\\FileHandling2.txt")       # This file in different folder so we need to enter the path.


#1. Append :  append to the end of the file
# file=open("python.txt",'a')
# file.write("This text is an addition to an existing file.")
# file.close()
#
# file=open("python.txt")
# print(file.read())
# file.close()


#1.Write - will overwrite any existing content
# file=open("python.txt",'w')
# file.write('Woops! I have deleted the content!.')
# file.close()
#
# file=open("python.txt",'r')
# print(file.read())
# file.close()


def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()

write_file("python.txt", "Good Morning")


