import re

f = open('day8/input.txt', 'r')
listStrings = f.read().split('\n')

totalCode = 0
totalEncoded = 0

for x in listStrings:
	matches = re.findall('(\\\"|\\\\)', x)
	encodedLen = len(x) + 2 + len(matches)
	totalCode += len(x)
	totalEncoded += encodedLen

print(totalEncoded - totalCode)
