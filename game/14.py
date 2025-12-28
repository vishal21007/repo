"""
Monster v/s player
"""
import random
pyr=100
mon=100
r=0
while True:
    p=random.randrange(10,31)
    m=random.randrange(5,26)
    pyr=pyr-m
    mon=mon-p
    r=r+1
    print("***Round ",r)
    print("-----------------")
    print("Player Attacks Monster for **",p,"**Damage")
    print("Monster Attacks Player for **",m,"**Damage")
    print("Players : **",pyr,"** HP")
    print("Monster : **",mon,"** HP")
    ch=input("Do you want to attack again : y/n ")
    if pyr <= 0 or mon <=0:
        break
    
print('Game finished !')
if pyr>mon:
    print("***Game Over***")
    print("  Player Wins ")
elif pyr<mon:
    print("***Game Over***")
    print("  Monster Wins  ")