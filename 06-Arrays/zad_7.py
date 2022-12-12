lista = [15, 8, 31, 47, 2, 19]
parzyste = 0
Nieparzyste = 0
for i in lista:
    if i%2==0:
        parzyste += 1
    else:
        Nieparzyste += 1
print('Nieparzyste:',Nieparzyste,"Parzyste:", parzyste)