sy=["!","@","#","$","%","^","&","*"]
for i in range(3):
    import random
    nu=random.randrange(0,10)
    s=random.randrange(0,8)
    up=random.randrange(65,91)
    lo=random.randrange(97,123)
    print(str(nu),end="")
    print(sy[s],end="")
    print(chr(up),end="")
    print(chr(lo),end="")