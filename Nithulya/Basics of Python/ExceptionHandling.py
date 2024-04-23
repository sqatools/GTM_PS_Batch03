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


#2). Explicit raise exception
def explicit_exception_function():
    try:
        num1 = 20
        num2 = "Hi"
        addition = num1 + num2
        print("Addition :", addition)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")
        raise
    print("Execution successful")

explicit_exception_function()