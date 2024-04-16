# Write a python program to combine both the files with alternate lines and create new file.

def combine_two_files(file1, file2, file3):
    with open(file1, "r") as file1_obj:
        file1_list = file1_obj.readlines()

    with open(file2, "r") as file2_obj:
        file2_list = file2_obj.readlines()

    file3_list = []
    len_list = 0
    if len(file1_list) > len(file2_list):
        len_list = len(file1_list)
    else:
        len_list = len(file2_list)

    for i in range(len_list):
        file3_list.append(file1_list[i])
        file3_list.append(file2_list[i])

    with open(file3, "a") as file3_obj:
        for line in file3_list:
            file3_obj.write(line)


combine_two_files("read_file1.txt", "read_file2.txt", "append_file3.txt")


# Homework :
# 1. write a python program Replace file content JAVA with PYTHON.
# 2. write a python program to get all the email id from given file.
# 3. Write a python program to get all the phone number from given file.

# Python program to replace text in a file
with open('file1.txt', 'r') as f1:
    with open('file2.txt', 'w') as f2:
        for line in f1:
            f2.write(line.replace('Java', 'python'))


with open('file3.txt', 'r') as f3:
    for line in f3:
        line.find("@")
        print(line)








