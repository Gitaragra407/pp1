quant = 0
sumOfNumbers = 0
while True:
    temp = float(input("Enter number"))
    if temp == 0:
        break
    quant +=1
    sumOfNumbers += temp
print(f"RESULT: Quantity={quant}, Sum={sumOfNumbers}, Mean={sumOfNumbers/quant}")