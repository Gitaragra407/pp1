def sum(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma
def array2str(lista):
    string = ''
    for i in lista:
        i = str(i)
        string += i
        string +=" "
    return string

lista = [4,3,7,1,3]
print('Array:',array2str(lista),'\nSum of Values',sum(lista))