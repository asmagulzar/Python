str = input("Enter String:")

words = str.split()

for word in words:
    print(word[::-1], end = " ")
    #print("".join(reversed(word)),end = " ")
