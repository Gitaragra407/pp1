array = [0,2.3,33.1,25.3,2.5,9.2,33.9,12.3,90.3,32.2,23.9]
array.sort()
print(array)
UsrNum = float(input("Enter number "))
for i in range(len(array)):
    if UsrNum < array[i]:
        print(len(array)-i)
        break