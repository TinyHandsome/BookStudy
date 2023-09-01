from functools import update_wrapper
def wrapper(f):
    def wrapper_function(*args, **kwargs):
        """这个是修饰函数"""
        return f(*args, **kwargs)
    return wrapper_function

@wrapper
def wrapped():
    """这个是被修饰的函数"""
    print('wrapped')

print(wrapped.__doc__)      # 这个是修饰函数
print(wrapped.__name__)     # wrapper_function

def wrapper2(f):
    def wrapper_function2(*args, **kwargs):
        """这个是修饰函数"""
        return f(*args, **kwargs)
    update_wrapper(wrapper_function2, f)
    return wrapper_function2

@wrapper2
def wrapped2():
    """这个是被修饰的函数"""
    print('wrapped')

print(wrapped2.__doc__)      # 这个是被修饰的函数
print(wrapped2.__name__)     # wrapped2