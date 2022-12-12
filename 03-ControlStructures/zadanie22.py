for i in range(1,31):
    if i %5 ==0 and i % 3==0:
        print("Bingo")
    elif i %5==0:
        print("FIVE")
    elif i %3 ==0:
        print("THREE")
    else:
        print(i)