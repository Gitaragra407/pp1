from random import randrange
with open("50Number.txt",'w') as FILE:
    for i in range(50):
        FILE.write(str(randrange(100,1000))+'\n')