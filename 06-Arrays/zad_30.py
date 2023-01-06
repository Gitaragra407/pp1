from random import randrange
array_length = int(input('How many items should the list have?'))
array = []
for i in range(array_length):
    array.append(randrange(1,999))
print(array)
def rand_elem(array):
    return array[randrange(len(array))]
for i in range(array_length):
    print(rand_elem(array))
