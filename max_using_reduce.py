from functools import reduce

l = [34, 67, 23, 67, 908, 43, 23, 3, 23]
a = reduce(max, l)
print(a)
