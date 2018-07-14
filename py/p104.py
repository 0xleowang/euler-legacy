from math import *
from time import time

def is_pandigital(n):
	digits = str(n)
	if len(digits) != 9:
		return False
	for i in "123456789":
		if i not in digits:
			return False
	return True

start = time()

a = log10((1 + sqrt(5)) / 2)
b = log10(sqrt(5))

f_k_1 = 86168291600238450732788312165664788095941068326060883324529903470149056115823592713458328176574447204501L % 1000000000
f_k = 139423224561697880139724382870407283950070256587697307264108962948325571622863290691557658876222521294125L % 1000000000
k = 500
while True:
    f_k_1, f_k = f_k, (f_k_1 + f_k) % 1000000000
    k += 1

    last = f_k
    if not is_pandigital(last):
        continue

    t = k * a - b
    first = int(pow(10, t - int(t) + 8))
    if not is_pandigital(first):
    	continue

    print k
    break

end = time()
print "Time: %f" % (end - start)