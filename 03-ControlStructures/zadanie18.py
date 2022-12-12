PLN = int(input("Podaj liczbę złotych"))
PLN5 = 0
PLN2 = 0
PLN1 = 0
while PLN >= 5:
    PLN5+= 1
    PLN -= 5
while PLN >= 2:
    PLN2+= 1
    PLN -= 2
while PLN >= 1:
    PLN1+= 1
    PLN -= 1
print("The amount of PLN 18 in coins:")
print("5 zł - ",PLN5)
print("2 zł - ",PLN2)
print("1 zł - ",PLN1)