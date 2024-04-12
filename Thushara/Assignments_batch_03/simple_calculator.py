# Simple calculator

def addition(num1, num2):
    print(num1+num2)


def subtraction(num1, num2):
    print(num1-num2)


def multiplication(num1, num2):
    print(num1*num2)


def division(num1, num2):
    print(num1/num2)


def cal():
    option = int(input("Enter 1 for addition, 2 for subtraction, 3 for multiplication, 4 for division, 5 to exit :"))
    if option not in (1, 2, 3, 4):
        print("Wrong option")
        exit()
    num1 = float(input("Enter the first number :"))
    num2 = float(input("Enter the second number :"))
    if option == 1:
        addition(num1,num2)
    elif option == 2:
        subtraction(num1, num2)
    elif option == 3:
        multiplication(num1, num2)
    elif option == 4 and num2 !=0:
        division(num1, num2)
    elif option == 4 and num2 == 0:
        print("Division by zero is not defined")
    cal()
