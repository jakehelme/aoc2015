# X is any element except Rn or Y or Ar
# e => XX or X => XX
# X => XRnXAr or XRnXYXAr or XRnXYXYXAr | X(X) or X(X,X) or X(X,X,X)
# XX => X to single element will take element count - 1
# because X(X) => X brackets are free, hence count(elements) - count(brackets) - 1
# because X(X,X) => X reduces length by 2 for each comma, then count(elements) - count(brackets) - 2*count(commas) - 1

import re

f = open('day19/input.txt')
raw = f.read().split('\n')

inputMol = raw.pop()

elementCount = len(re.findall(r'[A-Z][a-z]?', inputMol))
bracketCount = len(re.findall(r'Rn|Ar', inputMol))
commaCount = len(re.findall(r'Y', inputMol))

print(elementCount - bracketCount - 2 * commaCount - 1)