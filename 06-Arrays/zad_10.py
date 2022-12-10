file = open('information.txt','w')
for line in range(4):
    line = str(line)
    line = input(line)
    file.write(line+'\n')
file.close()