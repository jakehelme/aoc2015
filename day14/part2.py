import re
import math

totalTravelTime = 2503

# f = open('day14/example.txt', 'r')
f = open('day14/input.txt', 'r')
raw = f.read().split('\n')

reindeers = []

for line in raw:
	matches = re.findall(r'(\w+).*?(\d+).*?(\d+).*?(\d+)', line)[0]
	reindeers.append({'name': matches[0], 'speed': int(matches[1]), 'travelTime': int(matches[2]), 'restTime': int(matches[3]), 'points': 0})

def calcTotalDist(reindeer, time):
	fullCycles = math.floor(time / (reindeer['travelTime'] + reindeer['restTime']))
	secondsInPartialCycle = time % (reindeer['travelTime'] + reindeer['restTime'])
	distance = fullCycles * reindeer['speed'] * reindeer['travelTime']
	if secondsInPartialCycle >= reindeer['travelTime']:
		distance += (reindeer['speed'] * reindeer['travelTime'])
	else:
		distance += (reindeer['speed'] * secondsInPartialCycle)
	
	return distance

for i in range(1, totalTravelTime + 1):
	distances = []
	for deer in reindeers:
		distTravelled = calcTotalDist(deer, i)
		distances.append(distTravelled)
		deer['distanceTravelled'] = distTravelled
	furthestDistance = max(distances)
	winners = filter(lambda x: x['distanceTravelled'] == furthestDistance, reindeers)
	for deer in winners:
		deer['points'] += 1

print(max(list(map(lambda x: x['points'], reindeers))))