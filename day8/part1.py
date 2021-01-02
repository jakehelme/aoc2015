import re

f = open('day8/input.txt', 'r')
listStrings = f.read().split('\n')

totalCode = 0
totalInString = 0

for x in listStrings:
	totalChars = len(x)
	matches = re.findall('(\\\\\\"|\\\\\\\\|\\\\x[0-9a-f]{2})', x)
	escapeChars = 0
	if matches:
		for y in matches:
			if y[0:2] == '\\x':
				escapeChars += 3
			elif y == '\\"' or y == '\\\\':
				escapeChars += 1
	
	inString = totalChars - 2 - escapeChars
	totalCode += totalChars
	totalInString += inString

print(totalCode - totalInString)