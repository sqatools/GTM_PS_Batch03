def Addition(num1, num2):
    print('Addition:', num1 + num2)


def Multiplication(num1, num2):
    print('Multiplication:', num1 * num2)


def Division(num1, num2):
    print('Division:', num1 // num2)


# If print(__name__),we will get it as (__main__) then only this code will execute.
# It helps to prevent to execute this code in imported files, so we need to use below condition
# if __name__ == '__main__':  cu

if __name__ == '__main__':
    Addition(2, 3)
    Multiplication(2, 4)
    Division(10, 5)
