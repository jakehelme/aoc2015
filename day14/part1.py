import re
import math

# totalTravelTime = 1000
totalTravelTime = 2503

# f = open('day14/example.txt', 'r')
f = open('day14/input.txt', 'r')
raw = f.read().split('\n')

reindeers = []

for line in raw:
	matches = re.findall(r'(\w+).*?(\d+).*?(\d+).*?(\d+)', line)[0]
	reindeers.append({'name': matches[0], 'speed': int(matches[1]), 'travelTime': int(matches[2]), 'restTime': int(matches[3])})

def calcTotalDist(reindeer):
	fullCycles = math.floor(totalTravelTime / (reindeer['travelTime'] + reindeer['restTime']))
	secondsInPartialCycle = totalTravelTime % (reindeer['travelTime'] + reindeer['restTime'])
	distance = fullCycles * reindeer['speed'] * reindeer['travelTime']
	if secondsInPartialCycle >= reindeer['travelTime']:
		distance += (reindeer['speed'] * reindeer['travelTime'])
	else:
		distance += (reindeer['speed'] * secondsInPartialCycle)
	
	return distance

distances = []
for x in reindeers:
	distances.append(calcTotalDist(x))


print(max(distances))