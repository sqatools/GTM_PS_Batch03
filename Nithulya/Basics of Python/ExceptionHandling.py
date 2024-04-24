#1).
# def exception_function():
#     try:
#         num1 =30
#         num2='Hi'
#         addition = num1+num2
#         print("Addition : ",addition)
#     except Exception as e:
#         print(e)
#         print("Addition of integer and string is not allowed")
#
#     print("Execution successful")
# exception_function()


#2). Explicit raise exception #################################################################
# def explicit_exception_function():
#     try:
#         num1 = 20
#         num2 = "Hi"
#         addition = num1 + num2
#         print("Addition :", addition)
#     except Exception as e:
#         print(e)
#         print("Addition of integer and string is not allowed")
#         raise
#     print("Execution successful")
#
# explicit_exception_function()

#3). try - except - else ##########################################################################
# def try_except_else(x, y):
#     try :
#         num1 = x
#         num2 = y
#         print("Division :", num1//num2)
#
#     except Exception as e:
#         print(e)
#         print("Division by zero is not valid operation")
#     else:
#         print("Division operation is successful")

# try_except_else(20, 10)
# try_except_else(20, 0)


#4). try - except - else - finally ##################################################################
# finally : Finally section code always going to execute if whether there is exception or no exception.

# def try_except_else_finally(x, y, z):
#     try :
#         num1 = x
#         num2 = y
#         print("Division :", num1//num2)
#
#     except Exception as e:
#         print(e)
#         print("Division by zero is not valid operation")
#     else:
#         print("Division operation is successful")
#     finally:
#         for i in range(1, 11):
#             print(i, "*", z, ":", i*z)
#
# # try_except_else_finally(20, 10, 5)
# try_except_else_finally(20, 0, 5)


#5). Handle multiple exception ###################################################################################
# def handle_multiple_exception(num1, num2):
    # try:
    #     addition = num1 + num2
    #     print("Addition  :", addition)
    #
    #     multiplication = num1 * num2
    #     print("Multiplication :", multiplication)
    #
    #     division = num1 // num2
    #     print("Division :", division)
    #
    #     assert num1 == num2
    # except TypeError:
    #     print("Addition of integer and string is not allowed")
    # except ZeroDivisionError:
    #     print("Division of number with zero is not allowed")
    # except AssertionError:
    #     print("Both numbers are not equal")
    # except Exception as e:
    #     print(e)


# handle_multiple_exception(50, 10)
# handle_multiple_exception(50, 0)
# handle_multiple_exception(50, 50)

#6). Nested exception Handling ##########################################################################
# def nested_exception_handling(num1, num2):
#     try:
#         addition = num1 + num2
#         print("Addition:", addition)
#         try:
#             division = num1//num2
#             print("Division :", division)
#         except Exception as e:
#             #print(e)
#             print("Divide by zero is not allowed")
#
#     except Exception as e:
#         print(e)
#         print("Both the values should be integer")


# nested_exception_handling(20, 10)
# nested_exception_handling(30, 'Hello')
# nested_exception_handling(15, 0)


# 7). Custom exception ############################################################################
# class CustomError(Exception):
#     """This is custom exception class"""
#     def __init__(self):
#         print("Raising the custom exception with condition")
#
# def raise_custom_exception():
#     for i in range(20):
#         if i == 14:
#             raise CustomError()
#         else:
#             print(i)
#
#
# raise_custom_exception()


# List of all possible errors and exceptions
"""
ArithmeticError
OverflowError
ZeroDivisionError
FloatingPointError
BufferError
LookupError
AssertionError
AttributeError
 EOFError
GeneratorExit
 ImportError
ModuleNotFoundError
 IndexError
KeyError
MemoryError
NameError
NotImplementedError
OSError(
RecursionError
ReferenceError
RuntimeError
StopIteration
 SyntaxError
SystemError
SystemExit
TypeError
UnboundLocalError
UnicodeError
ValueError
"""
