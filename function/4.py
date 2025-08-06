#remove duplicate values in function 

def dup(l):
    lst1 = []
    for i in l:
        if i not in lst1:
            lst1.append(i)
    
    print('New list removing the duplicate value : ',lst1)

# main program
length_lst = int(input('Enter the length of list: '))
lst = []
for i in range(length_lst):
    value = int(input('Enter value: '))
    lst.append(value)

print('List Value:', lst)
dup(lst)