from functools import singledispatch

@singledispatch
def fun(text):
    print('String: ' + text)

@fun.register(int)
def _(text):
    print(text)

@fun.register(list)
def _(text):
    for k, v in enumerate(text):
        print(k, v)

@fun.register(float)
@fun.register(tuple)
def _(text):
    print('float, tuple')

fun('i am is gouzei')
fun(123)
fun(['a', 'b', 'c', 'd'])
fun(1.243)
print(fun.registry)
print(fun.registry[int])