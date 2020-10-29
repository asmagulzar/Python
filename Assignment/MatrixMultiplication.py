a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
c = []

for i in range(0,len(a)):
    c.append(a[i] * b[i])

print(c)