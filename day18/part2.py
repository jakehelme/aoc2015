
f = open('day18/input.txt', 'r')
data = f.read().split('\n')

steps = 100

grid = []

for line in data:        
    grid.append(list(line))

def getNeighbors(x,y):
    neighbors = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            neX = x + i
            neY = y + j
            if neX < 0 or neY < 0 or neX == len(grid) or neY == len(grid[x]): continue
            if neX == x and neY == y: continue
            neighbors.append(grid[neX][neY])
    return neighbors

def nextGrid():
    newGrid = []
    for x in range(len(grid)):
        newGrid.append([])
        for y in range(len(grid[x])):
            if (x == 0 and y == 0) or (x == len(grid) - 1 and y == len(grid[x]) - 1) or (x == 0 and y == len(grid[x]) - 1) or (x == len(grid) - 1 and y == 0):
                newGrid[x].append('#')
                continue

            neighbors = getNeighbors(x,y)
            neighborsOn = 0
            for neigh in neighbors:
                if neigh == '#': neighborsOn += 1

            if grid[x][y] == '#':
                if neighborsOn == 2 or neighborsOn == 3:
                    newGrid[x].append('#')
                    continue
            else:
                if neighborsOn == 3:
                    newGrid[x].append('#')
                    continue
            newGrid[x].append('.')
    return newGrid

grid[0][0] = '#'
grid[0][len(grid) - 1] = '#'
grid[len(grid) - 1][0] = '#'
grid[len(grid) - 1][len(grid) - 1] = '#'

for i in range(steps):
    grid = nextGrid()

hashes = 0
for x in grid:
    for y in x:
        if y == '#': hashes += 1

print(hashes)
