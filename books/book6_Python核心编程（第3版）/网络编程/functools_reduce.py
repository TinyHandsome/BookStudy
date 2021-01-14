from functools import reduce

l = range(1, 10)
print(reduce(lambda x, y: x+y, l))      # 45

