import time

input = 33100000

def getFactors(product):
    factors = set()
    for i in range(1, int(product**0.5) + 1):
        if product % i == 0:
            factors.add(i)
            factors.add(int(product/i))
    return factors


def part1():
    houseNumber = 0
    while True:
        houseNumber += 1
        presents = sum(getFactors(houseNumber)) * 10
        if (presents > input):
            print('part1:', houseNumber)
            break

def part2():
    housesVisited = {}
    houseNumber = 0
    while True:
        houseNumber += 1
        elvesVisiting = []
        factorElves = getFactors(houseNumber)
        for elf in factorElves:
            if housesVisited.get(elf):
                housesVisited[elf] += 1
            else:
                housesVisited[elf] = 1
            
            if housesVisited[elf] < 50:
                elvesVisiting.append(elf)
        
        presents = sum(elvesVisiting) * 11
        if presents > input:
            print('part2:', houseNumber)
            break


start = time.time()
part1()
mid = time.time()
print('part 1 took:', mid - start)
part2()
end = time.time()
print('part 2 took:', end - mid)
print('total:', end - start)