colours = ['Green','Yellow','Orange','Black','Blue','Red','Brown','White','Silver']
txtFile = open('colours.txt','w')
for i in colours:
    i += '\n'
    txtFile.write(i)
txtFile.close()