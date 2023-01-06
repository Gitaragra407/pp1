from random import randrange
array_length = int(input('How many items should the list have?'))
array = []
for i in range(array_length):
    array.append(randrange(1,999))
print(array)
for i in range(array_length*4+array_length+1):
    print('-',end='')
print()
for i in range(array_length):
    if array[i] < 10:
        print(f'|   {array[i]}',end='')
    elif array[i] > 10 and array[i] < 100:
        print(f'|  {array[i]}',end='')
    else:
        print(f'| {array[i]}',end='')
print('|')
for i in range(array_length*4+array_length+1):
    print('-',end='')
print()