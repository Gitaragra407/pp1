
lista1 = [4,36,12,28,9,44,5]
lista2 = [5,1,36]
checkTimes = len(lista2)
for i in lista1:
    check = checkTimes
    for j in lista2:
        if i != j:
            check -= 1
        if check == 0:
            print(f'This value is not in the 2nd list {i}')      