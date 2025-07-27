#program to calualt payable amount of tent 
def csa_con(r, l):
    return 3.14*r*l

def csa_cylind(r,h):
    return 2*3.14*r*h

def total_price(area):
    up=int(input("Enter the price of tent pr/unit : "))
    t_p=up*area
    print("Total price =",int(t_p))
    total_price=t_p+(0.18*t_p)
    print("Final price with GST =",int(total_price))

# main program

le=int(input("Enter the slant height : "))
rad=int(input("Enter the radious : "))
cyl_hei=int(input("Enter the height of the cylender : "))

canvas_area = csa_con(rad,le) + csa_cylind(rad,cyl_hei)

total_price(canvas_area)