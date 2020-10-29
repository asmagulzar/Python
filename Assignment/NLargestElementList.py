a=[3,4,1,2,5,6]
#3,4,1,2,5,6
n = int(input("Enter N:"))

for i in range(0,n):
    max = 0
    for j in range(0,len(a)):
        if(a[j]>max):
            max=a[j]
    print(max,end = " ")
    a.remove(max)


