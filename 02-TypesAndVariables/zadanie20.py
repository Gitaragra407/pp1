from random import randrange
import math
def sum_of_dice_rolls(number_of_rolls):
    sum_of_values = 0
    roll_result = 0
    for i in range(number_of_rolls):
     roll_result = randrange(6)
     roll_result+1
     sum_of_values += roll_result
     print("roll ",i+1,"result ", roll_result)
    else:
        print(sum_of_values)

user_input=int(input("Enter the amount of die rolls\n"))
sum_of_dice_rolls(user_input)