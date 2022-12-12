import mymath
win = False
while win == False:
    komputer_answer = int(mymath.generate_number())
    answer = int(mymath.read_number())
    if answer == komputer_answer:
        win = True
    else:
        print("Try again")

print("You win")
