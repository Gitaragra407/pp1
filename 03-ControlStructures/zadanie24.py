for i in range(1,10):
    print()
    if i < 6:
        for j in range(1,i+1):
            print("*",end="")
    else:
        for j in range(0,10-i):
            print("*",end="")