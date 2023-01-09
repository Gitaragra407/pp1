import re
with open('Random.txt') as File:
    content = File.read()
    sixminwords = re.findall(r"\b\w{6,}\b", content)
    for i in sixminwords:
        print(i)