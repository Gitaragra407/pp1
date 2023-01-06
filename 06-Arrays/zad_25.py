array = [4,2,8,4,7,9,5]
def minMax(arr):
    arrayNew = []
    maximum = arr[0]
    minimum = arr[0]
    for i in range(len(arr)):
        if minimum > arr[i]:
            minimum = arr[i]
        elif maximum < arr[i]:
            maximum = arr[i]
    arrayNew.append(minimum)
    arrayNew.append(maximum)
    return arrayNew
print(minMax(array))
