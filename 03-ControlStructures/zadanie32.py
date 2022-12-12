for i in range(1,8):
    print()
    iterator = i
    for j in range(7):
        if j ==0:
            print(i,end=" ")
        else:
            iterator+=7
            if iterator == 8 or iterator == 9:
                print(end=" ")
            print(iterator,end=" ")