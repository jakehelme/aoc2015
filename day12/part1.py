import re

# f = open('day12/example.txt', 'r')
f = open('day12/input.txt', 'r')
json = f.read()
matches = re.findall(r'-?\d+', json)
numbers = list(map(lambda x: int(x), matches))

print(sum(numbers))
