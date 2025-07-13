# count number of alphabet and digit
al=0
di=0
str='On a bright morning, Sarah walked 10 miles to reach the old library. She carried 3 books, eager to exchange them for new adventures. The librarian greeted her warmly, offering a cup of tea. After reading for 2 hours, Sarah left, promising to return in exactly 7 days.'
for i in str:
    if i.isalpha():
        al = al +1
    else : 
        if i.isdigit():
            di = di + 1

print(di,"number in string ")
print(al,"character in the str")