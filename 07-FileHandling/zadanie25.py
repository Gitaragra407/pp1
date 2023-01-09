import re
string = 'To be, or not to be, that is the question'
words = re.findall(r"\b\w+\b",string)
print(len(words))