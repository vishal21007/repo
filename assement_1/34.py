lst = [1, 2, 3, 4, 5, 6, 7]
print(lst)
last_val = len(lst)-2

lst[1], lst[last_val] = lst[last_val],lst[1]
print(lst)