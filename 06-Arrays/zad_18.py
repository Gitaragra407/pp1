lista1 = [4,36,13,28,9,44,5,2,12,10,23,92,22,20]
def bubbleSort(lista,direction): #Funkcja sortująca, która sortuje algorytmem bombelkowym. Przyjmuje dwa arguemtny, litę do posortowania i kolejność sortowania. Może być rosnąca asc lub malejaca desc
    bufor = 0
    for i in range(len(lista)): #Iterujemy tyle razy ile mamy komurek w tablicy
        if direction == 'asc':
            for j in range(len(lista)-1):
                if lista[j]>lista[j+1]:
                    bufor = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = bufor
        elif direction == 'desc':
            for j in range(len(lista)-1):
                if lista[j]<lista[j+1]:
                    bufor = lista[j]
                    lista[j] = lista[j+1]
                    lista[j+1] = bufor
        else:
            return 'Wrong direction'
    return lista

print(bubbleSort(lista1, 'desc'))