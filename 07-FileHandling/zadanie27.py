import re
with open('grades.txt') as File:
    for line in File:
         if 'Name' in line:
            print(line,end='')
         else:
            mean = 0.0
            grades = re.findall(r"\b\d+\.?\d*\b", line)
            for i in grades:
                mean += float(i)
            print('Mean of grades',mean/len(grades))