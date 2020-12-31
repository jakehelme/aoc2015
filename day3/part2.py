def part2(dirs):
	santaDirs = dirs[::2]
	roboDirs = dirs[1::2]
	houses = {'0,0': 2}
	santaPos = {'x':0,'y':0}
	roboPos = {'x':0,'y':0}
	loopSize = max(len(santaDirs), len(roboDirs))
	for i in range(loopSize):
		if i < len(santaDirs):
			move(santaPos, santaDirs[i], houses)
		if i < len(roboDirs):
			move(roboPos, roboDirs[i], houses)
	
	print(len(houses))

def move(pos, direction, houses):
	if direction == '^':
		pos['y'] = pos['y'] + 1
	elif direction == '>':
		pos['x'] = pos['x'] + 1
	elif direction == 'v':
		pos['y'] = pos['y'] - 1
	elif direction == '<':
		pos['x'] = pos['x'] - 1

	currPos = str(pos['x']) + ',' + str(pos['y'])
	if currPos in houses:
		houses[currPos]	 = houses[currPos] + 1
	else:
		houses[currPos]	 = 1
	