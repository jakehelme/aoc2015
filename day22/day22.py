import sys

spells = {
    'Magic Missile': 53,
    'Drain': 73,
    'Shield': 113,
    'Poison': 173,
    'Recharge': 229
}


def copyGame(game):
    effects = {}
    for effect in game['effects'].keys():
        effects[effect] = game['effects'][effect]
    return {
        'player': {
            'hp': game['player']['hp'],
            'armor': game['player']['armor'],
            'mana': game['player']['mana'],
            'manaSpent': game['player']['manaSpent']
        },
        'boss': {
            'hp': game['boss']['hp'],
            'damage': game['boss']['damage']
        },
        'effects': effects
    }


def createPlayer():
    return {'hp': 50, 'armor': 0, 'mana': 500, 'manaSpent': 0}


def createBoss():
    return {'hp': 58, 'damage': 9}


def playRound(game, spellToCast, part2=False):
    player = game['player']
    boss = game['boss']
    effects = game['effects']

    def checkMana():
        if player['mana'] > spells[spellToCast]:
            player['mana'] -= spells[spellToCast]
            player['manaSpent'] += spells[spellToCast]
            return True
        else:
            return False

    def checkEffects():
        for effect in effects.keys():
            if effect == spellToCast:
                return False
        return True

    def processEffects():
        toDeletes = []
        for effect in effects.keys():
            effects[effect] -= 1
            if effect == 'Shield':
                if effects[effect] == 0:
                    player['armor'] = 0
            elif effect == 'Poison':
                boss['hp'] -= 3
            elif effect == 'Recharge':
                player['mana'] += 101

            if effects[effect] == 0:
                toDeletes.append(effect)

        for toDelete in toDeletes:
            del effects[toDelete]

        return boss['hp'] > 0

    if part2:
        player['hp'] -= 1
        if player['hp'] <= 0:
            return 'Boss wins'

    if not (processEffects()):
        return 'Player wins'

    if not (checkMana()):
        return 'OoM'

    if not (checkEffects()):
        return 'Effect already in use'

    if spellToCast == 'Magic Missile':
        boss['hp'] -= 4
    elif spellToCast == 'Drain':
        boss['hp'] -= 2
        player['hp'] += 2
    elif spellToCast == 'Shield':
        player['armor'] = 7
        effects['Shield'] = 6
    elif spellToCast == 'Poison':
        effects['Poison'] = 6
    elif spellToCast == 'Recharge':
        effects['Recharge'] = 5
    else:
        return 'Spell doesn''t exist'

    if boss['hp'] <= 0:
        return 'Player wins'

    if not (processEffects()):
        return 'Player wins'

    bossDamage = boss['damage'] - \
        player['armor'] if boss['damage'] - player['armor'] > 1 else 1
    player['hp'] -= bossDamage

    if player['hp'] <= 0:
        return 'Boss wins'

    return 'Game continues'


def part1():
    keepPlaying = []
    lowestManaCost = sys.maxsize
    lowestMoves = []
    for spell in spells:
        game = {'player': createPlayer(), 'boss': createBoss(), 'effects': {}}
        result = playRound(game, spell)
        if result == 'Game continues':
            keepPlaying.append({'game': copyGame(game), 'history': [spell]})
        elif result == 'Player wins':
            if game['player']['manaSpent'] < lowestManaCost:
                lowestManaCost = game['player']['manaSpent']
                lowestMoves = game['player']['history']

    while len(keepPlaying) > 0 and any(roundToPlay['game']['player']['manaSpent'] < lowestManaCost for roundToPlay in keepPlaying):
        nextRound = []
        for round in keepPlaying:
            for spell in spells:
                newGame = copyGame(round['game'])
                result = playRound(newGame, spell)
                if result == 'Game continues':
                    nextRound.append(
                        {'game': copyGame(newGame), 'history': round['history'] + [spell]})
                elif result == 'Player wins':
                    if newGame['player']['manaSpent'] < lowestManaCost:
                        lowestManaCost = newGame['player']['manaSpent']
                        lowestMoves = round['history']
        nextRound = list(
            filter(lambda r: r['game']['player']['manaSpent'] < lowestManaCost, nextRound))
        keepPlaying = nextRound
    print('part 1:', lowestManaCost)


def part2():
    keepPlaying = []
    lowestManaCost = sys.maxsize
    lowestMoves = []
    for spell in spells:
        game = {'player': createPlayer(), 'boss': createBoss(), 'effects': {}}
        result = playRound(game, spell, True)
        if result == 'Game continues':
            keepPlaying.append({'game': copyGame(game), 'history': [spell]})
        elif result == 'Player wins':
            if game['player']['manaSpent'] < lowestManaCost:
                lowestManaCost = game['player']['manaSpent']
                lowestMoves = game['player']['history']

    while len(keepPlaying) > 0 and any(roundToPlay['game']['player']['manaSpent'] < lowestManaCost for roundToPlay in keepPlaying):
        nextRound = []
        for round in keepPlaying:
            for spell in spells:
                newGame = copyGame(round['game'])
                result = playRound(newGame, spell, True)
                if result == 'Game continues':
                    nextRound.append(
                        {'game': copyGame(newGame), 'history': round['history'] + [spell]})
                elif result == 'Player wins':
                    if newGame['player']['manaSpent'] < lowestManaCost:
                        lowestManaCost = newGame['player']['manaSpent']
                        lowestMoves = round['history']
        nextRound = list(
            filter(lambda r: r['game']['player']['manaSpent'] < lowestManaCost, nextRound))
        keepPlaying = nextRound
    print('part 2:', lowestManaCost)


part1()
part2()
