# 1). Python Program How to read a file in reading mode
def read_a_file(filename):
    with open(filename,'r') as f:
        data = f.readlines()
        return data



d1 = read_a_file('test_data.txt')


print(d1)


# 2). Python file program to overwrite the existing file content

def write_a_file(filename):
    with open(filename,'w') as file1:
        file1.write("PYTHON is a popular programming language.It was created by Guido van Rossum, and released in 1991. ")
    data = read_a_file('test_data.txt')
    return data

d4 = write_a_file('test_data.txt')
print(d4)

#  3). Python file program to overwrite the existing file content.

def append_a_file(filename):
    with open(filename,'a') as f1:
        f1.write("Python is easy to learn")
    d1 =read_a_file('test_data.txt')
    return d1



d1 = append_a_file('test_data.txt')
print(d1)


# 4).  Python file program to get the file’s first three and last three lines.
data_list=[]
with open('family.txt', 'r') as file:
    data_list = file.readlines()
    for line in (data_list[:3]):
        print(line)
    print("@"*50)
    for line in (data_list[-3:]):
        print(line)


# 5). Python file program to get all the email ids from a text file.
e_mail =[]
with open("email.txt", 'r') as f1:
    data = f1.readlines()
    for line in data:
        for word in line.split(" "):
            if '@' in word:
                e_mail.append(word)
    print("List of e_mails")
    print("-" * 50)
    print(e_mail)



