# string - str='hello world'
# string_var.lower()/upper()
# string_var.isupper()/islower() - T/F

from ctypes import string_at


str = 'hello world'
count = 0
# using loop, count number of lower cases in the string
for i in str:
    if i.islower():
        count = count + 1
print(count)

if 'h' in 'hello world':
    print('True')