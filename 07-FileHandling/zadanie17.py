data = []
with open("cars.txt") as FILE:
    for line in FILE:
        data.append(line)
with open('copy.txt','w') as FILE:
    for i in data:
        FILE.write(i)
