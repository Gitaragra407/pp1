arrayA = [1,0,9,4,6,7,10,2,9,11]
arrayB = [6,8,3,1,0,5,7]
def median(arr):
    arr.sort()
    length = len(arr)
    if length%2 == 0:
        return (arr[(length//2)-1] + arr[(length//2)])/2
    else:
        return arr[((length-1)//2)]
print(median(arrayA))
print(median(arrayB))
print(arrayA)
print(arrayB)
