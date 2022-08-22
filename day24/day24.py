from functools import reduce
from itertools import combinations
import operator

stream = open('day24/input.txt')
raw = stream.read()

def balance(balanceGroups):
    weights = list(map(int, raw.split('\n')))
    sectionWeight = int(reduce(operator.add, weights) / balanceGroups)
    comboLen = 1
    keepGoing = True

    while keepGoing:
        combos = list(combinations(weights, comboLen))
        goodConfigs = list(filter(lambda combo: reduce(operator.add, combo) == sectionWeight, combos))

        if len(goodConfigs) > 0:
            keepGoing = False
        comboLen += 1

    QEs = list(map(lambda goodConfig: reduce(operator.mul, goodConfig), goodConfigs))

    return min(QEs)

print('part 1:', balance(3))
print('part 2:', balance(4))