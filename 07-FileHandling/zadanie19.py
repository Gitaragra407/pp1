with open('Num1-50.txt','w') as FILE:
    for i in range(1,50):
        FILE.write(str(i)+'\n')
        
    FILE.write('50')