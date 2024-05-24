#  2). Python file program to overwrite the existing file content.
def read_a_file(filename):
    with open(filename,'a') as f:
        f.write("Hello")
        with open(filename, 'r') as file:
            data = file.readlines()
            return data

d1 = read_a_file('test_data.txt')
print(d1)