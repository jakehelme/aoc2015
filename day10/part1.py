import re

puzzleInput = '1321131112'
output = puzzleInput
pattern = r'(?:((\d)(\2+))|(\d))'



for i in range(50):
    matches = re.findall(pattern, output)
    nextStr = ''
    for match in matches:
        if match[0]:
            nextStr += str(len(match[0])) + match[0][0]
        else:
            nextStr += '1' + match[3]
    
    output = nextStr

print(len(output))