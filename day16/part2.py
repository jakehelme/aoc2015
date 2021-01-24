import re

f = open('day16/input.txt', 'r')
data = f.read().split('\n')

pattern = r'Sue\s(\d+):\s(\w+):\s(\d+),\s(\w+):\s(\d+),\s(\w+):\s(\d+)'

sues = []
for line in data:
    sueIndex, prop1, prop1val, prop2, prop2val, prop3, prop3val = re.match(pattern, line).groups()
    sues.append({prop1: int(prop1val), prop2: int(prop2val), prop3: int(prop3val)})



for idx, sue in enumerate(sues):
    matches = 0
    if 'children' in sue and sue['children'] == 3: matches += 1
    if 'cats' in sue and sue['cats'] > 7: matches += 1
    if 'samoyeds' in sue and sue['samoyeds'] == 2: matches += 1
    if 'pomeranians' in sue and sue['pomeranians'] < 3: matches += 1
    if 'akitas' in sue and sue['akitas'] == 0: matches += 1
    if 'vizslas' in sue and sue['vizslas'] == 0: matches += 1
    if 'goldfish' in sue and sue['goldfish'] < 5: matches += 1
    if 'trees' in sue and sue['trees'] > 3: matches += 1
    if 'cars' in sue and sue['cars'] == 2: matches += 1
    if 'perfumes' in sue and sue['perfumes'] == 1: matches += 1
    if matches == 3:
        print(idx + 1)
        break
