"""
read mode(r)
write mode(w)
append mode(a)
"""

def read_file(filename):
    file = open(filename, "r")
    data = file.read()
    file.close()
    print(data)

#read_file("read_data.txt")
read_file("E:\\Filesdata\\file1.txt")


def write_file(filename, content):
    file = open(filename, "w")
    file.write(content)
    file.close()


# when we open file to write there are possible case.
# 1. write existing available file : It will update existing content of the file
# write_file("write_data.txt", "Good Morning")

# 2. write to new file. : It will create new file and add content.
# write_file("write_new_file.txt", "Add content to fresh file.")

write_file("E:\\Filesdata\\write_new_file.txt", "Add content to fresh file.")
