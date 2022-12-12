def array2str(lista):
    string = ''
    for i in lista:
        i = str(i)
        string += i
        string +=" "
    return string

def checkList(ar1,ar2):
    if len(ar1) != len(ar2):
        return 'Comparison: arrays are not the same'
    else:
        for i in range(len(ar1)):
            if ar1[i] != ar2[i]:
                return 'Comparison: arrays are not the same'
    return 'Comparison: arrays are the same'            
        

list1 = ["water","book","sky"]
list2 = ["water","book","sky"]

list3 = [True,False]
list4 = [True,False,True]

list5 = [5,3,1]
list6 = [5,3,1]

list7 = [3,2,1]
list8 = [3,2,3]

print('Array1:',array2str(list1))
print('Array2:',array2str(list2))
print('Comparison',checkList(list1, list2))

print('Array1:',array2str(list3))
print('Array2:',array2str(list4))
print('Comparison',checkList(list3, list4))

print('Array1:',array2str(list5))
print('Array2:',array2str(list6))
print('Comparison',checkList(list5, list6))

print('Array1:',array2str(list7))
print('Array2:',array2str(list8))
print('Comparison',checkList(list7, list8))