# 9). Python program to check authentication with the given username and password.
user_name = "Thushara"
pass_word = "1234"

name = input("Enter the user name :")
password = input("Enter password :")

if name == user_name and password == password:
    print("Authentication Successful!")
else:
    print("Incorrect user name and password.")