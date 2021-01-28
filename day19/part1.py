import re

f = open('day19/input.txt', 'r')
raw = f.read().split('\n')

inputMol = raw.pop()

replacements = {}

for repl in raw:
    matches = re.findall(r'(\w+)\s=>\s(\w+)', repl)
    replacements.setdefault(matches[0][0], []).append(matches[0][1])

pattern = ''

for replacable in replacements.keys():
    pattern += replacable + '|'

pattern = pattern[:len(pattern)-1]


options = set()
matches = re.finditer(pattern, inputMol)

for match in matches:
    for repl in replacements[match[0]]:
        options.add(inputMol[:match.regs[0][0]] + repl + inputMol[match.regs[0][1]:])

print(len(options))  