x = float(input("Podaj x: "))
y = float(input("Podaj y: "))
if x and y > 0:
    print("To pierwsza ćwiartka wykresu")
elif x < 0 and y > 0:
    print("To druga ćwiartka wykresu")
elif x and y < 0:
    print("To trzecia ćwiartka wykresu")
elif x < 0 and y > 0:
    print("To czwarta ćwiartka wykresu")
else:
    print("X lub Y jest równe zero")