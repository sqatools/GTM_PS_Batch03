"""
global variable : The variable that can access by every function of the module.
local variable : The variable which we declare on function level and can be access inside the function.
                scope is limited to function
non-local variable: The variable we declare in the outer function, and it is available to access all the
               inner functions, then it is known as non-local variable.
"""

# global variable
var_global = 500


def function_1():
    print("Global Variable is:", var_global)
    var_local1 = 300  # local variable
    var_local2 = 400  # local variable
    print("Local Variable1 is:", var_local1)
    print("Local Variable2 is:", var_local2)


def function_2():
    print("Global Variable is:", var_global)


function_1()
function_2()

# Modifying the global variable in inner functions #
var_x = 600  # global variable


def outer_function():
    var_y = 700  # non local variable

    def inner_function1():
        global var_x  # Using global keyword we can modify the global variable in inner functions
        nonlocal var_y  # Using non-local keyword we can modify the non-local variable in inner functions
        var_z = 800
        var_x = 900
        var_y = 1000
        print("Global var_x:", var_x)  # 900
        print("Nonlocal var_y:", var_y)  # 1000
        print("local var_z:", var_z)  # 800

    def inner_function2():
        var_a = 1100  # local variable
        print("Global var_x:", var_x)  # 900
        print("Nonlocal var_y:", var_y)  # 1000
        print("local var_a:", var_a)  # 800

    inner_function1()
    inner_function2()


outer_function()
