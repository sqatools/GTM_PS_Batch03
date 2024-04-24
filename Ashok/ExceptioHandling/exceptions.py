# Exceptions: 1. Syntax error 2. Logical error 3. Run time error

# Index error: Below example is run time error
# k = [10, 20, 20, 40, 50]
# index = int(input("Enter a index:"))
# print(k[index])  # Enter out of index range number then it shows IndexError: list index out of range

# Value or Type error
# val = int('abc')
# print(type(val))  # ValueError: invalid literal for int() with base 10: 'abc'

# Key error:
# d = {1: 'abc', 2: 'cde', 3: 'fgh'}
# key = int(input("Enter a key"))
# print(d[key])

# Zero division error:
# a, b = 10, 0
# res = a/b
# print(res)

"""
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.

Summary:
Try block will check for exceptions, if any exception occurs then except block will execute.
Else block will execute when there is no exception in try block. Finally block executes whether exception
occurs or not it will execute.
"""


# 1.
# k = [10, 20, 30, 40, 50]
# try:
#     index = int(input("Enter a index:"))
#     print(k[index])
# except:
#     print("Invalid Key")
# print("Terminated successfully")

# 2.
# here x i nor defined #
# try:
#     print(x)
# except:
#     print("An exception occurred")

# 3. Without try block - Below example will raise NameError: name 'x' is not defined
# print(x)

# 4. You can define as many exception blocks as you want, e.g. if you want to execute a special block of
# code for a special kind of error:
# try:
#     print(x)
# except NameError:
#     print("Variable x is not defined")
# except:
#     print("Something else went wrong")

# 5. You can use the else keyword to define a block of code to be executed if no errors were raised:
# try:
#   print("Hello")
# except:
#   print("Something went wrong")
# else:
#   print("Nothing went wrong")

# 6. The finally block, if specified, will be executed regardless if the try block raises an error or not.
# Ex: file.close() - We can write this code in finally block, because if you read/write or not but the file
# should be closed.

# try:
#     print(x)
# except:
#     print("Something went wrong")
# finally:
#     print("The 'try except' is finished")

# 7. Raise Keyword: The raise keyword is used to raise an exception. You can define what kind of error to raise,
# and the text to print to the user

# x = "hello"
#
# if not type(x) is int:
#     raise TypeError("Only integers are allowed")

# 8.
# def exception_function():
#     try:
#         num1 = 40
#         num2 = "Hello"
#         addition = num1 + num2
#         print("Addition :", addition)
#     except Exception as e:
#         print(e)
#         print("Addition of integer and string is not allowed")


# exception_function()

# 9.
# def try_except_else(x, y):
#     try:
#         num1 = x
#         num2 = y
#         print("Division :", num1 // num2)
#
#     except Exception as e:
#         print(e)
#         print("division by zero is not valid operation")
#     else:
#         # This else part will only execute if there is no exception
#         print("division operation is successful")


# try_except_else(40, 5)
# try_except_else(40, 0)

# 10. Single try block with multiple exceptions blocks
# def handle_multiple_exception(num1, num2, num3):
#     try:
#         addition = num1 + num2
#         print("addition  :", addition)
#
#         multiplication = num1 * num2
#         print("multiplication :", multiplication)
#
#         division = num1 // num2
#         print("division :", division)
#
#         assert num1 == num2
#     except TypeError:
#         print("Addition of integer and string is not allowed")
#     except ZeroDivisionError:
#         print("Division of number with zero is not allowed")
#     except Exception as e:
#         raise


# handle_multiple_exception(50, "abc", 30)  # executes the Type error block
# handle_multiple_exception(50, 0, 30)  # executes the ZeroDivisionError block
# handle_multiple_exception(50, 10, 30)  # executes the Exception block

# 11. Nested exception handling
# def nested_exception_handling(num1, num2):
#     try:
#         addition = num1 + num2
#         print("addition:", addition)
#         try:
#             division = num1 // num2
#             print("division :", division)
#         except Exception as e:
#             # print(e)
#             print("Divide by zero is not allowed")
#
#     except Exception as e:
#         print(e)
#         print("Both the values should be integer")


# nested_exception_handling(30, 2)  # No Error
# nested_exception_handling(30, 'Hello')  # outer exception will execute
# nested_exception_handling(15, 0)  # inner exception will execute

# Custom Exceptions #
class CustomError(Exception):
    """This is a custom exception class"""

    def __init__(self):
        print("Raising the custom exception with condition")


# def raise_custom_exception():
#     for i in range(20):
#         if i == 14:
#             raise CustomError()
#         else:
#             print(i)
#
#
# raise_custom_exception()

# Different exceptions:
# try:
#     print("Hi")
# except ArithmeticError as e:
#     print(e)
# except AssertionError as e1:
#     print(e1)
# except AttributeError as e2:
#     print(e2)
# except Exception as e3:
#     print(e3)
# except:
#     print("Invalid text")


