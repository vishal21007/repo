lst = [1,2,3,4,5]

for i in range(len(lst)):
    print(lst[i])
x = int(input('Enter a value'))
lst[2] = x
print(lst[2])

for i in range(len(lst)):
    print(lst[i])