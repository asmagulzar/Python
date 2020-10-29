num = int(input("Enter a number: "))
order = len(str(num))
sum = 0

temp=num
while temp>0:
    n = temp%10
    sum += (n**order)
    temp = int(temp/10)

if sum == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")






