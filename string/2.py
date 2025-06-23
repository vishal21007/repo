# wap to count number of 'l' in a string.

count=0
str='hello world'

for i in str:
    if i == 'l':
        count= count + 1
print('Number of l in string is : ',count)
