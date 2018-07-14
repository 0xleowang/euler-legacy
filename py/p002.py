x, y, s = 1, 1, 0
while x + y < 4000000:
    s += x + y
    x, y = x + 2*y, 2*x + 3*y

print s