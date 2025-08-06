def mein(lst):
    print(lst)
    count=0
    for i in lst:
        count = count + i
        me = count/(len(lst))
    print(me)



#main menu
lst=[1.5,2.5,3.5,4.5,5.5,6.5,7.5]
mein(lst)