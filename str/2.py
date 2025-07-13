count = 0
vowel = 'aeiouAEIOU3'
str =input("Enter a string : ")
for i in str.lower():
    if i in vowel:
        count = count +1
print(count,'vowels in the str')
