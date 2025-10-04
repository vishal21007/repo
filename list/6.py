# display sqr of an element, if it is integer.

lst = [10,'fun',40,'few',50,'full']
for i in lst:
    if type(i) == int:
        print(i**2, end =' ')
    else:
        print(i, end = ' ')

print()