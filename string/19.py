str='hello world'
ch = input("Enter the character wants to be counted : ")
count = 0 
i = 0
while i<=len(str)-1:
    if ch == str[i]:
        count = count + 1
    i = i + 1

print(count)