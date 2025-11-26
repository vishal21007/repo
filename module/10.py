"""Write a code to generate 100 random lottery tickets (of 8 digits each) and 
pick two lucky tickets from it as a winner."""
lst=[]
for i in range(100):
    import random
    s=random.random()
    lst.append(int(s*100000000))
s1=random.randrange(0,100)
print("The lucky lottery number is:",lst[s1])