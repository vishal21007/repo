# check if string has vowels, count number of vowels
count=0
str='in this day and age, state of art is not well maintained'
count = 0
for i in str:
    if i in 'aeiou':
        count = count + 1
print("Number of vowles in the string :",count)