from functools import partial

def add(a, b):
    return a+b

addOne = partial(add, 10)
print(add(1, 2))
# 3
print(addOne(1))
# 11