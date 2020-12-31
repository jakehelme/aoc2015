import hashlib
import time

start = time.time()
secret = 'yzbqklnj'
i = 0
while True:
	i += 1
	toCheck = secret + str(i)
	result = hashlib.md5(toCheck.encode('utf-8')).hexdigest()
	if result[:6] == '000000':
		break

print(i)
end = time.time()
print(end - start)