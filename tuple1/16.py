"""
Dice Frequency Analyzer
"""
import random
dic={}
lst=[]
for i in range(20):
    d=random.randrange(1,7)
    lst.append(d)
for i in lst:
    if i not in dic:
        dic[i]=lst.count(i)
 
print("**Dice Frequency Table**")
print("------------------------")
print("1: ",dic[1]*"*","( ",dic[1]," Times )")
print("2: ",dic[2]*"*","( ",dic[2]," Times )")
print("3: ",dic[3]*"*","( ",dic[3]," Times )")
print("4: ",dic[4]*"*","( ",dic[4]," Times )")
print("5: ",dic[5]*"*","( ",dic[5]," Times )")
print("6: ",dic[6]*"*","( ",dic[6]," Times )")
print()
print("**Forecast (Relative Frequencies)**")
print("-----------------------------------")
print("1: ",(dic[1]/20)*100,"%","chance ( Based on past 20 rolls )")
print("2: ",(dic[2]/20)*100,"%","chance ( Based on past 20 rolls )")
print("3: ",(dic[3]/20)*100,"%","chance ( Based on past 20 rolls )")
print("4: ",(dic[4]/20)*100,"%","chance ( Based on past 20 rolls )")
print("5: ",(dic[5]/20)*100,"%","chance ( Based on past 20 rolls )")
print("6: ",(dic[6]/20)*100,"%","chance ( Based on past 20 rolls )")