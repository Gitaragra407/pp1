def digitsToAdd(text):
    sum = 0
    for i in text:
        sum += int(i)
    return sum
print(digitsToAdd('7182'))