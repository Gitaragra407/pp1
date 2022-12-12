names = ['Genowefa', 'Onufry', 'Celestyna', 'Alojzy', 'Pankracy']
print('names: ',end='')
for i in names:
    print(i,end=' ')
print()
longest=0
longestName=''
for i in names:
    if len(i)>longest:
        longest = len(i)
        longestName = i
else:
    print('Longest name:',longestName)