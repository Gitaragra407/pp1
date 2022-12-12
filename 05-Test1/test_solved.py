def f(number1, number2 ,number3):
    maksimum = number1
    minimum = number3
    if number1 < number2 and number2 > number3:
        maksimum = number2
    else:
        maksimum = number3
    if number3 > number2 and number2 < number1:
        minimum = number2
    else:
        minimum = number1
    return maksimum - minimum

print(f(9,9,9))