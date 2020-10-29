a = [1,2,3]
n = int(input("Enter N:"))
mul=1
for i in range(0,len(a)):
    mul =mul * a[i]
print(mul%n)


