lis = [{ "name" : "neha", "age" : 21},
{ "name" : "priya", "age" : 20 },
{ "name" : "sunny" , "age" : 19 }]

lis.sort(key = lambda i: i['age'])
print(lis)

lis = [{ "name" : "neha", "age" : 21},
{ "name" : "priya", "age" : 20 },
{ "name" : "sunny" , "age" : 19 }]

print(sorted(lis, key = lambda i: i['age']))
