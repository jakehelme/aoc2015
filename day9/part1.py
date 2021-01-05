import re
from functools import reduce
from itertools import permutations

f = open('day9/input.txt')
input = f.read().split('\n')

destinations = {}

for x in input:
	matches = re.findall('(\\w+)\\sto\\s(\\w+)\\s=\\s(\\d+)', x)
	if matches[0][0] in destinations:
		destinations[matches[0][0]][matches[0][1]] = int(matches[0][2])
	else:
		destinations[matches[0][0]] = { matches[0][1]: int(matches[0][2]) }

	if matches[0][1] in destinations:
		destinations[matches[0][1]][matches[0][0]] = int(matches[0][2])
	else:
		destinations[matches[0][1]] = { matches[0][0]: int(matches[0][2]) }


perms = permutations(destinations)

tots = []

for x in list(perms):
	tot = 0
	for y in range(len(x) - 1):
		tot += destinations[x[y]][x[y+1]]
	tots.append(tot)
		
# print(min(tots))
print(max(tots))