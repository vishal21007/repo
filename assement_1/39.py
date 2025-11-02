# if a string is encountered - print as it is, if number is encountered - print sq of number
# expected output - ['abc', 4, 'bat', 16, 'cat', 36]

lst = ['abc', 2, 'bat', 4 , 'cat', 6]
for i in lst:
    if type(i)==int:
        print(i**2,end=" ")
    else:
        print(i,end=" ")