file = open('countries.txt','r')
file_content = file.read()
file.close()
i = 1
for line in file_content:
     print( i, line, end="")
     i+=1