def exception_function():
    try:
        num1 = 40
        num2 = "Hello"

        addition = num1 + num2
        print("Addition :", addition)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")

    print("_"*50)

    print("Execution successful")


#exception_function()

# Explicit raise exception
def explicit_exception_function():
    try:
        num1 = 40
        num2 = "Hello"

        addition = num1 + num2
        print("Addition :", addition)
    except Exception as e:
        print(e)
        print("Addition of integer and string is not allowed")
        raise

    print("_"*50)

    print("Execution successful")

explicit_exception_function()


