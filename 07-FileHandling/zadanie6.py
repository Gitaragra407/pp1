file = open('countries.txt','r')
file_content = file.read()
file.close()
for line in file_content:
     print(line, end="")