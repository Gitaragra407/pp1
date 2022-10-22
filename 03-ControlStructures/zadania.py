"""
x = int(input("podaj liczbę"))
if x%2==0:
    print("liczba jest przysta")
else:
    print("liczba jest nie parzysta")

paul = int(input("wiek paula"))
annie = int(input("wiek annie"))
if paul >= 18 and annie >= 18:
    print("paula i annie mają 18 lat")
else:
    print("ktoś nie ma 18 lat")
a = float(input("podaj liczbę pierwszą"))
b = float(input("podaj liczbę drugą"))
if b > 0 or a > 0:
    print("jedna z liczba jest dodatnia")
else:
    print("liczba druga nie jest większa od zera")
"""
for x in range(5):
    print("practice makes perfect")
for y in range(1,21):
    print(y)
suma = int(0)
for numbers in range(100,151):
    suma += numbers
else:
    print(suma)

for mianownik in range(1,11):
    print(1/mianownik)

"""
password = "qwerty123"
if len(password) < 8:
    print(f"Password too short")
else:
    print(f"Password ok")
"""
sum = 0
number = 1
while number < 5:
    sum = sum + number
    number = number + 1
else:
    print("sum od numbers in <1,5> is ", sum)
