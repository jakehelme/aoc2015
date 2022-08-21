import math
import re
import sys
import itertools

def createShopItem(line):
    (name, cost, damage, armor) = re.split('\s{2,}', line)
    return {'name': name, 'cost': int(cost), 'damage': int(damage), 'armor': int(armor)}


def populateShop():
    raw = open('day21/shop.txt', 'r').read()
    rW, rA, rR = raw.split('\n\n')
    rW = rW.split('\n')
    rA = rA.split('\n')
    rR = rR.split('\n')
    rW.pop(0)
    rA.pop(0)
    rR.pop(0)
    weapons = list(map(createShopItem, rW))
    armors = list(map(createShopItem, rA))
    rings = list(map(createShopItem, rR))
    return (weapons, armors, rings)


def calculateDamage(damage, armor):
    return damage - armor if damage > armor else 1


def doesPlayerWin(player, boss):
    playerDamage = calculateDamage(player['damage'], boss['armor'])
    bossDamage = calculateDamage(boss['damage'], player['armor'])

    hitsForPlayerToWin = math.ceil(boss['hp'] / playerDamage)
    hitsForBossToWin = math.ceil(player['hp'] / bossDamage)

    return hitsForPlayerToWin <= hitsForBossToWin


def part1():
    lowestCost = sys.maxsize
    cheapestSet = []
    weapons, armors, rings = populateShop()

    armors.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})
    rings.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})
    rings.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})

    for weapon in weapons:
        for armor in armors:
            for ringSets in itertools.combinations(rings, 2):
                playerDamage = weapon['damage'] + ringSets[0]['damage'] + ringSets[1]['damage']
                playerArmor = armor['armor'] + ringSets[0]['armor'] + ringSets[1]['armor']
                if doesPlayerWin({'hp': 100, 'damage': playerDamage, 'armor': playerArmor}, {'hp': 104, 'damage': 8, 'armor': 1}):
                    cost = weapon['cost'] + armor['cost'] + ringSets[0]['cost'] + ringSets[1]['cost']
                    if(cost < lowestCost):
                        lowestCost = cost
                        cheapestSet = [weapon['name'], armor['name'], ringSets[0]['name'], ringSets[1]['name']]

                
    print(lowestCost, cheapestSet)

def part2():
    highestCost = 0
    mostExpensiveSet = []
    weapons, armors, rings = populateShop()

    armors.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})
    rings.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})
    rings.append({'name': 'Empty', 'cost': 0, 'damage': 0, 'armor': 0})

    for weapon in weapons:
        for armor in armors:
            for ringSets in itertools.combinations(rings, 2):
                playerDamage = weapon['damage'] + ringSets[0]['damage'] + ringSets[1]['damage']
                playerArmor = armor['armor'] + ringSets[0]['armor'] + ringSets[1]['armor']
                if not(doesPlayerWin({'hp': 100, 'damage': playerDamage, 'armor': playerArmor}, {'hp': 104, 'damage': 8, 'armor': 1})):
                    cost = weapon['cost'] + armor['cost'] + ringSets[0]['cost'] + ringSets[1]['cost']
                    if(cost > highestCost):
                        highestCost = cost
                        mostExpensiveSet = [weapon['name'], armor['name'], ringSets[0]['name'], ringSets[1]['name']]

                
    print(highestCost, mostExpensiveSet)

part1()
part2()
