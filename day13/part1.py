import re
from itertools import permutations

f = open('day13/input.txt', 'r')

data = f.read().split('\n')

guests = {}

for x in data:
    matches = re.findall(r'^(\w+)\swould\s(lose|gain)\s(\d+)\shappiness\sunits\sby\ssitting\snext\sto\s(\w+).$', x)
    if matches[0][0] not in guests:
        guests[matches[0][0]] = {}

    guests[matches[0][0]][matches[0][3]] = int(
        matches[0][2]) if matches[0][1] == 'gain' else -1 * int(matches[0][2])


combos = list(permutations(guests.keys()))

def calcTotChange(order):
	tot = 0
	for i in range(len(order)):
		if i == len(order) - 1:
			tot += guests[order[i]][order[0]] + guests[order[0]][order[i]]
		else:
			tot += guests[order[i]][order[i + 1]] + guests[order[i + 1]][order[i]]
  
	return tot

totals = []
for combo in combos:
  totals.append(calcTotChange(combo))

print(max(totals))
