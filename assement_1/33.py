lst = [10, 'fun', 20, 'World', 30, 'home']
for i in lst:
    if type(i) == int:
        print(i**2,end=" ")
    else:
        print(i,end=" ")
print()