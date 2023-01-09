import re
string = 'To be, or not to be, that is the question'
vowels = re.findall("[aeiouAEIOU]",string)
print(len(vowels))
