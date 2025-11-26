"""Generate Random String of 20 characters, including space after every 5 character."""

for i in range(20):
    import random
    s=random.randrange(65,91)
    if i%5==0:
        print(" ",end="")
    else:
        print(chr(s),end="")