import re

f = open('d5/input.txt', 'r')
strings = f.read().split('\n')

nice = 0

for s in strings:
    vowelMatches = re.findall('(a|e|i|o|u)', s)
    # print(vowelMatches)
    doubleCharMatches = re.findall('(.)\\1{1,}', s)
    # print(doubleCharMatches)
    disallowedMatches = re.findall('(ab|cd|pq|xy)', s)
    # print(disallowedMatches)

    if len(vowelMatches) >= 3 and len(doubleCharMatches) >= 1 and len(disallowedMatches) == 0:
        nice += 1

print(nice)

p2Nice = 0
for s in strings:
    pairMatches = re.findall('(..).*\\1', s)
    sandwichMatches = re.findall('(.).\\1', s)

    if len(pairMatches) > 0 and len(sandwichMatches) > 0:
        p2Nice += 1

print(p2Nice)
