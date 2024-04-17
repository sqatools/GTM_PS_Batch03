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


# def write_file(filename, content):
#     file = open(filename, "w")
#     file.write(content)
#     file.close()
#
# write_file("python.txt", "Good Morning")


######### Context Manager ###############
# def read_file_with_context_manager(filename):
#     with open(filename, "r") as file_obj:
#         data = file_obj.read()
#         print(data)
#         print("file is closed :", file_obj.closed)  # False
#
#     print("file is closed :", file_obj.closed) # True
#
# read_file_with_context_manager("python.txt")


######################### Different read option of the file #####################################################

#1. Read specific number of character from file
# def read_number_of_byte(filename, byte_count):
#     with open(filename, "r") as file_obj:
#         data = file_obj.read(byte_count)
#         print(data)
# read_number_of_byte("python.txt", 20)


#2. Read n number of line with readline method.
# def read_number_of_lines(filename, lines):
#     with open(filename, "r") as file_obj:
#         for i in range(lines):
#             data = file_obj.readline()
#             print(data, end="")
#
# read_number_of_lines("python.txt", 5)

#3. Read list of lines with help of readlines :
#1.
# def read_list_of_lines(filename):
#     with open(filename, "r") as file:
#         lines_data = file.readlines()
#         return lines_data
# print(read_list_of_lines("python.txt"))           # It will be in list format including \n


#2.
# def read_list_of_lines(filename):
#     with open(filename, "r") as file:
#         lines_data = file.readlines()
#         return lines_data
# read_list_of_lines("python.txt")
# def read_specific_line(filename, line_no):
#     lines_list = read_list_of_lines(filename)
#     print(lines_list[line_no-1])
#
# read_specific_line("python.txt", 5)         # 5.software development,
#
# read_specific_line("python.txt", 2)     # 2.Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.


#3
# def read_list_of_lines(filename):
#     with open(filename, "r") as file:
#         lines_data = file.readlines()
#         return lines_data
# read_list_of_lines("python.txt")
# def print_specific_number_line_from_end_of_file(filename, num_line):
#     lines_list = read_list_of_lines(filename)
#     for i in lines_list[-3:]:
#         print(i)
# print_specific_number_line_from_end_of_file("python.txt", 3)

############ tell() method : This method will tell you the current cursor position.
# def set_different_cursor_position(filename):
#     with open(filename, "rb") as file:
#         print("Start position of cursor :", file.tell())
#         char_5 = file.read(5)
#         print(char_5)
#         print("Current position of cursor :", file.tell())
# set_different_cursor_position("python.txt")


############ seek method :  This method will help to set the cursor poition with respect to
# 1. Beginning of file
# 2. End of file
# 3. current position of cursor

# set cursor at 30 position from beginning of file
    # file.seek(30, 0)  # setting the cursor position from begining of file
    # file.seek(30, 1)  # set the cursor position from current position of the cursor
    # file.seek(-30, 2) # set the cursor position from end of the file

#1.
# with open("python.txt", "rb") as file:
#     file.seek(40,0)
#     char_40 = file.read()
#     print(char_40)

#2.
# with open("python.txt", "rb") as file:
#     file.seek(40,1)
#     char_40 = file.read()
#     print(char_40)

#3.
# with open("python.txt", "rb") as file:
#     file.seek(-40,2)
#     char_40 = file.read()
#     print(char_40)


# Write a python program to combine both the files with alternate lines and create new file.
# def combine_two_files(file1, file2, file3):
#     with open(file1, "r") as file1_obj:
#         file1_list = file1_obj.readlines()
#
#     with open(file2, "r") as file2_obj:
#         file2_list = file2_obj.readlines()
#
#     file3_list = []
#     len_list = 0
#     if len(file1_list) > len(file2_list):
#         len_list = len(file1_list)
#     else:
#         len_list = len(file2_list)
#
#     for i in range(len_list):
#         file3_list.append(file1_list[i])
#         file3_list.append(file2_list[i])
#
#     with open(file3, "a") as file3_obj:
#         for line in file3_list:
#             file3_obj.write(line)
# combine_two_files("file1.txt", "file2.txt", "file3.txt")


#1. write a python program Replace file content JAVA with PYTHON.

# def replaceString(file1,file2):
#     with open(file1, "r") as file1_obj:
#         file1_list = file1_obj.readlines()
#         print(file1_list)
#         str=' '
#         for i in file1_list:
#             str=str+i.replace('Java','Python')
#         print(str)
#     with open(file2, "a") as file2_obj:
#         for line in str:
#             file2_obj.write(line)
# replaceString("file1.txt","file4.txt")


#2. write a python program to get all the email id from given file.
# def getString(file1,file2):
#     with open(file1, "r") as file1_obj:
#         file1_list = file1_obj.readlines()
#         str1=' '
#         for i in file1_list:
#             word1=i.split()
#             for j in word1:
#                 if '@' in j:
#                     str1=str1+"\n"+j
#         print(str1)
#     with open(file2, "a") as file2_obj:
#         for line in str1:
#             file2_obj.write(line)
# getString("file1.txt","file5.txt")


#3. Write a python program to get all the phone number from given file.
def getString(file1,file2):
    with open(file1, "r") as file1_obj:
        file1_list = file1_obj.readlines()
        str1=' '
        for i in file1_list:
            word1=i.split()
            for j in word1:
                if j.isnumeric() and len(j)==10:
                    str1=str1+"\n"+j
        print(str1)
    with open(file2, "a") as file2_obj:
        for data in str1:
            file2_obj.write(data)
getString("file1.txt","file5.txt")

