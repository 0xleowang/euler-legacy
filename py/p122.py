from time import time

start = time()

GOAL = 200

print 'START'
#exit(0)
counts = [0] + [-1 for i in range(GOAL)]
ls = [[] for i in range(GOAL+1)]

def recurrsive(num, l, n):
	if counts[num] < 0 or (counts[num] >= n and l != ls[num]):
		counts[num] = n
		ls[num] = l
	else:
		return None

	for i in l:
		new = num + i
		if new <= GOAL:
		    recurrsive(new, l+[new], n+1)
		else:
			break

recurrsive(1, [1], 0)

print counts
print sum(counts)
print time()-start