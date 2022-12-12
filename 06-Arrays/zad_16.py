def star(num):
    stringStars = ''
    for i in range(num):
        stringStars += '*'
    else:
        return stringStars
numbersList = [12, 6, 4, 9, 3]
for i in numbersList:
    print(f'{i}:{star(i)}')