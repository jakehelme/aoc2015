import json

f = open('day12/input.txt', 'r')
data = json.load(f)

def sumContentsIgnoringRed(toCheck):
	containerTotal = 0
	if isinstance(toCheck, list):
		for item in toCheck:
			if isinstance(item, int):
				containerTotal += item
			else:
				containerTotal += sumContentsIgnoringRed(item)
	elif isinstance(toCheck, dict):
		for value in toCheck.values():
			if isinstance(value, int):
				containerTotal += value
			elif isinstance(value, str) and value == 'red':
				return 0
			else:
				containerTotal += sumContentsIgnoringRed(value)
	
	return containerTotal


print(sumContentsIgnoringRed(data))

