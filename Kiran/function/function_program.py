def greeting():
    print("welcome")
greeting()

# 2
def addition(para1,para2):
    print("addition of parameter1 and parameter2 is : ",para1+para2)

# pass by value
addition(40,50)

# pass by reference
x =30
y =80
addition(x,y)

# change parameter sequence to call
addition(para2 =x , para1 = y )




# calculator program



def calculator(para3,para4):
    print("Please select your operation : \n1 Addition \n2 substraction \n3 division \n4 multiplication ")
    num1 = int(input("Enter output : "))

    if num1==1:
        sum = para3+para4
        print(sum)
    elif num1==2:
        sub = para3-para4
        print(sub)
    elif num1==3:
        div = para3/para4
        print(div)
    elif num1==4:
        multi = para3*para4
        print(multi)
    else:
        print("Invalid Input!!")
num1 = int(input("Enter first no. : "))
num2 = int(input("Enter second no : "))
calculator(num1,num2)




'''



def substraction(n1,n2):
    return n1-n2
def division(n1,n2):
    return n1/n2
def multiplication(n1,n2):
    return n1*n2
def addition(n1,n2):
    return n1+n2

print("Please select your operation : \n1 Addition \n2 substraction \n3 division \n4 multiplication ")
operation = int(input("select input : "))
num1 = int(input("Enter first no. : "))
num2 = int(input("Enter second no : "))
if operation==1:
    print(num1, "+", num2 ,"=", addition(num1,num2))
elif operation == 2:
    print(num1, "-", num2, "=", substraction(num1, num2))
elif operation==3:
    print(num1, "/", num2, "=", division(num1, num2))
elif operation==4:
    print(num1, "*", num2, "=", multiplication(num1, num2))
else:
    print("Invalid Input!!")

'''
