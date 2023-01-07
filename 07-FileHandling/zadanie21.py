with open('powers.txt','w') as FILE:
    for i in range(1,11):
        FILE.write(str(i)+','+str(i**2)+','+str(i**3)+'\n')