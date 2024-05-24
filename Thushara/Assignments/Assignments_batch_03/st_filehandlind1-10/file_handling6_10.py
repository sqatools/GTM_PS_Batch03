# 6). Python file program to get a specific line from the file.
def specific_line(a):
    with open('sqatools6','r') as file:
        data = file.readlines()
        if a < len(data):
            s_line= data[a]
            return s_line
        else:
            print("Exceeds limit")

sl =specific_line(5)
print(sl)



# 7). Python file program to get odd lines from files and append them to separate files.
even_lines=[]
with open("sqatools6",'r') as file1:
    data = file1.readlines()
    for i  in range(1,len(data)):
        if i%2 == 0:
            even_lines.append(data[i])
        else:
            continue
for l in even_lines:
    print(l)


# 8). Python file program to read a file line by line and store it in a list.

store_list=[]
with open("sqatools6",'r') as file1:
    data = file1.readlines()
    for i  in range(1,len(data)):
        store_list.append(data[i])


print(store_list)


# 9). Python file program to find the longest word in a file.
l_word = 1
longest_word = ""
with open("sqatools6",'r') as file2:
    data = file2.readlines()
    for line in data:
        for word in line.split(" "):
            if len(word) > l_word:
                l_word = len(word)
                longest_word = word
            else:
                continue
print("The longest word :", longest_word)


# 10). Python file program to get the count of a specific word in a file.


s_word =''
def count_of_specific_word(s_word):
    count=1
    with open("happy.txt",'r') as file:
        data =file.readlines()
        for lin in data:
            for word in line.split(" "):
                if word == s_word:
                    count += 1
                else:
                    continue
    return count
c = count_of_specific_word('life')
print("count of the word life:",c)
