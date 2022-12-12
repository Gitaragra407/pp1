a = int(input("podaj a:"))
b = int(input("podaj b:"))
for i in range(a):
    print()
    if i == 0 or i == a-1:
        for j in range(b):
            print("*",end="")
    else:
        for j in range(b):
            if j == 0 or j == b-1:
                print("*",end="")
            else:
                print(" ",end="")