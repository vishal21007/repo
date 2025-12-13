"""add new elements in lst, also extend by 3 values"""
lst=[1,2,3,4,5,6,7]
a=int(input("Enter new element : "))
lst.append(a)
b=int(input("Enter a new element : "))
lst.append(b)
lst1=[8,9,0]
lst.extend(lst1)
print(lst)