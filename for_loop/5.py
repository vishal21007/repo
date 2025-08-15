var = 7
while var > 0:
    print ('Current variable value: ', var)
    var = var - 1
    if var == 3:
        break
    else:
        if var == 6:
            var = var - 1
            continue
    print ("Good bye!")