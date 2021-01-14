x = ['hello', 'world', 'ni']
x.sort(key=len)
print(x)

from functools import cmp_to_key
ll = [9, 2, 23, 1, 2]
print(sorted(ll, key=cmp_to_key(lambda x, y: y - x)))
print(sorted(ll, key=cmp_to_key(lambda x, y: x - y)))
