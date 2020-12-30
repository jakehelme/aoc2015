f = open('day2/input.txt', 'r')
i = f.read()

dims = i.split('\n')

total = 0

for dim in dims:
    sides = list(map(int, dim.split('x')))
    surfArea = 2 * (sides[0] * sides[1] + sides[0] * sides[2] + sides[1] * sides[2])
    smallestSide = min(sides[0] * sides[1], sides[0] * sides[2] ,sides[1] * sides[2])
    wrapping = surfArea + smallestSide
    total += wrapping

print(total)