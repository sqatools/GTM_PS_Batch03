
# #1.Write a python program to reverse a number.
# num=123
# reverse_string=0
# num1=num%10
# reverse_string=reverse_string*10+num1
# print('reverse_string : ',reverse_string)
#
# num= num//10
# print('reverse_string : ',num)
# num1=num%10
# print('reverse_string : ',num1)
# reverse_string=reverse_string*10+num1
# print('reverse_string : ',reverse_string)
#
# num= num//10
# print(num)
# num1=num%10
# reverse_string=reverse_string*10+num1
# print('reverse_string : ',reverse_string)

#2.
num = 3210567
rev_result = 0

while num > 0:
    num1 = num%10
    #print("num1 =", num1)
    rev_result = rev_result*10 + num1
    #print("reverse result :", rev_result)
    num = num//10

print("reverse result :", rev_result)