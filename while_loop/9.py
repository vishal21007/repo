'''
print in reverse : hello world
'''

x = input('ENter a string !')
i = len(x) - 1
while i>=0:
    print(x[i], end=' ')
    i = i - 1
print('')