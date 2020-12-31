import re

f = open('day7/example.txt', 'r')
instructionsRaw = f.read().split('\n')

instructions = {}

def findValueForWire(key):
	wire = instructions[key]
	if 'value' in wire:
		return wire['value']
	elif wire['operation'] == '':
		result = findValueForWire(wire['operand2'])
		return result
	elif wire['operation'] == 'AND':
		if re.search('\\d+', wire['operand1']) and re.search('\\d+', wire['operand2']):
			return int(wire['operand1']) & int(wire['operand2'])
		elif re.search('\\d+', wire['operand1']):
			result = findValueForWire(wire['operand2'])
			return int(wire['operand1']) & result
		elif re.search('\\d+', wire['operand2']):
			return result & int(wire['operand2'])
		else:
			result1 = findValueForWire(wire['operand1'])
			return result1 & result2
	elif wire['operation'] == 'OR':
		if re.search('\\d+', wire['operand1']) and re.search('\\d+', wire['operand2']):
			return int(wire['operand1']) | int(wire['operand2'])
		elif re.search('\\d+', wire['operand1']):
			result = findValueForWire(wire['operand2'])
			return int(wire['operand1']) | result
		elif re.search('\\d+', wire['operand2']):
			result = findValueForWire(wire['operand1'])
			return result | int(wire['operand2'])
		else:
			result1 = findValueForWire(wire['operand1'])
			result2 = findValueForWire(wire['operand2'])
			return result1 | result2
	elif wire['operation'] == 'LSHIFT':
		result = findValueForWire(wire['operand1'])
		return  result << int(wire['operand2'])
	elif wire['operation'] == 'RSHIFT':
		result = findValueForWire(wire['operand1'])
		return result >> int(wire['operand2'])
	elif wire['operation'] == 'NOT':
		result = findValueForWire(wire['operand2'])
		return 2**16 + ~result
	else:
		print()
	

for instr in instructionsRaw:
	operand1, operation, operand2, key = re.findall(
		'(?:(?:(\\w+)\\s)?(AND|OR|LSHIFT|RSHIFT|NOT)\\s)?(\\w+)\\s->\\s([a-z]+)', instr)[0]
	if operand1 == '' and operation == '' and re.search('\\d+', operand2):
		instructions[key] = {'value': int(operand2)}
	else:
		instructions[key] = {'operand1': operand1, 'operation': operation, 'operand2': operand2}

print(findValueForWire('i'))