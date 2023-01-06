Lcounter = 0
with open("LINES.txt") as FILE:
    for line in FILE:
        if Lcounter%5 == 0:
            input()
        print(line,end='')
        Lcounter += 1
        