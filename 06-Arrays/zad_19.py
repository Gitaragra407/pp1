listA = [2, 3, 2, 5, 8, 1, 9, 8]
listB = []
for i in range(len(listA)):
    numCounter = 0
    for j in range(len(listA)):
        if listA[i] == listA[j]:
            numCounter += 1
    if numCounter == 1:
        listB.append(listA[i])

print(listB)