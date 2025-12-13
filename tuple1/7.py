# create a tuple and delete random values using random module.

import random
tup = (1,2,3,4,5,6,7,8,9,10)

lst = list(tup) # type casting into list.

#removing index values from list using random module
for i in range(4):
    c=random.randrange(0,9)
    lst.pop(c)

# type casting list to tuple & printing tuple values
tup = tuple(lst)
print(tup)
