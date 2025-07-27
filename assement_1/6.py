def cone(ra,l):
    return 3.14*ra*l
def c_cyl(ra,he):
    return 3.14*ra*he
def total():
    u_p=int(input("Enter the unit pr miter : "))
    tp=u_p+csa
    print("Total price of the tent is : ",tp)
    total_P=tp+(0.18*tp)
    print("The final amont of tent with tax is : ",total_P)
le=int(input("Enter the l of cone : "))
r=int(input("Enter the radious of cone : "))
h=int(input("Enter the height of the cylinder : "))
csa=c_cone=cone(r,le)+c_cyl(r,h) 
total()