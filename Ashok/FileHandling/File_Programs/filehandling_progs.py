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
#
#
# combine_two_files("read_file1.txt", "read_file2.txt", "append_file3.txt")

# Homework :
# 1. write a python program Replace file content JAVA with PYTHON.
# 2. write a python program to get all the email id from given file.
# 3. Write a python program to get all the phone number from given file.

# Python program to replace text in a file
# with open('file1.txt', 'r') as f1:
#     with open('file2.txt', 'w') as f2:
#         for line in f1:
#             f2.write(line.replace('Java', 'python'))

# 1. Python Program How to read a file in reading mode.

# Normal way
file = open("pfile1.txt", "r")
data1 = file.read()
print(data1)
file.close()

# with context manager
with open("pfile1.txt", "r") as f1:
    data2 = f1.read()
    print(data2)

# 2. Python file program to overwrite the existing file content.
with open("pfile1.txt", "w") as f2:
    f2.write("Line5: This London \n")

# 3. Python file program to append data to an existing file.
with open("pfile1.txt", "a") as f3:
    f3.write("Line6: This is Mumbai Indians")

# 4. Python file program to get the file’s first three and last three lines.
# use the readlines method to convert the content into list and apply slicing concept.

# 1st way
with open("pfile2.txt", "r") as f4:
    line_list1 = f4.readlines()
    k = line_list1[0:3:1]
    y = line_list1[-1:-4:-1]
    print(k)
    print(y)

# 2nd way
with open("pfile2.txt", "r") as f5:
    line_list2 = f5.readlines()
for i in (line_list2[:3]):
    print(i)
for m in (line_list2[-3:]):
    print(m)

# 5. Python file program to get all the email ids from a text file.
email_list = []
with open("pfile3.txt", "r") as f6:
    words_read = f6.read()
    words_list = words_read.split()
    for word in words_list:
        if "@" in word:
            email_list.append(word)
        else:
            continue
    print(email_list)

# 6. Python file program to get a specific line from the file
# use readlines method to convert the data into list and find the line with indexing.
with open("pfile2.txt", "r") as f7:
    specific_line = f7.readlines()
    print(specific_line[1])

# 7. Python file program to get odd lines from files and append them to separate files.
# seperate_list=[]
# with open("pfile2.txt", "r") as f8:
#     odd_lines = f8.readlines()
#     with open("pfile4.txt", "w") as f9:
#         for i in range(0,len(odd_lines)):
#             data = f9.write(s)
