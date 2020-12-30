f = open('day2/input.txt', 'r')
i = f.read()

dims = i.split('\n')

total = 0

for dim in dims:
    sides = list(map(int, dim.split('x')))
    sides.sort()
    around = 2 * (sides[0] + sides[1])
    bow = sides[0] * sides[1] * sides[2]
    total = total + around + bow

print(total)