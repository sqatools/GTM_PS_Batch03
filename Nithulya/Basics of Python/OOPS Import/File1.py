def Addition(num1,num2):
    print('Addition : ',num1+num2)
def Multiplication(num1,num2):
    print('Multiplication : ', num1 * num2)
def Division(num1,num2):
    print('Division : ', num1 // num2)


if __name__=='__main__':
             # If print(__name__),we will get it as (__main__) then only this code will execute.
    Addition(2,3)           # It helps to prevent to execute this code in imported files.
    Multiplication(2,4)
    Division(10,5)