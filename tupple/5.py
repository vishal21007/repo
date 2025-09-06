str=[]
tp=(1,2,2,4,4,5,43,4,5,3,2,2,4,3,2,)
for i in tp:
    if i not in str:
        print("Number :",i,"reoucours",tp.count(i),"tymes")
        str.append(i)