array = [6,8,3,1,0,5,7]
MaxVal = max(array)
secondVal = 0 
for i in range(len(array)-1,0,-1):
    if array[i] < MaxVal and array[i] > secondVal:
        secondVal = array[i]
print(secondVal)