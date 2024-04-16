# Home work :
# 1. write a python program Replace file content JAVA with PYTHON.
# 2. write a python program to get all the email id from given file.
# 3. Write a python program to get all the phone number from given file.

with open("file_replace.txt", "w") as f:
    f.write("JAVA is one of the most popular programming languages in software development. \n"
                 "JAVA is an interpreted, object-oriented,and high-level programming language "
                 "with dynamic semantics. ")
with open("file_replace.txt", "r") as f:
    data1 = f.readlines()
    for line in data1:
        print(line)

with open ("file_replace.txt", "r") as f1:
    with open("file_replace1.txt", "a") as f2:
        data = f1.readlines()
        for line in data:
            line = line.replace("JAVA", "Python")
            f2.write(line)

with open("file_replace1.txt", "r") as f:
    data1 = f.readlines()
    for line in data1:
        print(line)

with open("profile.txt","w")as f1:
    f1.writelines("Name: Anu, Phone : 1246457897 , email: anu@gmail.com "
                  "Name: Ami ,Phone : 3546465465  , email : ami@gmail.com "
                  "Name: Aarav, Phone : 6575765  , email : arav@gmail.com "
                  "Name: Lya, Phone : 7675765 , email: lya@gmail.com ")
num_lst=[]
e_mail=[]
with open ("profile.txt", "r")as f2:
    data =f2.readlines()
    print(data)
    for line in data:
        for word in line.split():
            if word.isnumeric() and len(word) == 10:
                num_lst.append(word)
    print("List of phone numbers")
    print("-"*50)
    print(num_lst)

    for line in data:
        for word in line.split(" "):
            if '@' in word:
                e_mail.append(word)
    print("List of e_mails")
    print("-" * 50)
    print(e_mail)









