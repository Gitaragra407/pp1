from random import randrange
import math
def dice_roll():
    roll_result = randrange(6)
    roll_result+1
    return roll_result

dice_outcome = dice_roll()
user_input=int(input("Podaj ilość wyrzuconych oczek przez komputer\n"))
if user_input == dice_outcome:
    print("udało ci się zgadnąć")
else:
    print("False")