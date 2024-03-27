####### For Loop #####

#1.
# for i in range(1,11):
#     print(i,end=' ')    # 1 2 3 4 5 6 7 8 9 10

#2.
# list1=['Amy','Anna','Colleen','Faith','Nicky']
# for i in list1:
#     print(i,end=' ')   #Amy Anna Colleen Faith Nicky

#3.
# char1= 'WELCOME'
# for i in char1:
#     print(i,end=' ')   # W E L C O M E

#4.
# for i in range(65,91):
#     print(chr(i),end=' ')   # A B C D E F G H I J K L M N O P Q R S T U V W X Y Z

#5.
# for i in range(97,123):
#     print(chr(i),end=' ')  # a b c d e f g h i j k l m n o p q r s t u v w x y z


#### While ####
#1.
# num = 2
# while num <= 20:
#     print(num, end=' ')
#     num += 2                  # 2 4 6 8 10 12 14 16 18 20

#2. Run infinite while loop
# num=1
# while True:
#     print(num,end=' ')
#     num += 1
#     if num == 31:
#         break              # 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30

#3. Write a python program for simple calculator
# while True:
#     print("Please select the math option to run\n"
#           "1.  Addition\n"
#           "2.  Multiplication \n"
#           "3.  Division \n"
#           "4.  Subtraction\n"
#           "5.  Stop calculator")
#
#     oprs_num = int(input("Please enter the operation number :"))
#     if oprs_num <=4:
#         num1 = int(input("Please enter the num1 value :"))
#         num2 = int(input("Please enter the num2 value :"))
#
#     if oprs_num == 1:
#         print("Addition :", num1+num2)
#     elif oprs_num == 2:
#         print("Multiplication :", num1*num2)
#     elif oprs_num == 3:
#         print("Division :", num1//num2)
#     elif oprs_num == 4:
#         print("Subtraction :", num1-num2)
#     elif oprs_num == 5:
#         print("Thanks for using calculator !! closing ...")
#         break

#(OR)
while True:
    choice = int(input('Enter the choice 1.Addition, 2.Substraction 3.Multiplication 4.Division : '))
    value1 = int(input("Enter the value1 : "))
    value2 = int(input("Enter the value2 : "))
    if choice==1:
        valuea=value1+value2
        print("Addition : ",valuea)
    elif choice==2:
        valueb=value1-value2
        print("Substraction : ",valueb)
    elif choice==3:
        valuec=value1*value2
        print("Multiplication: ",valuec)
    elif choice==4:
        valued=value1/value2
        print("Division : ",valued)
    else:
        print("Please choose correct choice, it is invalid")


