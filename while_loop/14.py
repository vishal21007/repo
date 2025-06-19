# infinite while loop

while True:
    print('Press 1 : To Enter information')
    print('Press 2 : TO View Information')
    print('Press 3 : Exit')
    ch = int(input('Enter your choice : '))
    if ch == 1:
        print('Enter information')
    elif ch == 2:
        print('View Value ')
    elif ch == 3:
        break
    else:
        print('Invalid Input')