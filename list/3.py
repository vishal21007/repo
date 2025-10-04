# Linear Search Implementation

lst=[10,51,2,18,4,31,13,5,23,64,29]
print(lst)
val = int(input("Enter the element you want to search : "))
count = 0
flag = False
'''
if n in lst:
    print(lst.index(n)+1)
else:
    print("Invalid input!!!")
'''
for i in lst:
    count = count + 1
    if val == i:
        print('Value : ',val,'present at : ',count)
        flag = True
if flag == False:
    print('Value not in list!')