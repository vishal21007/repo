# delete character from string and print output

str = input('Enter a string : ')
val = input('Enter character to delete from string : ')

for i in str :
    if val == i:
        continue
    else:
        print(i, end = ' ')
print('')