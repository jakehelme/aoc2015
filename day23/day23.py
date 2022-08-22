import re

filestream = open('day23/input.txt')
raw = filestream.read()


class Instruction:
    def __init__(self, type, reg, val):
        self.type = type
        self.reg = reg
        self.val = val


def createInstruction(raw):
    instType = raw[:3]
    reg = None
    val = None
    regAndOrVal = raw[4:].replace(' ', '')
    regAndOrVal = regAndOrVal.split(',')
    if len(regAndOrVal) > 1:
        reg = regAndOrVal[0]
        val = int(regAndOrVal[1][1:])
    elif not (re.search('\d+', regAndOrVal[0])):
        reg = regAndOrVal[0]
    else:
        val = int(regAndOrVal[0])

    return Instruction(instType, reg, val)


instructions = raw.split('\n')
instructions = list(map(createInstruction, instructions))


def runInstructions(startingA, startingB):
    instIndex = 0
    a = startingA
    b = startingB
    while instIndex < len(instructions) and instIndex >= 0:
        if instructions[instIndex].type == 'hlf':
            if instructions[instIndex].reg == 'a':
                a = int(a / 2)
            else:
                b = int(b / 2)
            instIndex += 1
        elif instructions[instIndex].type == 'tpl':
            if instructions[instIndex].reg == 'a':
                a = int(a * 3)
            else:
                b = int(b * 3)
            instIndex += 1
        elif instructions[instIndex].type == 'inc':
            if instructions[instIndex].reg == 'a':
                a += 1
            else:
                b += 1
            instIndex += 1
        elif instructions[instIndex].type == 'jmp':
            instIndex = instIndex + instructions[instIndex].val
        elif instructions[instIndex].type == 'jie':
            if instructions[instIndex].reg == 'a':
                if a % 2 == 0:
                    instIndex = instIndex + instructions[instIndex].val
                else:
                    instIndex += 1
            else:
                if b % 2 == 0:
                    instIndex = instIndex + instructions[instIndex].val
                else:
                    instIndex += 1
        elif instructions[instIndex].type == 'jio':
            if instructions[instIndex].reg == 'a':
                if a == 1:
                    instIndex = instIndex + instructions[instIndex].val
                else:
                    instIndex += 1
            else:
                if b == 1:
                    instIndex = instIndex + instructions[instIndex].val
                else:
                    instIndex += 1
        else:
            raise Exception('nope')

    print(b)


runInstructions(0, 0)
runInstructions(1, 0)
