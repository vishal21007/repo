"""wap to count the no. of times a character appears in a i given stng and store character and its value in fornamt 
key : value """
str="hello world"
dic={}
for i in str:
    str.count(i)
    if i not in dic:
        dic[i]=str.count(i)
    else:
        continue
print(dic)