# 17). Python program to check if any given string is palindrome or not.
# Input: ‘jaj’

str = 'jaj'
rev_str = str[::-1]
print("The reverse of the string :", rev_str)
if str == rev_str:
    print("The given string is a palindrome")