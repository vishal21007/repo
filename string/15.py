#take a string and replace all spaces with hyphen
str =  'hello world, this is a new testing string'

for i in str.split():
    print(i,end='-')
print('')