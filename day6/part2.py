import re

def perfAction(topLeft, botRight, action, grid):
    for x in range(topLeft[0], botRight[0] + 1):
        for y in range(topLeft[1], botRight[1] + 1):
            if action == 'turn on':
                grid[y][x] += 1
            elif action == 'turn off':
                grid[y][x] -= 1
                if grid[y][x] < 0:
                    grid[y][x] = 0
            else:
                grid[y][x] += 2

gridLength = 1000
f = open('d6/input.txt', 'r')
rawInstructions = f.read().split('\n')

grid = [[0 for x in range(gridLength)] for y in range(gridLength)]

for instr in rawInstructions:
    matches = re.findall('(toggle|turn\\soff|turn\\son)\\s(\\d+),(\\d+)\\sthrough\\s(\\d+),(\\d+)', instr)
    action = matches[0][0]
    topLeft = (int(matches[0][1]), int(matches[0][2]))
    botRight = (int(matches[0][3]), int(matches[0][4]))
    perfAction(topLeft, botRight, action, grid)

lightBrightness = 0
for x in range(gridLength):
    for y in range(gridLength):
        lightBrightness += grid[y][x]

print(lightBrightness)


    