def add(a,b):
    return lambda c: a + b + c
sum = add(5,7)
print(add(5,7))
print(sum(3))



add = lambda x, y: x + y
print(add(5,5))