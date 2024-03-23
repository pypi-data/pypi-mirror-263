import inspect

def my_function2():
    # Use inspect.currentframe() to get the current frame,
    # and f_code.co_name to get the code object's name
    print(inspect.currentframe().f_code.co_name)

my_function2()
