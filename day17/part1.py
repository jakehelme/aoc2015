from data import containers
from itertools import combinations

toStore = 150

combos = []

for i in range(2, len(containers) + 1):
    for combo in combinations(containers, i):
        combos.append(combo)

amount = 0
for combo in combos:
    if sum(combo) == toStore: amount += 1

print(amount)