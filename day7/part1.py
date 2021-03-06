import numpy
import re

f = open('day7/input.txt', 'r')
instructionsRaw = f.read().split('\n')

instructions = {}

def tryFindValue(inst):
	if 'value' in inst:
		return
	elif inst['operation'] == '':
		if 'value' in instructions[inst['operand2']]:
			inst['value'] = instructions[inst['operand2']]['value']
	elif inst['operation'] == 'AND':
		if not inst['operand1'].isnumeric() and 'value' in instructions[inst['operand1']] and 'value' in instructions[inst['operand2']]:
			inst['value'] = instructions[inst['operand1']]['value'] & instructions[inst['operand2']]['value']
		elif inst['operand1'].isnumeric() and 'value' in instructions[inst['operand2']]:
			inst['value'] = numpy.uint16(inst['operand1']) & instructions[inst['operand2']]['value']
	elif inst['operation'] == 'OR':
		if 'value' in instructions[inst['operand1']] and 'value' in instructions[inst['operand2']]:
			inst['value'] = instructions[inst['operand1']]['value'] | instructions[inst['operand2']]['value']
	elif inst['operation'] == 'LSHIFT':
		if 'value' in instructions[inst['operand1']]:
			inst['value'] = instructions[inst['operand1']]['value'] << numpy.uint16(inst['operand2'])
	elif inst['operation'] == 'RSHIFT':
		if 'value' in instructions[inst['operand1']]:
			inst['value'] = instructions[inst['operand1']]['value'] >> numpy.uint16(inst['operand2'])
	elif inst['operation'] == 'NOT':
		if 'value' in instructions[inst['operand2']]:
			inst['value'] = ~instructions[inst['operand2']]['value']

def filterWithoutValues(x):
	return not 'value' in x

for instr in instructionsRaw:
	operand1, operation, operand2, key = re.findall(
		'(?:(?:(\\w+)\\s)?(AND|OR|LSHIFT|RSHIFT|NOT)\\s)?(\\w+)\\s->\\s([a-z]+)', instr)[0]
	if operand1 == '' and operation == '' and re.search('\\d+', operand2):
		instructions[key] = {'value': numpy.uint16(operand2)}
	else:
		instructions[key] = {'operand1': operand1, 'operation': operation, 'operand2': operand2}

missingValues = True
while missingValues:
	for instr in instructions:
		tryFindValue(instructions[instr])
	missingValues = False
	for instr in instructions:
		if 'value' not in instructions[instr]:
			missingValues = True
			break

print(instructions['a']['value'])