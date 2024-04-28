def Addition(num1,num2):
    print('Addition : ',num1+num2)
def Multiplication(num1,num2):
    print('Multiplication : ', num1 * num2)
def Division(num1,num2):
    print('Division : ', num1 // num2)


if __name__ == '__main__':              # If __name__ == '__main__' then only it will execute. If you print(__name__),we will get (__main__)
    Addition(2,3)
    Multiplication(2,4)
    Division(10,5)