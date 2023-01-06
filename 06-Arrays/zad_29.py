arrayA = [5,4,3,2,6,5]
arrayB = [2,4,5,99]
arrayBLength = len(arrayB)
counter = 0
for i in range(arrayBLength):
    if arrayA.count(arrayB[i]) > 0:
        counter += 1
if counter == arrayBLength:
    print('ArrayB is a subset of arrayA')
else:
    print('ArrayB is not a subset of arrayA')