import re

pwLength = 8

rule1 = r'[a-z]*?(?:abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)[a-z]*?'
rule2 = r'^[^iol]+$'
rule3 = r'[a-z]*?([a-z])\1[a-z]*?([a-z])\2[a-z]*?'

def incrementString(target):
	for i in range(pwLength):
		j = pwLength - i - 1
		charIndex = ord(target[j])
		if charIndex < 122:
			target = target[0:j] + chr(charIndex + 1) + target[j+1:]
			break
		else:
			target = target[0:j] + 'a' + target[j+1:]
	return target

# test = 'vzbxxyzz'
test = 'vzbxxyzz'

while(True):
	test = incrementString(test)

	match1 = re.match(rule1, test)
	match2 = re.match(rule2, test)
	match3 = re.match(rule3, test)

	if match1 and match2 and match3: break

print(test)