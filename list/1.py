lst_len=int(input("Enter the length of list : "))
lst=[None]*lst_len
for i in range(lst_len):
    lst[i]=input("Enter a value : ")
print(lst)  # printing list value

lst_in=input("Enter value to be searched in list : ")
flag = 0 # false

for i in range(len(lst)): # range helps in finding index value
    if lst[i] == lst_in:
        print('Value : ',lst_in,'is present at position : ',i+1)
        flag = 1 # value found, so updating flag value
        break
if not flag:
    print('Value not in list !')