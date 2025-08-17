str=input("Enter a string : ")
vowel='aeiou'
cou=0
for i in range(len(str)):
    if str[i] in vowel:
        print("*",end=" ")
    else:
        print(str[i],end=" ")
print()