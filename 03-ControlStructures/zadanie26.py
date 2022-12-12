code = "0805"
for i in range(3):
    enteredCode = input("Enter the PIN code:")
    if enteredCode == code:
        print("Correct PIN")
        break
    else:
        print("Incorrect...")
else:
    print("Sorry, your payment card has been blocked.")