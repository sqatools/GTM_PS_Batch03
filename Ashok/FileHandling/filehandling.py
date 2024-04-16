"""
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode. # syntax: f=open("filename.txt","filemode")
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:

There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending the content to end of existing data, or creates the file
      if it does not exist
"w" - Write - Opens a file for writing and overrides the existing content if file exist, or creates the file
       if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition, you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""


def read_file(filename):
    file_reading = open(filename, "r")
    printing_file = file_reading.read()
    print(printing_file)
    file_reading.close()


read_file("C:\\PythonAutomation\\GTM_PS_Batch03\\Ashok\\FileHandling\\demo1.txt")


def write_append_file1(filename, content):
    file_writing = open(filename, "a")
    file_writing.write(content)
    file_writing.close()


write_append_file1("demo1.txt", "\n9. hello world")
write_append_file1("demo2.txt", "1. Hello world, this is a new file")


def write_writing_file2(filename, content):
    file_writing = open(filename, "w")
    file_writing.write(content)
    file_writing.close()


write_writing_file2("demo2.txt", "Hello Ashok, replacing with previous content")
write_writing_file2("demo3_new.txt", "Hello This is a new file")


# Context Manager #
def read_file_with_context_manager(filename):
    with open(filename, "r") as file_obj:
        data = file_obj.read()
        print(data)
        print("file is closed :", file_obj.closed)

    print("file is closed :", file_obj.closed)


read_file_with_context_manager("demo1.txt")


def write_file_with_context_manager(filename, content):
    with open(filename, "a") as file_obj2:
        file_obj2.write(content)
        print("file is closed :", file_obj2.closed)

    print("file is closed :", file_obj2.closed)


write_file_with_context_manager("demo4_new.txt", "This a file with context manager")


# Different read options of the file #
# 1. Read a specific number of characters from file

def read_number_of_bytes(filename, byte_count):
    with open(filename, "r") as file_obj3:
        data1 = file_obj3.read(byte_count)
        print(data1)


read_number_of_bytes("demo1.txt", 30)


# 2. readline(): This method reads a single line from the file each time it is called #
def read_number_of_lines(filename, lines_count):
    with open(filename, "r") as file_obj4:
        for i in range(lines_count):
            data = file_obj4.readline()
            print(data, end="")


read_number_of_lines("demo1.txt", 5)


# 3. readlines(): this method read all the lines but in list format. #
def read_list_of_lines(filename):
    with open(filename, "r") as file:
        lines_data = file.readlines()
        return lines_data


print(read_list_of_lines("demo1.txt"))
print()


# 4. read a specific line from list #
def read_specific_line(filename, line_no):
    lines_list = read_list_of_lines(filename)
    print(lines_list[line_no - 1])


read_specific_line("demo1.txt", 5)

"""
# tell() method : This method will tell you the current cursor position.
# seek method :  This method will help to set the cursor position with respect to
# 1. Begining of file
# 2. End of file
# 3. current position of cursor
"""


def tell_different_cursor_position(filename):
    with open(filename, "rb") as file:
        print("start position of cursor :", file.tell())
        char_10 = file.read(10)
        print(char_10)
        print("current position of cursor :", file.tell())


tell_different_cursor_position("demo1.txt")


def set_different_cursor_position(filename):
    with open(filename, "rb") as file:
        # set cursor at 10 position from begining of file
        # file.seek(10, 0)  # setting the cursor position from begining of file
        # file.seek(10, 1)  # set the cursor position from current position of the cursor
        file.seek(-30, 2)  # set the cursor position from end of the file
        print("start position of cursor :", file.tell())
        print(file.read())


set_different_cursor_position("demo1.txt")
