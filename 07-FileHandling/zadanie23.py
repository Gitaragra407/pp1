import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C"
temperatures = re.findall("\d{2}",message)
averageTemp = 0
length = len(temperatures)
for i in range(length):
    averageTemp += int(temperatures[i])
print(averageTemp/length)