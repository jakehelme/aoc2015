def part1(dirs):
	houses = {'0,0': 1}
	pos = {'x':0,'y':0}
	for dir in dirs:
		if dir == '^':
			pos['y'] = pos['y'] + 1
		elif dir == '>':
			pos['x'] = pos['x'] + 1
		elif dir == 'v':
			pos['y'] = pos['y'] - 1
		elif dir == '<':
			pos['x'] = pos['x'] - 1 

		currPos = str(pos['x']) + ',' + str(pos['y'])
		if currPos in houses:
			houses[currPos]	 = houses[currPos] + 1
		else:
			houses[currPos]	 = 1
	
	print(len(houses))