import re

puzzleInput = '1321131112'

pattern = '(?:(?:(\\d)(\\1)+)|\\d)'

matches = re.findall(pattern, puzzleInput)

print(matches)