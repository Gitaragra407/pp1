import csv

with open("students.txt") as CSVfile:
    reader = csv.DictReader(CSVfile)
    for line in reader:
        if int(line['age']) < 30:
            print(line['first_name'],line['last_name'],line['email'])
