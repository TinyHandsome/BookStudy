from functools import wraps

def wrap1(func):
    # 去掉就会返回inner
    @wraps(func)
    def inner(*args):
        print(func.__name__)
        return func(*args)
    return inner


@wrap1
def demo():
    print('Hello World!')

print(demo.__name__)        # demo