from part1 import part1
from part2 import part2

f = open('day3/input.txt', 'r')
input = f.read()
dirs = list(input)

part1(dirs)
part2(dirs)

