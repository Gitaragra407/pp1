<<<<<<< HEAD
lista = [15, 8, 31, 47, 2, 19]
parzyste = 0
Nieparzyste = 0
for i in lista:
    if i%2==0:
        parzyste += 1
    else:
        Nieparzyste += 1
print('Nieparzyste:',Nieparzyste,"Parzyste:", parzyste)
=======
file = open('countries.txt','r')
file_content = file.read()
file.close()
i = 1
for line in file_content:
     print( i, line, end="")
     i+=1
>>>>>>> 6d0eb2c33f85117fd03033eb20df61ff30915065
