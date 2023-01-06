array = [1,0,9,4,6,7,10,2,9,11]
newArray = []
for i in range(len(array)):
    if array[i]%2==0:
        newArray.insert(0,array[i])
    else:
        newArray.append(array[i])
print(newArray)