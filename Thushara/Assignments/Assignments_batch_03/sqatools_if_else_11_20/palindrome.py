# 16). Python program to check whether any given number is a palindrome.
num = input("Enter a number :")
rev_num = num[::-1]
print("The reverse number :", rev_num)
if num == rev_num:
    print("The number is a palindrome number")
else:
    print("Not palindrome")