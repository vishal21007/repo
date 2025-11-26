"""Generate Random Password : Write a code to generate a random password which meets the
 following conditions.

    Password length must be 10 characters long.
    It must contain at least 2 upper case letters, 1 digit, and 1 special symbol."""
import random
lst=["!","@","#","$","%","^","&","*"]
for i in range(2):
    s=random.randrange(0,8)
    
    for j in range(2):
        s1=random.randrange(65,91)
        print(chr(s1),end="")
    s2=random.randrange(97,123)
    print(chr(s2),end="")
    print(s,end="")
    print(lst[s],end="")
    