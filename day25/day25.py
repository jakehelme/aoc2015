import re

starting = 20151125
mult = 252533
mod = 33554393

stream = open('day25/input.txt')
raw = stream.read()
(ansRow, ansCol) = list(map(int, re.findall('\d+', raw)))
ansRow -= 1
ansCol -= 1

grid = [[]]
grid[0].append(starting)


def nextCode(prev):
    intermediate = prev * mult
    return intermediate % mod

rowIndex = 0
colIndex = 0
next = starting
looping = True

def shouldStop(row, col):
    return row == ansRow and col == ansCol

while looping:
    next = nextCode(next)
    if rowIndex == 0:
        grid.append([next])
        rowIndex = colIndex + 1
        colIndex = 0
    else:
        rowIndex -= 1
        colIndex += 1
        grid[rowIndex].append(next)

    if shouldStop(rowIndex, colIndex):
        looping = False

print('ans:', grid[ansRow][ansCol])
