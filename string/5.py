#calculating number of lower case character in string
count = 0 
d_count = 0
u_count = 0
a_count=0
str ='Vishal123'
for i in str:
    if i.islower():
        count = count + 1
    elif i.isupper():
        u_count = u_count + 1
    elif i.isdigit():
        d_count=d_count+1
    elif i.isalpha():
        a_count = a_count + 1

print("Number of lower case characters :",count ,'\nNumber of upper case characters :', u_count)
print('Digit : ',d_count)
print(a_count)