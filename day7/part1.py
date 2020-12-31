import re

f = open('day7/example.txt', 'r')
instructionsRaw = f.read().split('\n')

instructions = {}

for instr in instructionsRaw:
	matches = re.findall('(?:(?:([a-z]+)\\s)?(AND|OR|LSHIFT|RSHIFT|NOT)\\s)?(\\w+)\\s->\\s([a-z]+)', instr)
	instructions[matches[0][3]] = {'value': matches[0][2]}