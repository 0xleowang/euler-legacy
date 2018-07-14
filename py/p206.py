import re
from time import time

start = time()

lower = 1020304050607080900
upper = 1929394959697989990

lb = int(lower ** 0.5)
rb = int((upper ** 0.5) / 10) * 10

while lb < rb:
    lb_square = 0
    rb_square = 0

    try:
        lb_square = re.search('1\d2\d3\d4\d5\d6\d7\d8\d9\d0', str(lb * lb)).group(0)
    except:
        None
    try:
        rb_square = re.search('1\d2\d3\d4\d5\d6\d7\d8\d9\d0', str(rb * rb)).group(0)
    except:
        None

    if lb_square:
        print lb, time() - start
        break
    lb += 10
    if rb_square:
        print rb, time() - start
        break
    rb -= 10

    print lb, rb, time() - start