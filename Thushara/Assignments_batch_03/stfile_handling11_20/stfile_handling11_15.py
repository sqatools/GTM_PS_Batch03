# 11).  Python file program to read a random line from a file.

import random
#lines = open('happy2.txt').read().splitlines()
f = open('happy2.txt','r')
lines = f.read().splitlines()
data=random.choice(lines)
print(data)
f.close()


print("$"*50)

# 13). Python file program to copy the file’s contents to another file after converting it to uppercase.

def uppercase_file(file_name):
    with open(file_name,'r')as file:
        with open("changed_to_uppercase.txt", 'w') as f:
            data = file.read().splitlines()
            for line in data:
                print(line)
                line = line.upper()
                f.writelines(line)


uppercase_file('happy2.txt')

with open ("changed_to_uppercase.txt",'r') as f2:
    data = f2.readlines()
    print(data)



#uppercase_file('happy2.txt')

print("@"*50)
# 14). Python file program to count all the words from a file.

def word_count(file_name):
    count=0
    with open(file_name,'r')as file:
        data = file.readlines()
        for line in data:
            for word in line.split():
                count += 1
    return count

c= word_count('happy2.txt')
print("The count of all words in the given file :", c)

# 15). Python file program to sort all the lines File as per line length size.



with open('happy2.txt','r')as file:
    data = file.readlines()
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if len(data[i]) > len(data[j]):
                temp = data[i]
                data[i] = data[j]
                data[j] = temp
            else:
                continue


with open('sort_content.txt', "w") as file:
    all_lines = ''.join(data)
    file.write(all_lines)

with open('sort_content.txt', "r") as file1:
    data = file1.read().splitlines()
    for line in data:
        print(line)


