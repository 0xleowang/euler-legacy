limit = 1000000

n = 0
a = 3
while 4 * a <= limit:
    b = a
    s = 0
    while True:
        s += 4 * b
        if s <= limit:
            b += 2
            n += 1
            print a, b, s
        else:
            break
    a += 2

a = 2
while 4 * a <= limit:
    b = a
    s = 0
    while True:
        s += 4 * b
        if s <= limit:
            b += 2
            n += 1
            print a, b, s
        else:
            break
    a += 2

print n