nCounter = 0
FILE_name = input("Enter the file name to search for the amount of lines in the file: ")
with open(FILE_name) as FILE:
    for i in FILE:
        nCounter += 1
print(f"File name: {FILE_name}\nNumber of lines:{nCounter}")