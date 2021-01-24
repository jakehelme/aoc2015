import re
from functools import reduce

f = open('day15/input.txt', 'r')
data = f.read().split('\n')

pat = r'(\w+):.*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+).*?(-?\d+)'
ingsDict = {}

for ingredient in data:
    matches = re.findall(pat, ingredient)
    ingsDict[matches[0][0]] = {'cap': int(matches[0][1]), 'dur': int(matches[0][2]), 'fla': int(
        matches[0][3]), 'tex': int(matches[0][4]), 'cal': int(matches[0][5])}

ings = list(ingsDict.keys())
combos = []
sumTo = 100
maxDepth = len(ingsDict)

def getCombos(depth, *nums):
    if depth == maxDepth:
        if sum(nums) < sumTo:
            combos.append(tuple([*nums, sumTo - sum(nums)]))
    else:
        for i in range(1, sumTo - maxDepth + 2):
            getCombos(depth + 1, *nums, i)

getCombos(1)

scores = []
for combo in combos:
    cap = 0
    dur = 0
    fla = 0
    tex = 0
    cal = 0
    for idx, amount in enumerate(combo):
        cap += ingsDict[ings[idx]]['cap'] * amount
        dur += ingsDict[ings[idx]]['dur'] * amount
        fla += ingsDict[ings[idx]]['fla'] * amount
        tex += ingsDict[ings[idx]]['tex'] * amount
        cal += ingsDict[ings[idx]]['cal'] * amount
    if cap < 0: cap = 0
    if dur < 0: dur = 0
    if fla < 0: fla = 0
    if tex < 0: tex = 0
    if cal == 500: scores.append(cap * dur * fla * tex)

print(max(scores))