with open('MeatAndFish.txt') as FILE1:
    with open("GrainsAndBread.txt") as FILE2:
        with open("shoppinglist.txt",'w') as FILE3:
            FILE3.write(FILE1.read())
            FILE3.write('\n'+FILE2.read())